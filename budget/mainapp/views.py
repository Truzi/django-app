from django.shortcuts import render, redirect
from .models import Expense, Income
from .forms import ChartForm, ExpenseForm, IncomeForm
from .charts import generate_chart
import plotly.offline as opy
from django.core.exceptions import ObjectDoesNotExist

def index(request):
  return render(request, 'index.html')

def income(request):
  incomes = Income.objects.all()
  form = IncomeForm()
  return render(request, 'income.html', {'form': form, 'incomes': incomes})

def add_income(request):
  if request.method == 'POST':
    form = IncomeForm(request.POST)
    if form.is_valid():
      form.save()
      
      form = IncomeForm()
      return redirect('income')
  else:
    form = IncomeForm()
    return render(request, 'income.html', {'form': form})

def expenses(request):
  expenses = Expense.objects.all()
  form = ExpenseForm()
  return render(request, 'expenses.html', {'form': form, 'expenses': expenses})

def add_expense(request):
  if request.method == 'POST':
    form = ExpenseForm(request.POST)
    if form.is_valid():
      form.save()
      
      form = ExpenseForm()
      return redirect('expenses')
  else:
    form = ExpenseForm()
    return render(request, 'expenses.html', {'form': form})

def summary(request):
  form = ChartForm()
  return render(request, 'summary.html', {'form': form})
  
  
def remove_item(request):
  if request.method == 'POST':
    if 'expense' in request.POST:
      try:
        id = request.POST['expense']
        expense = Expense.objects.get(pk=request.POST['expense'])
        expense.delete()
      except Expense.DoesNotExist:
        raise ObjectDoesNotExist('There is no expense with id={id}'.format(id=id))
      return redirect('expenses')
    elif 'income' in request.POST:
      try:
        id = request.POST['income']
        income = Income.objects.get(pk=request.POST['income'])
        income.delete()
      except Income.DoesNotExist:
        raise ObjectDoesNotExist('There is no income with id={id}'.format(id=id))
      return redirect('income')
    
    else:
      redirect('')
    
  # elif request.method == 'POST':
  #   chart = generate_chart(context=request.POST)
  #   return render(request, 'summary.html', {'chart': chart})