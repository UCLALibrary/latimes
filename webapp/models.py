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
    Negative = models.IntegerField(db_index=True)
    Quantity = models.IntegerField()
    BoxNumber = models.IntegerField(db_index=True)
    SubjectName = models.CharField(null=True, max_length=1000, db_index=True)
    SubjectDescription = models.CharField(null=True, max_length=10000, db_index=True)
    Month = models.IntegerField(choices=MONTHS)
    Day = models.IntegerField()
    Year = models.IntegerField(db_index=True)
    #NoDate = models.CharField(null=True, max_length=10)
    PhotoDescription = models.CharField(null=True, max_length=10000, db_index=True)
    
    @property
    def date(self):
        if self.Day == 88:
            return "No Date Avaliable"
        else:
            return "{} {}, {}".format(self.get_Month_display(), self.Day, self.Year)

    def __str__(self):
        return self.SubjectName