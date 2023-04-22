from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('income', views.income, name="income"), 
    path('expenses', views.expenses, name="expenses"),
    path('summary', views.summary, name='summary')
]
