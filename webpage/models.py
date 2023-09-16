from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self)->str:
        return self.name


class Subject(models.Model):
    
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=128)
    credit = models.IntegerField()
    term = models.IntegerField(choices=((1, 1),(2,2)))
    year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self)->str:
        return self.name
