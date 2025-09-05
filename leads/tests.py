from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Lead

# Create your tests here.

class LeadApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_crud_flow(self):
        # Create
        r = self.client.post('/api/leads/', {"name": "Alice", "email": "alice@example.com", "source": "website"}, format='json')
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        lid = r.data["id"]

        # List
        r = self.client.get('/api/leads/')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertTrue(len(r.data) >= 1)

        # Update
        r = self.client.patch(f'/api/leads/{lid}/', {"source": "referral"}, format='json')
        self.assertEqual(r.status_code, status.HTTP_200_OK)

        # Report
        r = self.client.get('/api/leads/metrics_by_day/')
        self.assertEqual(r.status_code, status.HTTP_200_OK)

        # Delete
        r = self.client.delete(f'/api/leads/{lid}/')
        self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)
