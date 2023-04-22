from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=30)

class Income(models.Model):
  amount = models.FloatField()
  date = models.DateField()
  description = models.CharField(max_length=100)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  
class Expense(models.Model):
  amount = models.FloatField()
  date = models.DateField()
  description = models.CharField(max_length=100)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)