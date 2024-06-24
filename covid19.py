import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from matplotlib.ticker import FuncFormatter
import seaborn as sns
csv_reader = pd.read_csv('Covid19_updated.csv')
csv_reader['Date'] = pd.to_datetime(csv_reader['Date'])
csv_reader.sort_values('Date', inplace=True)
date = csv_reader['Date']
UScase = csv_reader['Case_US']
Brazilcase = csv_reader['Case_Brazil']
Indiacase = csv_reader['Case_India']
Germanycase = csv_reader['Case_Germany']
Francecase = csv_reader['Case_France']

def millions(x, pos):
   return '%1.0fM' % (x * 1e-6)
formatter = FuncFormatter(millions)
fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)
each_month_locator = mpl_dates.MonthLocator(interval=1)
year_month_formatter = mpl_dates.DateFormatter('%m-%Y')

ax.xaxis.set_major_locator(each_month_locator)
ax.xaxis.set_major_formatter(year_month_formatter)


plt.plot(date, UScase, linestyle = 'solid', label = 'USA')
plt.plot(date, Brazilcase, linestyle = 'solid', label = 'Brazil')
plt.plot(date, Indiacase, linestyle = 'solid', label = 'India')
plt.plot(date, Germanycase, linestyle = 'solid', label = 'Germany')
plt.plot(date, Francecase, linestyle = 'solid', label = 'France')
plt.gcf().autofmt_xdate()

plt.title('COVID-19 Confirmed Cases Over Time (2022)')
plt.ylabel('Confirm Cases')
plt.legend()
plt.show()
