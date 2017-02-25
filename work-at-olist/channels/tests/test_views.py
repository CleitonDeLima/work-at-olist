import uuid

from django.shortcuts import resolve_url
from rest_framework.test import APITestCase

from channels.models import Channel, Category


class ChannelApiTest(APITestCase):
    def setUp(self):
        self.channel = Channel.objects.create(name='market')

    def test_list(self):
        url = resolve_url('channel-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        url = resolve_url('channel-detail', pk=self.channel.uuid)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_not_found(self):
        url = resolve_url('channel-detail', pk=uuid.uuid4())
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class CategoryApiTest(APITestCase):
    def setUp(self):
        channel = Channel.objects.create(name='market')
        self.category = Category.objects.create(
            name='book', channel=channel
        )
        self.category2 = Category.objects.create(
            name='book slim', channel=channel, parent=self.category
        )

    def test_list(self):
        url = resolve_url('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        url = resolve_url('category-detail', pk=self.category.pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_not_found(self):
        url = resolve_url('category-detail', pk=uuid.uuid4())
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_get_subcategory_detail(self):
        url = resolve_url('category-detail', pk=self.category2.pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
