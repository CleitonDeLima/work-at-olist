import os

from django.test import TestCase
from django.utils.six import StringIO
from django.core.management import call_command

from channels.models import Channel


class ImportCategoriesTest(TestCase):
    def setUp(self):
        self.out = StringIO()
        call_command(
            'importcategories',
            'marketplace',
            os.path.abspath('channels/tests/fixtures/categories.csv'),
            stdout=self.out
        )

    def test_channel_created(self):
        self.assertEqual(Channel.objects.count(), 1)

    def test_categories_created(self):
        self.assertEqual(
            Channel.objects.get(name='marketplace').categories.count(),
            23)

    def test_stdout(self):
        self.assertIn('Total: 23', self.out.getvalue())
