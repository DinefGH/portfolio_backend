from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Visit, VisitCount

class IncrementVisitTest(TestCase):
    def setUp(self):
        # Initialize the API client for making requests
        self.client = APIClient()
        self.url = reverse('increment_visit')  # URL for the increment_visit endpoint

    def test_increment_visit_creates_new_visit(self):
        """
        Test that a new Visit instance is created each time
        the increment_visit endpoint is called.
        """
        # Ensure there are no Visit instances initially
        self.assertEqual(Visit.objects.count(), 0)

        # Call the increment_visit endpoint
        response = self.client.post(self.url)

        # Check if a Visit instance was created
        self.assertEqual(Visit.objects.count(), 1)

        # Check if VisitCount instance was created or updated
        visit_count = VisitCount.objects.get(pk=1)
        self.assertEqual(visit_count.count, 1)

        # Verify the response status and message
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Visit count incremented')

    def test_increment_visit_response_data(self):
        """
        Test that the response data includes the updated visit count and the visit timestamp.
        """
        # Make an initial request to create a Visit instance and VisitCount instance
        response = self.client.post(self.url)
        
        # Check if the response contains 'count' and 'visit_timestamp' fields
        self.assertIn('count', response.data)
        self.assertIn('visit_timestamp', response.data)

        # Validate that the 'count' field in the response matches the VisitCount model's count
        visit_count = VisitCount.objects.get(pk=1)
        self.assertEqual(response.data['count'], visit_count.count)

        # Ensure the timestamp is formatted correctly
        timestamp = response.data['visit_timestamp']
        self.assertIsInstance(timestamp, str)  # Check it's returned as a string (ISO format)

    def test_multiple_visits_increment_count_correctly(self):
        """
        Test that each call to the increment_visit endpoint correctly increments the visit count.
        """
        # Call the increment_visit endpoint multiple times
        for _ in range(5):
            self.client.post(self.url)

        # Verify that the count in VisitCount is incremented to 5
        visit_count = VisitCount.objects.get(pk=1)
        self.assertEqual(visit_count.count, 5)