from django.test import TestCase
from django.contrib.auth.models import User
from unittest.mock import patch, MagicMock
from .models import Watch, WatchMovement, WatchList


class TestWatchList(TestCase):

    def test_list_return_string(self):
        test_list = WatchList.objects.create(friendly_name='Wish List')
        self.assertEqual(str(test_list), 'Wish List')


class TestWatchMovement(TestCase):

    def test_movement_return_string(self):
        test_movement = WatchMovement.objects.create(movement_name='Quartz')
        self.assertEqual(str(test_movement), 'Quartz')


class TestWatch(TestCase):

    def setUp(self):
        # setting up test user, movement and list options
        self.test_list = WatchList.objects.create(list_name='Collection')
        self.test_movement = WatchMovement.objects.create(
            movement_name='Quartz'
        )
        self.user = User.objects.create_user(
            username='testuser', password='password123'
        )

    def test_just_watch_make_return(self):
        self.test_watch = Watch.objects.create(
            owner=self.user,
            make='Seiko',
            movement_type=self.test_movement,
            list_name=self.test_list
        )
        self.assertEqual(str(self.test_watch), 'Seiko')

    def test_watch_make_and_collection_return(self):
        self.test_watch = Watch.objects.create(
            owner=self.user,
            make='Seiko',
            collection='Prospex',
            movement_type=self.test_movement,
            list_name=self.test_list
        )
        self.assertEqual(str(self.test_watch), 'Seiko Prospex')

    def test_watch_make_and_model_return(self):
        self.test_watch = Watch.objects.create(
            owner=self.user,
            make='Seiko',
            model='Speedtimer',
            movement_type=self.test_movement,
            list_name=self.test_list
        )
        self.assertEqual(str(self.test_watch), 'Seiko Speedtimer')

    def test_watch_make_and_collection_and_model_return(self):
        self.test_watch = Watch.objects.create(
            owner=self.user,
            make='Seiko',
            collection='Prospex',
            model='Speedtimer',
            movement_type=self.test_movement,
            list_name=self.test_list
        )
        self.assertEqual(str(self.test_watch), 'Seiko Prospex Speedtimer')

    @patch('cloudinary.uploader.destroy')
    def test_delete_with_image(self, mock_destroy):
        watch = Watch.objects.create(
            owner=self.user,
            movement_type=self.test_movement,
            list_name=self.test_list,
            make="Seiko",
            collection="Prospex",
            model="Speedtimer",
            image='wot/3263827.jpg'
        )

        mock_image = MagicMock()
        mock_image.public_id = 'sample_public_id'
        watch.image = mock_image

        watch.delete()
        mock_destroy.assert_called_once_with('sample_public_id')

    @patch('cloudinary.uploader.destroy')
    def test_delete_with_placeholder_image(self, mock_destroy):
        watch = Watch.objects.create(
            owner=self.user,
            movement_type=self.test_movement,
            list_name=self.test_list,
            make="Seiko",
            collection="Prospex",
            model="Speedtimer",
            image='placeholder'
        )

        watch.delete()
        mock_destroy.assert_not_called()

    @patch('watches.models.cloudinary_url')
    def test_get_optimized_image_url(self, mock_cloudinary_url):
        mock_cloudinary_url.return_value = (
            'https://res.cloudinary.com/demo/image/upload/'
            'c_fill,h_400,w_400/q_auto:eco/f_auto/your_image.jpg',
        )

        watch = Watch.objects.create(
            owner=self.user,
            movement_type=self.test_movement,
            list_name=self.test_list,
            make="Rolex",
            collection="Submariner",
            model="116610LN",
            image='watches/116610LN.jpg'
        )

        mock_image = MagicMock()
        mock_image.public_id = 'your_image'
        watch.image = mock_image

        optimized_url = watch.get_optimized_image_url()

        mock_cloudinary_url.assert_called_once_with(
            'your_image',  # public_id
            secure=True,
            fetch_format='auto',
            quality='auto:eco',
            width=400,
            height=400,
            crop='fill'
        )

        self.assertEqual(
            optimized_url,
            'https://res.cloudinary.com/demo/image/upload/'
            'c_fill,h_400,w_400/q_auto:eco/f_auto/your_image.jpg'
        )
