from datetime import timedelta
from django.test import TestCase, client
from .models import Menu, Course

class GetResourcesTestCase(TestCase):
    """
    Test case for checking the extraction of data from API
    """
    def setUp(self):

        # create some menu objects
        for i in range(11):
            menu = Menu.objects.create(name="Menu {}".format(i), description="Foobar" )

    def test_resource_pagination(self):
        menus_name = ["Menu 0", "Menu 1", "Menu 2", "Menu 3", "Menu 4", "Menu 5", "Menu 6", "Menu 7", "Menu 8", "Menu 9",]

        response  = self.client.get("/menus/?page=1")
        first_page_menus = response.json()['results']
        names = []
        for item in first_page_menus:
            names.append(item['name'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(names, menus_name)

    def test_get_menus_with_courses_only(self):

        # first check what is response for all menus empty
        response = self.client.get("/menus/?not_empty=True")
        self.assertFalse(response.json()['results'])
        course = Course.objects.create(name="Foo", description="Bar", price=21.2, preparation_time=timedelta(minutes=29),)
        menu = Menu.objects.filter(name="Menu 1")
        course.cards.set(menu)
        course.save()
        response = self.client.get("/menus/?not_empty=True")
        self.assertEqual(len(response.json()['results']), 1)




