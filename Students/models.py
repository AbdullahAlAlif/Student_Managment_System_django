from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Students(models.Model):
    Student_id = models.PositiveIntegerField()
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    email = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    gpa = models.FloatField(validators=[MaxValueValidator(4.00)]) #Since CGPA or SGPA normally maximum 4.00 thus added a max value constraint

    def __str__(self):
        return f"Student ID: {self.Student_id}, Name: {self.first_name} {self.last_name}, Department: {self.Department}, GPA: {self.gpa:.2f}"