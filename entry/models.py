from django.db import models

# Create your models here.
class Student(models.Model):
    
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=False)
    address = models.CharField(max_length=100, blank=False)
    grade = models.CharField(max_length=1, blank=False)
    major = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return f"{self.name} has {self.grade} as major {self.major}"
    