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

    # Group the expense transactions by category and calculate the total amount for each category
    expense_by_category = expense_transactions.values('category__name').annotate(total_amount=Sum('amount'))

    # Create the Plotly chart
    data = [
        go.Bar(x=['Income'], y=[total_income], name="Income")
    ]
    for expense in expense_by_category:
        data.append(
            go.Bar(x=['Expenses'], y=[expense['total_amount']], name=expense['category__name'])
        )

    layout = go.Layout(title=dict(text='Income vs Expense by Category', x=0.5), yaxis=dict(title='Amount'))
    chart = opy.plot({'data': data, 'layout': layout}, auto_open=False, output_type='div')
    print(data)
    return chart
