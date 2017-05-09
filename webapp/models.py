from django.db import models

class Card(models.Model):
    MONTHS = (
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December")
    )
    
    #ID = models.IntegerField()
    Negative = models.IntegerField()
    Quantity = models.IntegerField()
    BoxNumber = models.IntegerField()
    SubjectName = models.CharField(null=True, max_length=1000)
    SubjectDescription = models.CharField(null=True, max_length=10000)
    Month = models.IntegerField(choices=MONTHS)
    Day = models.IntegerField()
    Year = models.IntegerField()
    NoDate = models.CharField(null=True, max_length=10)
    PhotoDescription = models.CharField(null=True, max_length=10000)
    