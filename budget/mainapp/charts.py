import matplotlib.pyplot as plt
from .models import Income
from io import BytesIO
import base64

def income_chart(request):
  colors = ['blue']
  plt.rcParams['axes.prop_cycle'] = plt.cycler(color=colors)
  
  incomes = Income.objects.all()

  dates = [income.date for income in incomes]
  amounts = [income.amount for income in incomes]

  plt.plot(dates, amounts)
  plt.title('Income over time')
  plt.xlabel('Date')
  plt.ylabel('Amount')

  buffer = BytesIO()
  plt.savefig(buffer, format='png')
  buffer.seek(0)
  image_png = buffer.getvalue()
  buffer.close()
  return base64.b64encode(image_png).decode('utf-8')