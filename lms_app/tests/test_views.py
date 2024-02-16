# test_views.py
import json

from django.test import TestCase, Client
from django.urls import reverse
from lms_app.models import TestModel


class TestApiViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        TestModel.objects.all().delete()

    def test_post(self):
        response = self.client.post(reverse('test_api'))
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        response = self.client.get(reverse('test_api'))
        self.assertEqual(response.status_code, 200)


class TestApiEndpoints(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        with open('dj_test_app/tests/testing.json', 'r') as f:
            cls.test_data = json.load(f)

    def test_event_endpoints(self):
        for event in self.test_data:
            data = {
                'book_id': event['book_id'],
                'member_id': event.get('member_id'),
                'date': event['date'],
                'eventtype': event['eventtype'],
            }

            response = self.client.post(reverse('handle_event'), data=data)

            self.assertEqual(response.status_code, 200)