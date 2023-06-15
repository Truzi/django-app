import plotly.graph_objs as go
import plotly.offline as opy
from django.db.models import Sum
from random import randint as rand

from .models import Category, Expense, Income

def generate_chart(start_date, end_date):
  income_transactions = Income.objects.filter(
    date__gte=start_date,
    date__lte=end_date
  )

  categories = [item['category'] for item in Expense.objects.values('category').distinct()]
  expense_transactions = Expense.objects.filter(
    date__gte=start_date,
    date__lte=end_date,
    category__in=categories
  ).values('category').annotate(total_amount=Sum('amount'))

  total_income = sum(transaction.amount for transaction in income_transactions)

  data = [
    go.Bar(x=['Income'], y=[total_income], name='Income',
    hovertext=f'Income - {str(total_income)}', hoverinfo='text'),
  ]

  for item in expense_transactions:
    category_name = Category.objects.get(pk=item['category']).name
    amount = item['total_amount']
    marker_color = f'rgba({rand(0, 255)}, {rand(0, 255)}, {rand(0, 255)}, 1)'
    data.append(
      go.Bar(x=['Expense'], y=[amount], name=category_name,
        hovertext=f'{category_name} - {amount}' , hoverinfo='text',
        marker=dict(color=marker_color,
        line=dict(color='rgba(55, 128, 161, 1.0)', width=1)))
    )

  layout = go.Layout(title=dict(text='Incomes vs Expenses', x=0.5), yaxis=dict(title='Amount'), barmode='stack')
  chart = opy.plot({'data': data, 'layout': layout}, auto_open=False, output_type='div')

  return chart