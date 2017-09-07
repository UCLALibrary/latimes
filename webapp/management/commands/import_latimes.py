import csv
import codecs

from django.core.management.base import BaseCommand, CommandError
from webapp.models import Card, BoxNumb


STD_GR_CSV = 'webapp/data/01_LAT-Negatives_1429_Sub-Index_A_Genealogical_1977_1983-xls-csv-csv_with_box-csv.csv'

class Command(BaseCommand):

    help = "Converts Goodreads data from a CSV file and loads it"


    def handle(self, *args, **options):
        with open(STD_GR_CSV, 'r') as data:
            x = 0
            reader = csv.DictReader(data)
            for row in reader:
                try:
                    card = self.create_card(row)
                except:
                    from pprint import pprint
                    x +=1
                    pprint(row)
        print("Skipped Rows: %s"%x)
    def create_card(self, row):
        card = Card()
        try:
            if row['Negative'] is not '':
                card.Negative = row['Negative']
        except:
            pass
        try:
            if row['Quanitity'] is not '':
                card.Quanitity = row['Quantity']
        except:
            pass
        try:
            if row['BoxNumber'] is not '':
                card.BoxNumber = row['BoxNumber']
        except:
            pass
        try:
            if row['SubjectName'] is not '':
                card.SubjectName = row['SubjectName']
        except:
            pass
        try:
            if row['SubjectDescrition'] is not '':
                card.SubjectDescrition = row['SubjectDescrition']
        except:
            pass
        try:
            if row['Month'] is not '':
                card.Month = row['Month']
        except:
            pass
        try:
            if row['Day'] is not '':
                card.Day = row['Day']
        except:
            pass
        try:
            if row['Month'] is not '':
                card.Month = row['Month']
        except:
            pass
        try:
            if row['Year'] is not '':
                card.Year = row['Year']
        except:
            pass
        try:
            if row['PhotoDescription'] is not '':
                card.PhotoDescription = row['PhotoDescription']
        except:
            pass
        try:
            if row['PHOTOGRAPHER'] is not '':
                card.Photographer = row['PHOTOGRAPHER']
        except:
            pass
        try:
            if row['LOCATION'] is not '':
                card.Location = row['LOCATION']
        except:
            pass
        try:
            if row['SUBJECT'] is not '':
                card.SubjectDescription = row['SUBJECT']
        except:
            pass
        try:
            if row['Original NEG NO'] is not '':
                card.Negative = row['Original NEG NO']
        except:
            pass
        try:
            if row['DATE'] is not '' and row['DATE'] != 'UNDATED':
                date = row['DATE'].split('-')
                card.Year = "19%s"%date[0]
                card.Month = date[1]
                card.Day = date[2]
            elif row['DATE'] == 'UNDATED':
                card.Year = 8888
                card.Month = 88
                card.Day = 88
        except:
            pass
        try:
            if row['Box'] is not '':
                if "," in row['Box']:
                    boxes = row['Box'].split(",")
                    for box in boxes:
                        card.save()
                        box = box.replace(" ", "")
                        BOX = BoxNumb()
                        BOX.box = box
                        BOX.save()
                        card.BoxNumber.add(BOX)
                        card.save()
                else:
                    BOX = BoxNumb()
                    BOX.box = row['Box']
                    BOX.save()
                    card.save()
                    card.BoxNumber.add(BOX)
                    card.save()
        except:
            pass
        try:
            if row['NAME/ SUBJECT INDEX'] is not '':
                card.SubjectDescription = row['NAME/ SUBJECT INDEX']
        except:
            pass
        try:
            if row['NAME / SUBJECT INDEX'] is not '':
                card.SubjectDescription = row['NAME / SUBJECT INDEX']
        except:
            pass
        try:
            if row['NAME /SUBJECT INDEX'] is not '':
                card.SubjectDescription = row['NAME /SUBJECT INDEX']
        except:
            pass
        card.save()