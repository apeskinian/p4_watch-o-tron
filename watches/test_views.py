from django.test import TestCase
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from unittest.mock import patch
from .models import Watch, WatchList, WatchMovement
from .forms import WatchForm, ListForm, MovementForm
from .views import *


class TestGetUserLists(TestCase):

    def setUp(self):
        # set up a user
        self.user = User.objects.create_user(
            username='user',
            password='password'
        )
        # set up a test movement for watch objects
        self.test_movement = WatchMovement.objects.create(
            movement_name='movement'
        )
        # set up default lists
        self.collection_list = WatchList.objects.create(
            friendly_name='collection'
        )
        self.wishlist_list = WatchList.objects.create(
            friendly_name='wish-list'
        )
        # set up custom list for user
        self.custom_list = WatchList.objects.create(
            friendly_name='custom-list'
        )
        # create a watch for each list
        self.watch1 = Watch.objects.create(
            owner=self.user,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.collection_list
        )
        self.watch1 = Watch.objects.create(
            owner=self.user,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.wishlist_list
        )
        self.watch1 = Watch.objects.create(
            owner=self.user,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.custom_list
        )

    def test_get_user_lists_gets_correct_lists(self):
        # getting lists that user has watches in
        user_lists = get_user_lists(self.user)
        # checking the lists created above are found
        self.assertIn(self.collection_list, user_lists)
        self.assertIn(self.wishlist_list, user_lists)
        self.assertIn(self.custom_list, user_lists)
        self.assertEqual(user_lists.count(), 3)

    def test_get_user_lists_does_not_get_someone_elses_too(self):
        # create other user
        self.other_user = User.objects.create(
            username='other_user',
            password='password'
        )
        # set up a custom list for the other user
        self.other_list = WatchList.objects.create(
            list_name='other-list'
        )
        # add a watch for the other user to this list
        self.other_watch = Watch.objects.create(
            owner=self.other_user,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.other_list
        )
        # getting lists that user has watches in
        user_lists = get_user_lists(self.user)
        # check it doesn't get the other users list
        self.assertNotIn(self.other_list, user_lists)


class TestHome(TestCase):

    def setUp(self):
        # set up a user and login
        self.user = User.objects.create_user(
            username='user',
            password='password'
        )
        self.client.login(username='user', password='password')
        # set up a test movement for watch objects
        self.test_movement = WatchMovement.objects.create(
            movement_name='movement'
        )
        # set up list
        self.collection_list = WatchList.objects.create(
            friendly_name='collection'
        )
        self.wishlist_list = WatchList.objects.create(
            friendly_name='wish-list'
        )
        # create a watch
        self.watch1 = Watch.objects.create(
            owner=self.user,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.collection_list
        )
        self.watch2 = Watch.objects.create(
            owner=self.user,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.collection_list
        )
        # URL for the home view
        self.url = reverse('home')

    def test_home_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_home_view_context_data(self):
        response = self.client.get(self.url)
        # check context variables
        self.assertIn('day', response.context)
        self.assertIn('date', response.context)
        self.assertIn('moonphase', response.context)
        self.assertIn('watches', response.context)
        self.assertIn('lists', response.context)
        self.assertIn('current_list', response.context)
        # check current list name
        self.assertEqual(response.context['current_list'], 'collection')
        # check watches in queryset
        watches = response.context['watches']
        self.assertEqual(len(watches), 2)
        self.assertIn(self.watch1, watches)
        self.assertIn(self.watch2, watches)

    def test_home_view_pagination(self):
        # add more watches to test pagination
        for i in range(10):
            Watch.objects.create(
                owner=self.user,
                make='test_make',
                movement_type=self.test_movement,
                list_name=self.collection_list
            )
        # testing page 1
        response = self.client.get(self.url, {'page': 1})
        self.assertEqual(response.context['pages'].paginator.num_pages, 2)
        # testing page 2
        response_page_2 = self.client.get(self.url, {'page': 2})
        self.assertEqual(response_page_2.context['pages'].number, 2)

    def test_home_view_messages_pagination(self):
        # add more watches to test pagination
        for i in range(10):
            Watch.objects.create(
                owner=self.user,
                make='test_make',
                movement_type=self.test_movement,
                list_name=self.collection_list
            )
        response = self.client.get(self.url)
        messages = list(get_messages(response.wsgi_request))
        
        # check for pagination message
        self.assertTrue(any(
            'Switched to collection (Page 1 of 2)'
            in message.message for message in messages
        ))
    
    def test_home_view_messages_no_pagination(self):
        response = self.client.get(self.url)
        messages = list(get_messages(response.wsgi_request))

        # check for no pagination message
        self.assertTrue(any(
            'Switched to collection' in message.message for message in messages
        ))

    def test_page_not_an_integer_exception(self):
        # add more watches to test pagination
        for i in range(10):
            Watch.objects.create(
                owner=self.user,
                make='test_make',
                movement_type=self.test_movement,
                list_name=self.collection_list
            )
        # Simulate PageNotAnInteger by passing a non-integer value
        response = self.client.get(self.url, {'page': 'invalid'})
        
        # Check that the response defaults to page 1
        self.assertEqual(response.context['pages'].number, 1)

    def test_empty_page_exception(self):
        # add more watches to test pagination
        for i in range(10):
            Watch.objects.create(
                owner=self.user,
                make='test_make',
                movement_type=self.test_movement,
                list_name=self.collection_list
            )
        # simulate EmptyPage by passing an out-of-range page number
        response = self.client.get(self.url, {'page': 999})
        # Check that the response defaults to the last page
        self.assertEqual(
            response.context['pages'].number,
            response.context['pages'].paginator.num_pages
        )

    def test_home_view_access_denied_for_anonymous(self):
            # Log out user to test anonymous access
            self.client.logout()
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(
                response, f'/accounts/login?next={self.url}',
                fetch_redirect_response=False
            )


class TestManageWatch(TestCase):

    def setUp(self):
        # set up a user and login
        self.user = User.objects.create_user(
            username='user',
            password='password'
        )
        self.client.login(username='user', password='password')
        # set up a test movement for watch objects
        self.test_movement = WatchMovement.objects.create(
            movement_name='movement'
        )
        # set up list
        self.collection_list = WatchList.objects.create(
            friendly_name='collection'
        )
        self.wishlist_list = WatchList.objects.create(
            friendly_name='wish-list'
        )
        # create a watch
        self.watch1 = Watch.objects.create(
            owner=self.user,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.collection_list
        )

    def test_unauthorised_access_attempt(self):
        self.client.logout()
        url = reverse('manage_watch', kwargs={'origin': 'collection'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, f'/manage_watch/accounts/login?next={url}',
            fetch_redirect_response=False
        )

    def test_add_watch_view(self):
        response = self.client.get(
            reverse('manage_watch', kwargs={'origin': 'collection'})
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('watch_form', response.context)
        self.assertEqual(response.context['mode'], 'add')
        self.assertIsInstance(response.context['watch_form'], WatchForm)
    
    def test_edit_watch_view(self):
        response = self.client.get(reverse(
            'manage_watch', 
            kwargs={'origin': 'collection', 'watch_id': self.watch1.id}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn('watch_form', response.context)
        self.assertEqual(response.context['mode'], 'edit')
        self.assertEqual(response.context['watch'].id, self.watch1.id)

    def test_add_watch(self):
        form_data = {
            'owner': self.user.id,
            'make': 'test make',
            'movement_type': self.test_movement.id,
            'list_name': self.collection_list.id
        }
        response = self.client.post(
            reverse('manage_watch', kwargs={'origin': 'collection'}),
            data=form_data
        )
        self.assertRedirects(
            response,
            reverse('watch_list', kwargs={'list_name': 'collection'})
        )

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Added test make watch'
            in message.message for message in messages
        ))

    def test_edit_watch(self):
        form_data = {
            'owner': self.user.id,
            'make': 'new updated make', # new make
            'movement_type': self.test_movement.id,
            'list_name': self.wishlist_list.id # change list
        }
        response = self.client.post(reverse(
            'manage_watch',
            kwargs={'origin': 'collection', 'watch_id': self.watch1.id}
        ), data=form_data)
        self.assertRedirects(response, reverse(
            'watch_list',
            kwargs={'list_name': 'wish-list'}
        ))
        
        self.watch1.refresh_from_db()
        self.assertEqual(self.watch1.make, 'new updated make')
        
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            "watch edited successfully"
            in message.message for message in messages
        ))

    def test_invalid_form_data(self):
        form_data = {
            'owner': self.user.id,
            'make': '', # missing out the make as required field
            'movement_type': self.test_movement.id,
            'list_name': self.collection_list.id
        }
        response = self.client.post(
            reverse('manage_watch', kwargs={'origin': 'collection'}),
            data=form_data
        )
        self.assertEqual(response.status_code, 200)
        
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'An error occurred.'
            in message.message for message in messages
        ))


class TestPurchaseWatch(TestCase):
    
    def setUp(self):
        # set up a user and login
        self.user = User.objects.create_user(
            username='user',
            password='password'
        )
        self.client.login(username='user', password='password')
        # set up a test movement for watch objects
        self.test_movement = WatchMovement.objects.create(
            movement_name='movement'
        )
        # set up default lists
        self.collection_list = WatchList.objects.create(
            friendly_name='collection'
        )
        self.wish_list = WatchList.objects.create(
            friendly_name='wish-list'
        )
        # create a watch
        self.watch = Watch.objects.create(
            owner=self.user,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.wish_list
        )

    def test_successful_watch_purchase(self):
        # set watch as purchased
        response = self.client.post(reverse(
            'purchase', args=[self.watch.id]
        ))
        # refresh watch details
        self.watch.refresh_from_db()
        # check watch is now in collection list
        self.assertEqual(self.watch.list_name, self.collection_list)
        # check for a success message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'watch moved to Collection'
            in message.message for message in messages
        ))
        # verify the redirection
        self.assertRedirects(
            response, reverse('watch_list', args=['collection'])
        )

    def test_unsuccessful_watch_purchase(self):
        # set watch as purchased
        response = self.client.post(reverse(
            'purchase', args=[3263827]
        ))
        # check for an error message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Error occurred while moving watch to Collection'
            in message.message for message in messages
        ))
        # verify the redirection
        self.assertRedirects(
            response, reverse('watch_list', args=['collection'])
        )


class TestDeleteWatch(TestCase):

    def setUp(self):
        # set up a user and login
        self.user = User.objects.create_user(
            username='user',
            password='password'
        )
        self.client.login(username='user', password='password')
        # set up a test movement for watch objects
        self.test_movement = WatchMovement.objects.create(
            movement_name='movement'
        )
        # set up list
        self.collection_list = WatchList.objects.create(
            friendly_name='collection'
        )
        # create a watch
        self.watch = Watch.objects.create(
            owner=self.user,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.collection_list
        )

    def test_successful_watch_delete(self):
        # delete the watch
        response = self.client.post(reverse(
            'delete_watch', args=[self.watch.id]
        ))
        # confirm the watch does not exist
        with self.assertRaises(Watch.DoesNotExist):
            Watch.objects.get(id=self.watch.id)
        # check for a success message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            "watch deleted from"
            in message.message for message in messages
        ))
        # verify the redirection
        self.assertRedirects(response, '/')
    
    def test_unsuccessful_watch_delete(self):
        # delete a watch that does not exist
        response = self.client.post(reverse('delete_watch', args=[3263827]))
        # check for error message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            "Error occurred while deleting watch"
            in message.message for message in messages
        ))
        # verify the redirection
        self.assertRedirects(response, '/')

    def test_redirection_to_HTTP_referer(self):
        # set the HTTP_REFERER in the headers to test redirection
        referer_url = reverse('home')
        response = self.client.post(
            reverse('delete_watch', args=[self.watch.id]),
            HTTP_REFERER=referer_url
        )
        # check redirection to the referring URL
        self.assertRedirects(response, referer_url)


class TestStaffSettings(TestCase):

    def setUp(self):
        #create staff user
        self.staff = User.objects.create_user(
            username='staff',
            password='password',
            is_staff=True
        )
        #create standard user
        self.user = User.objects.create_user(
            username='user',
            password='password'
        )
        self.url = reverse('staff_settings')
    
    def test_staff_access(self):
        # login with staff
        self.client.login(username='staff', password='password')
        # request page
        response = self.client.get(self.url)
        # check page loads with 200 status and renders template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'watches/staff_settings.html')

    def test_non_staff_access_is_denied(self):
        # login with standard user
        self.client.login(username='user', password='password')
        # request page
        response = self.client.get(self.url)
        # check for 302 code as result of @staff_member_required
        self.assertEqual(response.status_code, 302)

    def test_no_login_access_is_denied(self):
        # request page without logging in
        response = self.client.get(self.url)
        # check for 302 code as result of @staff_member_required
        self.assertEqual(response.status_code, 302)

    def test_valid_movement_form_submission(self):
        # login with staff member
        self.client.login(username='staff', password='password')
        # create new movement name to enter
        form_data = {'movement_name': 'Perpetual Motion'}
        # submit the form with the form data
        response = self.client.post(
            self.url, data={'movement-form': 'submit', **form_data}
        )
        # check redirect staff_settings
        self.assertRedirects(response, self.url)
        # check that new movement has been created
        self.assertTrue(
            WatchMovement.objects.filter
            (movement_name='Perpetual Motion').exists()
        )
        # check for success message
        messages = list(response.wsgi_request._messages)
        self.assertIn(
            'Perpetual Motion movement created.',
            [msg.message for msg in messages]
        )

    def test_invalid_movement_form_submission(self):
        # login with staff member
        self.client.login(username='staff', password='password')
        # create invalid form data with blank movement name
        form_data = {'movement_name': ''}
        # submit the form with the form data
        response = self.client.post(
            self.url, data={'movement-form': 'submit', **form_data}
        )
        # check page is rendered okay still
        self.assertEqual(response.status_code, 200)
        # confirm that movement does not exist
        self.assertFalse(WatchMovement.objects.exists())
        # check for form validation message
        messages = list(response.wsgi_request._messages)
        self.assertTrue(
            any('This field is required.' in msg.message for msg in messages)
        )

    def test_valid_list_form_submission(self):
        # login with staff member
        self.client.login(username='staff', password='password')
        # create new list name to enter
        form_data = {'friendly_name': 'To Sell...'}
        # submit the form with the form data
        response = self.client.post(
            self.url, data={'list-form': 'submit', **form_data}
        )
        # check redirect staff_settings
        self.assertRedirects(response, self.url)
        # check that new list has been created
        self.assertTrue(
            WatchList.objects.filter(friendly_name='To Sell...').exists()
        )
        # check for success message
        messages = list(response.wsgi_request._messages)
        self.assertIn(
            'To Sell... created.', [msg.message for msg in messages]
        )

    def test_invalid_list_form_submission(self):
        # login with staff member
        self.client.login(username='staff', password='password')
        # create invalid form data with blank list name
        form_data = {'friendly_name': ''}
        # submit the form with the form data
        response = self.client.post(
            self.url, data={'list-form': 'submit', **form_data}
        )
        # check page is rendered okay still
        self.assertEqual(response.status_code, 200)
        # confirm that list does not exist
        self.assertFalse(WatchMovement.objects.exists())
        # check for form validation message
        messages = list(response.wsgi_request._messages)
        self.assertTrue(
            any('This field is required.' in msg.message for msg in messages)
        )


class TestEditMovement(TestCase):

    def setUp(self):
        #create staff user
        self.staff = User.objects.create_user(
            username='staff',
            password='password',
            is_staff=True
        )
        # login as staff user
        self.client.login(username='staff', password='password')
        # create a movment to edit
        self.test_movement = WatchMovement.objects.create(
            movement_name='test movement'
        )
        # set up list
        self.collection_list = WatchList.objects.create(
            friendly_name='collection'
        )
        # create 2 watches
        self.watch1 = Watch.objects.create(
            owner=self.staff,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.collection_list
        )
        self.watch2 = Watch.objects.create(
            owner=self.staff,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.collection_list
        )

    def test_bring_up_edit_movement_input(self):
        # request edit
        response = self.client.get(reverse(
            'edit_movement', args=[self.test_movement.id]
        ))
        # check any associated watches are mentioned
        self.assertEqual(response.context['associated'], 2)
        # check the edit_form is part of the context
        self.assertIn('edit_form', response.context)
        # check correct template is rendered
        self.assertTemplateUsed(response, 'watches/staff_settings.html')

    def test_editing_movement_valid_data(self):
        # create new name for movement
        form_data = {'movement_name': 'new updated name'}
        # submit form with new name
        response = self.client.post(
            reverse('edit_movement', args=[self.test_movement.id]),
            data=form_data
        )
        # refresh info from the db and confirm the name has been changed
        self.test_movement.refresh_from_db()
        self.assertEqual(self.test_movement.movement_name, 'new updated name')
        # confirm redirect to staff_settings
        self.assertRedirects(response, reverse('staff_settings'))
        # check for success message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            "Changes saved."
            in message.message for message in messages
        ))

    def test_editing_movement_invalid_data(self):
        # create invalid movement name
        form_data = {'movement_name': ''}
        # submit invalid form
        response = self.client.post(
            reverse('edit_movement', args=[self.test_movement.id]),
            data=form_data
        )
        # confirm redirect to staff_settings
        self.assertRedirects(response, reverse('staff_settings'))
        # check for error message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Failed to edit movement:'
            in message.message for message in messages
        ))


class TestEditList(TestCase):

    def setUp(self):
        #create staff user
        self.staff = User.objects.create_user(
            username='staff',
            password='password',
            is_staff=True
        )
        # login as staff user
        self.client.login(username='staff', password='password')
        # create a movment
        self.test_movement = WatchMovement.objects.create(
            movement_name='test movement'
        )
        # set up list to edit
        self.test_list = WatchList.objects.create(
            friendly_name='test list'
        )
        # create 2 watches
        self.watch1 = Watch.objects.create(
            owner=self.staff,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.test_list
        )
        self.watch2 = Watch.objects.create(
            owner=self.staff,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.test_list
        )

    def test_bring_up_edit_list_input(self):
        # request edit
        response = self.client.get(reverse(
            'edit_list', args=[self.test_list.id]
        ))
        # check any associated watches are mentioned
        self.assertEqual(response.context['associated'], 2)
        # check the edit_form is part of the context
        self.assertIn('edit_form', response.context)
        # check correct template is rendered
        self.assertTemplateUsed(response, 'watches/staff_settings.html')

    def test_editing_list_valid_data(self):
        # create new name for list
        form_data = {'friendly_name': 'new updated list'}
        # submit form with new name
        response = self.client.post(
            reverse('edit_list', args=[self.test_list.id]),
            data=form_data
        )
        # refresh info from the db and confirm the name has been changed
        self.test_list.refresh_from_db()
        self.assertEqual(self.test_list.friendly_name, 'new updated list')
        # confirm redirect to staff_settings
        self.assertRedirects(response, reverse('staff_settings'))
        # check for success message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            "Changes saved."
            in message.message for message in messages
        ))

    def test_editing_list_invalid_data(self):
        # create invalid list name
        form_data = {'friendly_name': ''}
        # submit invalid form
        response = self.client.post(
            reverse('edit_list', args=[self.test_list.id]),
            data=form_data
        )
        # confirm redirect to staff_settings
        self.assertRedirects(response, reverse('staff_settings'))
        # check for error message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Failed to edit list:'
            in message.message for message in messages
        ))


class TestDeleteMovement(TestCase):

    def setUp(self):
        # set up a user and login
        self.staff_user = User.objects.create_user(
            username='staff',
            password='password',
            is_staff=True
        )
        self.client.login(username='staff', password='password')
        # set up a test movement
        self.test_movement = WatchMovement.objects.create(
            movement_name='movement'
        )
        # set up list
        self.collection_list = WatchList.objects.create(
            friendly_name='collection'
        )
        # create 2 watches
        self.watch1 = Watch.objects.create(
            owner=self.staff_user,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.collection_list
        )
        self.watch2 = Watch.objects.create(
            owner=self.staff_user,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.collection_list
        )

    def test_for_affected_watches_on_movement_delete(self):
        response = self.client.get(reverse(
            'delete_movement', args=[self.test_movement.id]
        ))
        # check that the context includes the number of
        # associated watches and the movement
        self.assertEqual(response.context['associated'], 2)
        self.assertEqual(response.context['to_delete'], self.test_movement)
        # check that the correct template is used
        self.assertTemplateUsed(response, 'watches/staff_settings.html')

    def test_successful_movement_deletion(self):
        # delete the movement
        response = self.client.post(reverse(
            'delete_movement', args=[self.test_movement.id]
        ))
        # confirm movement does not exist
        with self.assertRaises(WatchMovement.DoesNotExist):
            WatchMovement.objects.get(id=self.test_movement.id)
        # check for a success message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'movement deleted'
            in message.message for message in messages
        ))
        # verify the redirection
        self.assertRedirects(response, '/staff_settings/')

    @patch('watches.models.WatchMovement.delete', side_effect=Exception(
        "Deletion failed"
    ))
    def test_delete_movement_post_failure(self, mock_delete):
        # delete the movement but simulating failure in delete method
        response = self.client.post(
            reverse('delete_movement', args=[self.test_movement.id])
        )
        # check for an error message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(
            any("Error occurred while deleting movement"
            in message.message for message in messages
        ))
        # verify the redirection to 'staff_settings'
        self.assertRedirects(response, reverse('staff_settings'))

    def test_delete_movement_access_denied_for_non_staff(self):
        # log out the staff user and log in as a regular user
        self.client.logout()
        self.client.login(username='testuser', password='password')
        # attempt to access the view
        response = self.client.get(
            reverse('delete_movement', args=[self.test_movement.id])
        )
        # verify that access is denied (302 redirect to login page)
        self.assertEqual(response.status_code, 302)


class TestDeleteList(TestCase):

    def setUp(self):
        # set up a user and login
        self.staff_user = User.objects.create_user(
            username='staff',
            password='password',
            is_staff=True
        )
        self.client.login(username='staff', password='password')
        # set up a movement
        self.test_movement = WatchMovement.objects.create(
            movement_name='movement'
        )
        # set up test list
        self.collection_list = WatchList.objects.create(
            friendly_name='collection'
        )
        # create 2 watches
        self.watch1 = Watch.objects.create(
            owner=self.staff_user,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.collection_list
        )
        self.watch2 = Watch.objects.create(
            owner=self.staff_user,
            make='test_make',
            movement_type=self.test_movement,
            list_name=self.collection_list
        )

    def test_for_affected_watches_on_list_delete(self):
        response = self.client.get(reverse(
            'delete_list', args=[self.collection_list.id]
        ))
        # check that the context includes the number of
        # associated watches and list
        self.assertEqual(response.context['associated'], 2)
        self.assertEqual(response.context['to_delete'], self.collection_list)
        # check that the correct template is used
        self.assertTemplateUsed(response, 'watches/staff_settings.html')

    def test_successful_list_deletion(self):
        # delete the list
        response = self.client.post(reverse(
            'delete_list', args=[self.collection_list.id]
        ))
        # confirm list does not exist
        with self.assertRaises(WatchList.DoesNotExist):
            WatchList.objects.get(id=self.collection_list.id)
        # check for a success message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'deleted'
            in message.message for message in messages
        ))
        # verify the redirection
        self.assertRedirects(response, '/staff_settings/')

    @patch('watches.models.WatchList.delete', side_effect=Exception(
        "Deletion failed"
    ))
    def test_delete_list_post_failure(self, mock_delete):
        # delete the list but simulating failure in delete method
        response = self.client.post(
            reverse('delete_list', args=[self.collection_list.id])
        )
        # check for an error message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(
            any('Error occurred while deleting'
            in message.message for message in messages
        ))
        # verify the redirection to 'staff_settings'
        self.assertRedirects(response, reverse('staff_settings'))

    def test_delete_list_access_denied_for_non_staff(self):
        # log out the staff user and log in as a regular user
        self.client.logout()
        self.client.login(username='testuser', password='password')
        # attempt to access the view
        response = self.client.get(
            reverse('delete_list', args=[self.collection_list.id])
        )
        # verify that access is denied (302 redirect to login page)
        self.assertEqual(response.status_code, 302)


class TestCancelProcess(TestCase):

    def setUp(self):
        # set up a user
        self.user = User.objects.create_user(
            username='user',
            password='password'
        )
        # set up a staff user
        self.user = User.objects.create_user(
            username='staff',
            password='password',
            is_staff=True
        )
        # log in as user
        self.client.login(username='user', password='password')
        # create a list
        self.test_list = WatchList.objects.create(friendly_name='test-list')
    
    def test_successful_cancel_to_existing_list(self):
        # check redirection to existing list
        response = self.client.get(reverse(
            'cancel_process',
            kwargs={'content': 'Action', 'cancel_url': 'test-list'}
        ))
        # check the redirect URL
        self.assertRedirects(
            response, reverse('watch_list', kwargs={'list_name': 'test-list'})
        )
        # check for the info message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            "Action cancelled." in message.message for message in messages
        ))
    
    def test_successful_cancel_to_cancel_url(self):
        # logout as user and login as staff for staff settings cancel_url
        self.client.logout()
        self.client.login(username='staff', password='password')
        # check redirection to existing list
        response = self.client.get(reverse(
            'cancel_process',
            kwargs={'content': 'Action', 'cancel_url': 'staff_settings'}
        ))
        # check the redirect URL
        self.assertRedirects(response, reverse('staff_settings'))
        # check for the info message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            "Action cancelled." in message.message for message in messages
        ))
    
    @patch('django.contrib.messages.info')
    def test_cancel_process_handles_exception(self, mock_messages_info):
        # Mock messages.info to raise an exception
        mock_messages_info.side_effect = Exception('Test exception during message')
        # trigger the cancel_process view
        response = self.client.get(reverse(
            'cancel_process',
            kwargs={'content': 'Action', 'cancel_url': 'test-list'}
        ))
        # verify that the exception is handled and the redirect occurs
        self.assertRedirects(
            response, reverse('watch_list', kwargs={'list_name': 'test-list'})
        )
        # check for the error message
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any(
            'Error occurred while cancelling:' in message.message
            for message in messages
        ))


class TestLeavingManage(TestCase):
    def setUp(self):
        # set up a user and login
        self.user = User.objects.create_user(
            username='user',
            password='password'
        )
        self.client.login(username='user', password='password')
        self.url = reverse('leaving_manage', kwargs={'content': 'Test Action'})

    def test_leaving_manage(self):
        # content message to pass in the URL
        content = "test thing"
        # request to leave a message with the content
        response = self.client.get(reverse('leaving_manage', args=[content]))
        # check that the response is JsonResponse
        self.assertIsInstance(response, JsonResponse)
        # check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # check the response content
        self.assertJSONEqual(
            str(response.content,
            encoding='utf8'), {'status': 'message set'}
        )
        # check that the message was set
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'{content} cancelled.')

    # patching messages.error and messages.info
    @patch('watches.views.messages.error')
    @patch('watches.views.messages.info')
    def test_leaving_manage_exception(self, mock_info, mock_error):
        # simulate and exception
        mock_info.side_effect = Exception("Simulated Exception")
        # request to leave a message with the content
        response = self.client.get(self.url)
        # check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # check the response content
        self.assertJSONEqual(response.content, {'status': 'message set'})
        # check that the error message was set
        mock_error.assert_called_once_with(
            response.wsgi_request,
            'Error occurred while cancelling: Simulated Exception'
        )
