from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(menu_id=1,title="Sandwich", price=7.95, inventory=15)
        # self.assertEqual(item, "Menu: Sandwich : 7.95")
        self.assertEqual(str(item), "Sandwich : 7.95")