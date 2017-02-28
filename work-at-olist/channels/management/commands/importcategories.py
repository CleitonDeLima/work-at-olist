import csv

from django.core.management.base import BaseCommand
from django.db import transaction

from channels.models import Channel, Category


class Command(BaseCommand):
    final_file = ':'
    column_category = 'Category'

    def add_arguments(self, parser):
        parser.add_argument('channel_name', help='Channel name')
        parser.add_argument('categories_csv', help='File csv to import categories')

    def handle(self, *args, **options):
        channel_name, categories_file = options.get('channel_name'), options.get('categories_csv')

        channel, created = Channel.objects.get_or_create(name=channel_name)
        if created:
            self.stdout.write(self.style.SUCCESS(f'Channel {channel.name} created.'))

        channel.categories.all().delete()

        with open(categories_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[self.column_category].strip() == self.final_file:
                    break

                categories = (category.strip() for category in
                              row[self.column_category].split('/'))

                parent = None
                with transaction.atomic():
                    with Category.objects.disable_mptt_updates():
                        for category in categories:
                            obj, created = channel.categories.get_or_create(
                                name=category, parent=parent)

                            if created:
                                self.stdout.write(self.style.SUCCESS(f'Category {obj.name} created.'))

                            parent = obj
                    Category.objects.rebuild()

        self.stdout.write(self.style.SUCCESS(f'Total: {channel.categories.count()}'))
