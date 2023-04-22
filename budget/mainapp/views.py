from django.shortcuts import render

def index(request):
  return render(request, 'index.html')

def income(request):
  return render(request, 'income.html')

def expenses(request):
  return render(request, 'expenses.html')

def summary(request):
  return render(request, 'summary.html')