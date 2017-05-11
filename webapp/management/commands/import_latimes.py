import csv
import codecs

from django.core.management.base import BaseCommand, CommandError
from webapp.models import Card


STD_GR_CSV = 'webapp/data/latimes2.csv'

class Command(BaseCommand):

    help = "Converts Goodreads data from a CSV file and loads it"

    def add_arguments(self, parser):
        parser.add_argument('csv_path', nargs='?', type=str, default=STD_GR_CSV)

    def handle(self, *args, **options):
        with open(options['csv_path'], 'r') as data:
            reader = csv.DictReader(data)
            for row in reader:
                try:
                    card = self.create_card(row)
                except:
                    from pprint import pprint
                    pprint(row)

    def create_card(self, row):
    	card = Card()
    	card.id = row['ID']
    	card.Negative = row['Negative']
    	card.Quantity = row['Quantity']
    	card.BoxNumber = row['BoxNumber']
    	card.SubjectName = row['SubjectName']
    	card.SubjectDescription = row['SubjectDescription']
    	card.Month = row['Month']
    	card.Day = row['Day']
    	card.Year = row['Year']
    	card.PhotoDescription = row['PhotoDescription']
    	card.save()