from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('income', views.income, name="income"),
    path('expenses', views.expenses, name="expenses"),
    path('summary', views.summary, name='summary'),
    
    path('add_income', views.add_income, name="add_income"),
    path('add_expense', views.add_expense, name="add_expense"),
    path('remove_item', views.remove_item, name="remove_item")
]
