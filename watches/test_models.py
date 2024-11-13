from django.test import TestCase
from django.contrib.auth.models import User
from .models import Watch, WatchMovement, WatchList

class TestWatchList(TestCase):

    def testListReturnString(self):
        test_list = WatchList.objects.create(friendly_name='Wish List')
        self.assertEqual(str(test_list), 'Wish List')

class TestWatchMovement(TestCase):

    def testMovementReturnString(self):
        test_movement = WatchMovement.objects.create(movement_name='Quartz')
        self.assertEqual(str(test_movement), 'Quartz')

class TestWatch(TestCase):

    def setUp(self):
        # setting up test watch with movement and list options
        self.test_list = WatchList.objects.create(list_name='Collection')
        self.test_movement = WatchMovement.objects.create(
            movement_name='Quartz'
        )
        self.user = User.objects.create_user(
            username='testuser', password='password123'
        )

    def testJustWatchMakeReturn(self):
        self.test_watch = Watch.objects.create(
            owner=self.user,
            make='Seiko',
            movement_type=self.test_movement,
            list_name=self.test_list
        )
        self.assertEqual(str(self.test_watch), 'Seiko')
    
    def testWatchMakeAndCollectionReturn(self):
        self.test_watch = Watch.objects.create(
            owner=self.user,
            make='Seiko',
            collection='Prospex',
            movement_type=self.test_movement,
            list_name=self.test_list
        )
        self.assertEqual(str(self.test_watch), 'Seiko Prospex')

    def testWatchMakeAndModelReturn(self):
        self.test_watch = Watch.objects.create(
            owner=self.user,
            make='Seiko',
            model='Speedtimer',
            movement_type=self.test_movement,
            list_name=self.test_list
        )
        self.assertEqual(str(self.test_watch), 'Seiko Speedtimer')
    
    def testWatchMakeAndCollectionAndModelReturn(self):
        self.test_watch = Watch.objects.create(
            owner=self.user,
            make='Seiko',
            collection='Prospex',
            model='Speedtimer',
            movement_type=self.test_movement,
            list_name=self.test_list
        )
        self.assertEqual(str(self.test_watch), 'Seiko Prospex Speedtimer')
