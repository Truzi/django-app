from django import forms
from .models import Expense, Income

class IncomeForm(forms.ModelForm):
  class Meta:
    model = Income
    fields = ['amount', 'description', 'date']

class ExpenseForm(forms.ModelForm):
  class Meta:
    model = Expense
    fields = ['amount', 'description', 'category', 'date']
    
class ChartForm(forms.Form):
  start_date = forms.DateField(label = "Start Date")
  end_date = forms.DateField(label = "End Date")