from django.db import models
from datetime import date

class Category(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self) -> str:
    return self.name

class Income(models.Model):
  amount = models.FloatField()
  date = models.DateField()
  description = models.CharField(max_length=100)

  def __str__(self) -> str:
    return f'{self.amount}$ for {self.description}'
  
  def formatted_date(self):
    return self.my_date.strftime("%Y-%m-%d")
  
class Expense(models.Model):
  amount = models.FloatField()
  date = models.DateField()
  description = models.CharField(max_length=100)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f'{self.amount}$ for {self.description}'
  
  def formatted_date(self):
    return self.my_date.strftime("%Y-%m-%d")