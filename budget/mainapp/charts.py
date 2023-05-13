import plotly.graph_objs as go
import plotly.offline as opy
from django.db.models import Sum
from datetime import datetime, timedelta

from .models import Income, Expense

def generate_chart():
  # Get the start and end dates for the chart
  end_date = datetime.today().date()
  start_date = end_date - timedelta(days=30)

  income_transactions = Income.objects.filter(
      date__gte=start_date,
      date__lte=end_date
  )
  expense_transactions = Expense.objects.filter(
      date__gte=start_date,
      date__lte=end_date
  )

  # Calculate the total income amount
  total_income = sum(transaction.amount for transaction in income_transactions)

  # Create a dictionary of expense categories and their total amounts
  total_expense = sum(transaction.amount for transaction in expense_transactions)

  # Create the Plotly chart
  data = [
      go.Bar(x=['Income', 'Expense'], y=[total_income, total_expense])
  ]
  layout = go.Layout(title=dict(text='Income vs Expense', x=0.5), yaxis=dict(title='Amount'))
  chart = opy.plot({'data': data, 'layout': layout}, auto_open=False, output_type='div')

  return chart