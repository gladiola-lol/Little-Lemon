from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(title="Ice Cream", price=5, inventory=10)
        Menu.objects.create(title="Pizza", price=10, inventory=20)
        Menu.objects.create(title="Pasta", price=8, inventory=15)

    def test_getall(self):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        self.assertEqual(len(serializer.data), 3)
        self.assertEqual(serializer.data[0]['title'], "Ice Cream")
