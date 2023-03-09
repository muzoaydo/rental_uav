from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import UAV
from .serializers import UAVSerializer

class UAVTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.uav1 = UAV.objects.create(
            brand='DJI',
            model='Mavic Air 2',
            weight=0.57,
            category='Consumer',
            rented=False
        )
        self.uav2 = UAV.objects.create(
            brand='DJI',
            model='Phantom 4 Pro',
            weight=1.39,
            category='Professional',
            rented=True
        )

    def test_uav_model_str(self):
        self.assertEqual(str(self.uav1), 'DJI Mavic Air 2')

    def test_uav_listing(self):
        response = self.client.get(reverse('uav_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.uav1.brand)
        self.assertContains(response, self.uav1.model)
        self.assertContains(response, self.uav2.brand)
        self.assertContains(response, self.uav2.model)



