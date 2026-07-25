from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.IntegerField()



# Dunder methods (short for "double underscore" methods), also known as magic methods, are special built-in Python functions that start and end with two underscores
    def __str__(self):
        return self.company_name

# Returns a precise, developer-friendly string representation