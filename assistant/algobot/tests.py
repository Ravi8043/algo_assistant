from django.test import TestCase, Client
from django.urls import reverse
import json


# Create your tests here.
class AskViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/ask'  # direct path since you're not using `name='ask'` in urls
        self.headers = {'content_type': 'application/json'}

    def test_post_valid_query(self):
        data = {'query': 'What is Algorand?'}
        response = self.client.post(self.url, data=json.dumps(data), **self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('answer', response.json())

    def test_post_without_query(self):
        response = self.client.post(self.url, data=json.dumps({}), **self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('answer', response.json())  # depending on your logic

    def test_get_method_not_allowed(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

