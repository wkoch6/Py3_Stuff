import csv
import time
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import datetime
from matplotlib import dates as mpl_dates

#check_state = "CO"
#check_state = "GA"
#check_state = "AL"
#check_state = "FL"
#check_state = "NC"
#check_state = "NY"
#check_state = "VA"
#check_state = "WI"
#check_state = "TX"

states = ["CO","AL","AZ","FL","GA","NC", "NY","TX","VA","WI"]


roll_5 = []
date_x = []
dev_x = []
dev_y = []
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

for check_state in states:
    roll_5 = []
    date_x = []
    dev_x = []
    dev_y = []
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
    with open('C:\Users\C40630\Downloads\daily - 2020-07-17T171813.883.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file) # the entire csv file is read into "csv_reader"
        #print("'date', 'num_increase'")
        for line in csv_reader:
            #print(line['state'])
            #print(type(line['state']))
            if (line['state']) == check_state:
                #print("line is of type: ",type(line))
                #print(line)
                print(line['state'])
                my_temp_date = (line['date'])
                year = int(my_temp_date[:4])
                month = int(my_temp_date[4:6:1])
                day = int(my_temp_date[6:])
                my_date = datetime.datetime(year,month,day)
                #print("my date is: ", my_date)
                #print("my_date = ",my_date)
                #print("my_temp_date is type: ",type(my_temp_date))
                #print("year = ", year)
                #print("month = ", month)
                #print("day = ", day)
                date_x.append(my_date)
                dev_x.append(int((line['date'])))
                dev_y.append(int((line['positiveIncrease'])))
                #print("line[date] is of type",type(line['date']))
                #print("line[date] is of type",type(int((line['date']))))
                #print(line['date'],line['positiveIncrease'])
                #print("line is of type: ",type(line))
                if len(date_x) >= 5:
                    #print"x is greater than or equal to 5"
                    #print("date_x length is: ",len(date_x))
                    #print("date is: ", my_date)
                    #print(dev_y[len(date_x)-1])
                    #print(dev_y[len(date_x)-5])
                    #print("date_x -5 is: ",date_x[len(date_x)-5])
                    temp_sum = sum(dev_y[len(date_x)-5:len(date_x)])
                    #print(temp_sum)
                    #print(temp_sum/5)
                    roll_5.append(temp_sum/5)
                    #print(dev_y[len(date_x)-5:len(date_x)])
                    #break
                if int(line['date']) <= 20200315:
                    print "March 15 found -- break here"
                    csv_file.close()
                    break

    #print("date_x is of type: ",type(date_x))

    plt.figure(figsize=(12, 6)) # The size of the figure is specified as (width, height) in inches
    #print("printing dev_x",dev_x)
    #print("printing dev_y",dev_y)
    date_for_print = (date_x[0].strftime("%Y_%m_%d"))
    plt.title(date_for_print + ' ' + check_state + ' positives vs Date')
    plt.xlabel('Date')
    plt.ylabel(check_state + ' Covid-19 positives')
    #plt.plot(date_x,dev_y,linestyle='solid',label='Positives')
    plt.bar(date_x,dev_y,label='Positives')
    plt.tight_layout()
    plt.legend()
    #plt.grid(True)
    plt.savefig(check_state + ' Covid-19 positives vs Date ' +  date_for_print + '.png')
    plt.clf()
    #plt.show()
    #time.sleep(1)

    plt.figure(figsize=(12, 6))
    #plt.figure(figsize=(18.0, 12.0)) # The size of the figure is specified as (width, height) in inches
    plt.title(date_for_print + ' ' + check_state + '  5-day rolling average vs Date')
    plt.xlabel('Date')
    plt.ylabel(check_state + '  5-day rolling average')
    #plt.plot(date_x[0:len(date_x)-4],roll_5,linestyle='--',label='5-day rolling average')
    plt.bar(date_x[0:len(date_x)-4],roll_5,label='5-day rolling average')
    plt.legend()
    #plt.grid(True)
    plt.tight_layout()
    plt.savefig(check_state + ' 5-day rolling average vs Date ' +  date_for_print + '.png')
    plt.clf()
    #plt.savefig('US 5-day rolling average vs Date 2020_05_25.png')
    #plt.show(fig1)
    #time.sleep(1)
        