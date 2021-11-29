from django.test import TestCase
from django.urls import reverse
from django.db.models import QuerySet
from places.models import Place


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