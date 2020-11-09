from django.urls import reverse

from rest_framework.test import APITestCase

from ..models import Board


class TestBoardList(APITestCase):
    def setUp(self):
        self.url = reverse('boards:list')

    def test_board_list(self):
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, 200)
