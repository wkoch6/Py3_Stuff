#new comment
import csv
from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib import dates as mpl_dates
import numpy as np
import datetime
import io
import requests
import urllib.request
import pandas

roll_5 = []
date_x = []
dev_x = []
dev_y = []
num_tests = []
cur_hosp = []
death_increase = []
percent_positive = []
#my_date = ''
#year = 0
#month = ''
#day = ''
my_temp_date = ''
plt.style.use('fivethirtyeight')
#plt.style.use('seaborn')
#plt.style.use('ggplot')
#plt.xkcd()
#print"dev_x is of type: ",(type(dev_x))

#url="https://covidtracking.com/api/v1/us/daily.csv"
#response = urllib.request.urlopen(url)
df = pandas.read_csv("https://covidtracking.com/api/v1/us/daily.csv")
#lines = [l.decode('utf-8') for l in response.readlines()]
#csv_reader = csv.reader(lines)


#with open('C:\Users\C40630\Downloads\daily - 2020-07-12T182102.105.csv', 'r') as csv_file:
#csv_reader = csv.DictReader(response) # the entire csv file is read into "csv_reader"
#print("'date', 'num_increase'")

for row in df:
    #print("line is of type: ",type(line))
    print(row)
    #print("my date is: ", my_date)
    #print("my_temp_date is type: ",type(my_temp_date))
    #print("year = ", year)
    #print("month = ", month)
    #print("day = ", day)
    #print(pos_incr)
    #print(tot_tests)
    # my_percent = float(pos_incr)/float(tot_tests)
    #print(my_percent*100)
    # num_tests.append(int(line['totalTestResultsIncrease']))
    # cur_hosp.append(int(line['hospitalizedCurrently']))
    # death_increase.append(int(line['deathIncrease']))
    # percent_positive.append((float(line['positiveIncrease'])/float(line['totalTestResultsIncrease']))*100)
    #print("line[date] is of type",type(line['date']))
    #print("line[date] is of type",type(int((line['date']))))
    #print(line['date'],line['positiveIncrease'])
    #print("line is of type: ",type(line))
    #if len(date_x) >= 5:
        # #print"x is greater than or equal to 5"
        # #print("date_x length is: ",len(date_x))
        # #print("date is: ", my_date)
        # #print(dev_y[len(date_x)-1])
        # #print(dev_y[len(date_x)-5])
        # #print("date_x -5 is: ",date_x[len(date_x)-5])
        # #temp_sum is the sum of the last 5 days 
        # temp_sum = sum(dev_y[len(date_x)-5:len(date_x)])
        # #print(temp_sum)
        # #print(temp_sum/5)
        # roll_5.append(temp_sum/5)
        # #print(dev_y[len(date_x)-5:len(date_x)])
        #break
    # if int(line['date']) <= 20200320:
    #     print("March 20 found -- break here")
    #     break

#print("date_x is of type: ",type(date_x))

# plt.figure(figsize=(14, 6)) # The size of the figure is specified as (width, height) in inches
# #print("printing dev_x",dev_x)
# #print("printing dev_y",dev_y)
# plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
# plt.gcf().autofmt_xdate()
# date_for_print = (date_x[0].strftime("%Y_%m_%d"))
# plt.title(date_for_print + '  US Covid-19 positives vs Date')
# plt.xlabel('Date')
# plt.ylabel('US Covid-19 positives')
# #plt.plot(date_x,dev_y,linestyle='solid',label='Positives')
# plt.bar(date_x,dev_y,label='Positives')
# #plt.tight_layout()
# plt.legend()
# #plt.gca().spines['right'].set_visible(True)
# #plt.gca().patch.set_visible(True)
# #plt.grid(True)
# plt.savefig('US Covid-19 positives vs Date ' +  date_for_print + '.png')
# #plt.show()
# plt.grid(True)
# plt.clf()


# plt.figure(figsize=(14, 6))
# #plt.figure(figsize=(18.0, 12.0)) # The size of the figure is specified as (width, height) in inches
# plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
# plt.gcf().autofmt_xdate()
# plt.title(date_for_print + '  US 5-day rolling average vs Date')
# plt.xlabel('Date')
# plt.ylabel('US 5-day rolling average')
# #plt.plot(date_x[0:len(date_x)-4],roll_5,linestyle='--',label='5-day rolling average')
# plt.bar(date_x[0:len(date_x)-4],roll_5,label='5-day rolling average')
# plt.legend()
# #plt.grid(True)
# plt.tight_layout()
# plt.savefig('US 5-day rolling average vs Date ' +  date_for_print + '.png')
# plt.clf()
# #plt.savefig('US 5-day rolling average vs Date 2020_05_25.png')
# #plt.show(fig1)

# plt.figure(figsize=(14, 6)) # The size of the figure is specified as (width, height) in inches
# #print("printing dev_x",dev_x)
# #print("printing dev_y",dev_y)
# plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
# plt.gcf().autofmt_xdate()
# date_for_print = (date_x[0].strftime("%Y_%m_%d"))
# plt.title(date_for_print + '  US Covid-19 Daily Test Increase vs Date')
# plt.xlabel('Date')
# plt.ylabel('US Covid-19 Daily Test Increase')
# #plt.plot(date_x,dev_y,linestyle='solid',label='Positives')
# plt.bar(date_x,num_tests,label='Daily Test Increase')
# plt.tight_layout()
# plt.legend()
# #plt.grid(True)
# plt.savefig('US Covid-19 Daily Test Increase vs Date ' +  date_for_print + '.png')
# plt.clf()
# #plt.show()        


# plt.figure(figsize=(14, 6)) # The size of the figure is specified as (width, height) in inches
# #print("printing dev_x",dev_x)
# #print("printing dev_y",dev_y)
# plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
# plt.gcf().autofmt_xdate()
# date_for_print = (date_x[0].strftime("%Y_%m_%d"))
# plt.title(date_for_print + '  US Covid-19 Currently Hospitalized vs Date')
# plt.xlabel('Date')
# plt.ylabel('US Covid-19 Currently Hospitalized')
# #plt.plot(date_x,dev_y,linestyle='solid',label='Positives')
# plt.bar(date_x,cur_hosp,label='Currently Hospitalized')
# plt.tight_layout()
# plt.legend()
# #plt.grid(True)
# plt.savefig('US Covid-19 Currently Hospitalized vs Date ' +  date_for_print + '.png')
# plt.clf()
# #plt.show()        
# #hospitalizedCurrently

# #deaths per day
# plt.figure(figsize=(14, 6)) # The size of the figure is specified as (width, height) in inches
# plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
# plt.gcf().autofmt_xdate()
# date_for_print = (date_x[0].strftime("%Y_%m_%d"))
# plt.title(date_for_print + '  US Covid-19 Deaths per day vs Date')
# plt.xlabel('Date')
# plt.ylabel('US Covid-19 Deaths per day')
# plt.bar(date_x,death_increase,label='Deaths per day')
# plt.tight_layout()
# plt.legend()
# plt.savefig('US Covid-19 Deaths per day vs Date ' +  date_for_print + '.png')
# plt.clf()


# #percent positive
# plt.figure(figsize=(14, 6)) # The size of the figure is specified as (width, height) in inches
# #plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
# plt.gcf().autofmt_xdate()
# date_for_print = (date_x[0].strftime("%Y_%m_%d"))
# plt.title(date_for_print + '  US Covid-19 Percent Positive per day vs Date')
# plt.xlabel('Date')
# plt.ylabel('US Covid-19 Percent Positive per day')
# plt.bar(date_x,percent_positive,label='Percent Positive per day')
# plt.tight_layout()
# plt.legend()
# plt.savefig('US Covid-19 Percent Positive vs Date ' +  date_for_print + '.png')
# plt.clf()