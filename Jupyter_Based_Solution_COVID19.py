import pandas as pd
import datetime
from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib import dates as mpl_dates
import datetime
import urllib2
import numpy as np

plt.style.use('fivethirtyeight')


#import io
#import requests
#import csv

url="https://covidtracking.com/api/v1/us/daily.csv"
response = urllib2.urlopen(url)

#csv_reader = csv.DictReader(response)

df = pd.read_csv(response)

df['date'] = pd.to_datetime(df["date"],format='%Y%m%d')

df.set_index('date',inplace=True)
df['date_col'] = df.index
cols = df.columns.tolist()
#print(cols)
cols = cols[-1:] + cols[:-1]
df = df[cols] 
#print(df)
rev_df = df.loc['2020-03-12':'2020-08-19':-1]
#rev_df.plot(kind='bar', x='date_col', y='hospitalizedCurrently')
plt.figure(figsize=(14, 6))
plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
plt.gcf().autofmt_xdate()
#plt.show() 
df.plot(kind='bar', x='date_col', y='hospitalizedCurrently')
plt.show()
