import csv
import os

from django.core.management.base import BaseCommand

from lms_app.models import Books, Members


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(os.path.join(os.path.dirname(__file__), 'books.csv'), 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                Books.objects.create(
                    id=int(row['book_id']),
                    total_copies=int(row['no_of_copies']),
                    available_copies=int(row['no_of_copies']),
                    book_name=row['book_name']
                )

        with open(os.path.join(os.path.dirname(__file__), 'members.csv'), 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                Members.objects.create(
                    id=int(row['member_id']),
                    name=row['member_name']
                )