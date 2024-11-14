from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
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
        # set up default lists
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


