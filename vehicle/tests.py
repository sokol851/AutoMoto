from rest_framework import status

from rest_framework.test import APITestCase, APIClient

from users.models import User
from vehicle.models import Car


class VehicleTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(username='admin')
        self.client.force_authenticate(user=self.user)

    def test_create_car(self):
        """ Тестирование создания машины """
        data = {
            'title': 'test',
            'description': 'Test'
        }

        response = self.client.post(
            '/cars/',
            data=data
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'milage': [], 'title': 'test', 'description': 'Test', 'owner': None}
        )

        self.assertTrue(
            Car.objects.all().exists()
        )

    def test_list_car(self):
        """ Тестирование списка машин """

        Car.objects.create(
            title='list test',
            description='list test'
        )

        response = self.client.get(
            '/cars/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': 2, 'milage': [], 'title': 'list test', 'description': 'list test', 'owner': None}]
        )
