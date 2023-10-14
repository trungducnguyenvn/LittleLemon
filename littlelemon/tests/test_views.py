from django.test import TestCase
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='Pizza', price=20, inventory=100, menu_id=4)

    def test_getall(self):
        response = self.client.get('/api/menu/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

