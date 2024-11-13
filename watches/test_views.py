from django.test import TestCase

class TestViews(TestCase):

    def test_get_login_page(self):
        response = self.client.get('/')