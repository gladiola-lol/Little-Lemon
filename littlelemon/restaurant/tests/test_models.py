from django.test import TestCase
from restaurant.models import Menu, MenuItem

# TestCase class


class MenuTests(TestCase):
    def test_menu_str(self):
        item = Menu.objects.create(
            title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
