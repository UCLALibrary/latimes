from django.db import models
from django.core.validators import validate_comma_separated_integer_list
class BoxNumb(models.Model):
	box = models.CharField(max_length=30)
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
    Negative = models.CharField(max_length=1000, db_index=True)
    Quantity = models.IntegerField(null=True)
    Photographer = models.CharField(null=True, max_length=1000, db_index=True)
    Location = models.CharField(null=True, max_length=1000, db_index=True)
    BoxNumber = models.ManyToManyField(BoxNumb)
    SubjectName = models.CharField(null=True, max_length=1000, db_index=True)
    SubjectDescription = models.CharField(null=True, max_length=10000, db_index=True)
    Month = models.IntegerField(null=True, choices=MONTHS)
    Day = models.IntegerField(null=True)
    Year = models.IntegerField(db_index=True, null=True)
    #NoDate = models.CharField(null=True, max_length=10)
    PhotoDescription = models.CharField(null=True, max_length=10000, db_index=True)
    
    @property
    def split_box(self):
    	if "," in self.BoxNumber:
    		box = self.BoxNumber.replace(" ", "")
    		return "{}".format(self.BoxNumber.split(","))
    	else:
    		return "{}".format(self.BoxNumber)
    @property
    def date(self):
        if self.Day == 88 and self.Month == 88 and self.Year == 8888:
            return "No Date Avaliable"
        if self.Day == 88 and self.Month == 88 and self.Year != 8888:
            return "{}".format(self.Year)
        if self.Day == 88 and self.Month != 88 and self.Year != 8888:
            return "{} {}".format(self.Month, self.Year)
        else:
            return "{} {}, {}".format(self.get_Month_display(), self.Day, self.Year)

   
    		
    def __str__(self):
        return self.SubjectName
    