from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from unittest.mock import patch
from .models import Watch, WatchList, WatchMovement
from .views import *


class getUserListsTests(TestCase):

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


class deleteWatchTest(TestCase):

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


class purchaseWatchTest(TestCase):
    
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


class testDeleteMovementTests(TestCase):

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

    def test_for_affected_watches(self):
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
