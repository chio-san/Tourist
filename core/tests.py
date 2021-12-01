from django.test import TestCase
from django.urls import reverse
from django.db.models import QuerySet
from places.models import Place
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class SeleniumTest(TestCase):
    def test_one(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000/")
        elem = driver.find_element_by_link_text('')
        sleep(5)
      
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source
        driver.close()


class PlacesListTestCase(TestCase):
    def test_open_list_success(self):
        url = reverse('places-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('places'), QuerySet)



class PlaceCreateTestCase(TestCase):
    def test_create_place_success(self):
        url = reverse('create-place')
        data = {
            'name': 'Issyk-kul',
            'location': 'Kara-Kol region',
            'description': 'Lake in KG'
        }
        response = self.client.post(url, data)
        place = Place.objects.last()
        self.assertEqual(place.name, 'Issyk-kul')