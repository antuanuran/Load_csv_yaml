import csv
import os.path
from app.service import import_data_all


from django.core.management import BaseCommand



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("path")

    def handle(self, path, *args, **options):
        format_data = os.path.splitext(os.path.basename(path))[1][1:]
        print(format_data)
        with open(path, "r") as file:
            import_data_all(file, format_data)




