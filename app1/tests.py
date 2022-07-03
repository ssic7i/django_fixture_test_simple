import json

from django.test import TestCase, Client
from app1.models import Goods

# Create your tests here.
class TestCaseWithFixture(TestCase):
    fixtures = ["goods.json"]

    def test_get(self):
        c = Client()
        saved_itm = Goods.objects.get(id=2)
        result = c.get('/get/2/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(saved_itm.id, result.json()['data']['id'])
        self.assertEqual(saved_itm.name, result.json()['data']['name'])

    def test_add(self):
        c = Client()
        form_data = {'good': 'test item 1', 'description': 'test description'}
        result = c.post('/add/', form_data)
        self.assertEqual(result.status_code, 200)
        goods_itm = Goods.objects.get(id=result.json()['added_object'])
        self.assertEqual(goods_itm.name, form_data['good'])

    def test_mixed(self):
        c = Client()
        form_data = {'good': 'test item mixed', 'description': 'test description mixed'}
        result = c.post('/add/', form_data)
        self.assertEqual(result.status_code, 200)
        added_id = result.json()['added_object']
        result2 = c.get(f'/get/{added_id}/')
        self.assertEqual(result2.status_code, 200)
        added_name = result2.json()['data']['name']
        self.assertEqual(added_name, form_data['good'])