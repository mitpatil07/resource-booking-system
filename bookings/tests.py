from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Resource, Booking

class ResourceBookingAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass1234')
        self.token_url = reverse('token_obtain_pair')
        self.resource_url = reverse('resource_list')
        self.client = APIClient()

    def authenticate(self):
        response = self.client.post(self.token_url, {'username': 'testuser', 'password': 'pass1234'})
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])

    def test_list_resources(self):
        Resource.objects.create(name="Projector", description="HD", available_quantity=5)
        response = self.client.get(self.resource_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_resource_requires_auth(self):
        data = {'name': 'Laptop', 'description': 'i7 Dell', 'available_quantity': 2}
        response = self.client.post(self.resource_url, data)
        self.assertEqual(response.status_code, 401)  # unauthorized

    def test_create_resource_with_auth(self):
        self.authenticate()
        data = {'name': 'Laptop', 'description': 'i7 Dell', 'available_quantity': 2}
        response = self.client.post(self.resource_url, data)
        self.assertEqual(response.status_code, 201)

    def test_booking_resource(self):
        self.authenticate()
        res = Resource.objects.create(name="Mic", description="Wireless", available_quantity=5)
        book_url = reverse('book_resource')
        data = {
            'resource': res.id,
            'quantity': 2,
            'start_time': '2025-08-10T10:00:00Z',
            'end_time': '2025-08-10T12:00:00Z'
        }
        response = self.client.post(book_url, data)
        self.assertEqual(response.status_code, 201)

    def test_my_bookings(self):
        self.authenticate()
        res = Resource.objects.create(name="Table", description="Wood", available_quantity=3)
        Booking.objects.create(
            user=self.user,
            resource=res,
            quantity=1,
            start_time='2025-08-10T10:00:00Z',
            end_time='2025-08-10T11:00:00Z'
        )
        response = self.client.get(reverse('my_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
