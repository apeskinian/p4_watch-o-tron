from django.test import TestCase
from django.urls import reverse, resolve
from watches import views

class TestUrls(TestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)

    def test_watch_list_url_resolves(self):
        url = reverse('watch_list', kwargs={'list_name': 'collection'})
        self.assertEqual(resolve(url).func, views.home)

    def test_cancel_process_url_resolves(self):
        url = reverse(
            'cancel_process',
            kwargs={'content': 'Logout', 'cancel_url': 'home'}
        )
        self.assertEqual(resolve(url).func, views.cancel_process)

    def test_delete_list_url_resolves(self):
        url = reverse('delete_list', kwargs={'list_id': 1})
        self.assertEqual(resolve(url).func, views.delete_list)

    def test_delete_movement_url_resolves(self):
        url = reverse('delete_movement', kwargs={'movement_id': 1})
        self.assertEqual(resolve(url).func, views.delete_movement)

    def test_delete_watch_url_resolves(self):
        url = reverse('delete_watch', kwargs={'watch_id': 1})
        self.assertEqual(resolve(url).func, views.delete_watch)

    def test_edit_list_url_resolves(self):
        url = reverse('edit_list', kwargs={'list_id': 1})
        self.assertEqual(resolve(url).func, views.edit_list)

    def test_edit_movement_url_resolves(self):
        url = reverse('edit_movement', kwargs={'movement_id': 1})
        self.assertEqual(resolve(url).func, views.edit_movement)

    def test_leaving_manage_url_resolves(self):
        url = reverse('leaving_manage', kwargs={'content': 'Manage Watch'})
        self.assertEqual(resolve(url).func, views.leaving_manage)

    def test_manage_watch_url_resolves(self):
        # test without watch_id
        url = reverse('manage_watch', kwargs={'origin': 'list'})
        self.assertEqual(resolve(url).func, views.manage_watch)

        # test with watch_id
        url = reverse('manage_watch', kwargs={'origin': 'list', 'watch_id': 1})
        self.assertEqual(resolve(url).func, views.manage_watch)

    def test_purchase_watch_url_resolves(self):
        url = reverse('purchase', kwargs={'watch_id': 1})
        self.assertEqual(resolve(url).func, views.purchase_watch)

    def test_staff_settings_url_resolves(self):
        url = reverse('staff_settings')
        self.assertEqual(resolve(url).func, views.staff_settings)