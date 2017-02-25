from django.test import TestCase

from ..models import Channel, Category


class ChannelModelTest(TestCase):
    def setUp(self):
        self.channel = Channel.objects.create(name='market')

    def test_create(self):
        self.assertTrue(Channel.objects.exists())

    def test_str(self):
        self.assertTrue(str(self.channel), 'market')


class CategoryModelTest(TestCase):
    def setUp(self):
        channel = Channel.objects.create(name='market')
        self.category = Category.objects.create(name='book', channel=channel)

    def test_create(self):
        self.assertTrue(Category.objects.exists())

    def test_str(self):
        self.assertTrue(str(self.category), 'book')
