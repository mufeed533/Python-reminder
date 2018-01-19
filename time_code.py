#This python script will generate a TKinter widget which shows the remaining time you have from 13.12.17 to 31.12.18. As the days goes by, this script updates the remaining days, remaining seconds and remaing time in percent.
from Tkinter import *
import time
from datetime import datetime,date
from calendar import monthrange

#GUI module(customise the widget appearance).
root = Tk()
root.wm_title("Hurry!")
root.config(bg = "#828481")
clock = Label(root, font=('times', 15, 'bold'),highlightthickness=1, highlightbackground="#111",foreground = "white", bg='#0A2D4B',width=17, height=5,takefocus=0, wraplength=170, anchor=W,justify=CENTER)
clock.pack(fill=BOTH, expand=1)
clock.grid(row=0, column=0, padx=10, pady=2, sticky=N+S)

#function to count the number of days in different months. For ex: If you run the script in January(the initial month is set as December).
def daysInMonthCalculater(current_date,current_month,old_date,old_month,days_count,month_difference,old_year):
    #calculates the total days in old and current months
    total_days_old_month = monthrange(old_year, old_month)
    remaining_days_old_month = total_days_old_month[1] - old_date
    days_count = days_count + remaining_days_old_month + current_date

    #calculates the total days in month in between old and current months
    if(month_difference > 1):
        month_difference = month_difference - 1
        for i in range( 0,month_difference ):
            total_days_middle_month = monthrange(old_year, (old_month+1)+i)
            days_count = days_count + total_days_middle_month[1]
    return days_count


def tick():
    #fixed initial date
    old_date = 13
    old_month = 12
    old_year = 2017
    total_seconds = 33091200.00
    days_count = 0

    #get the current day,hour,minute,seconds,year
    time2 = datetime.now()
    current_hour= time2.hour
    current_minute = time2.minute
    current_seconds = time2.second
    current_date = time2.day
    current_month = time2.month
    current_year = time2.year

    #calculate the days count
    #calculate days count if the days are in same month
    if(current_date != old_date and current_month == old_month and current_year == old_year):
        days_count = days_count + (current_date - old_date)

    #calculate the days count if the days are in different months
    elif(current_month != old_month and current_year == old_year):
        month_difference = current_month - old_month
        days_count = daysInMonthCalculater(current_date,current_month,old_date,old_month,days_count,month_difference,old_year)

    #calculate the days count if the days are in different years
    elif(current_year != old_year):
        #to find the remaining days in last year,so changed the current date and month to de 31
        current_date1 = 31
        current_month1 = 12
        month_difference = 12 - old_month

        #if the month is December
        if(month_difference < 1):
            old_year_days_count = current_date1 - old_date
        else:
            old_year_days_count = daysInMonthCalculater(current_date1,current_month1,old_date,old_month,days_count,month_difference,old_year)

        #find the remining days in current years and add it with the days in last year.
        old_date = 1
        old_month = 1
        month_difference = current_month - old_month
        days_count = old_year_days_count + daysInMonthCalculater(current_date,current_month,old_date,old_month,days_count,month_difference,old_year)

    # print ("days count : %d"%days_count)
    remaining_seconds = total_seconds-( days_count*24*60*60 + current_hour*60*60 + current_minute*60 + current_seconds) - 31 #temporary fix. 
    # print("The timer started on 14/12/17")
    # print("remaining seconds : %d"%remaining_seconds)
    # print("remianing days :%d"%(remaining_seconds/(3600*24)))
    remaining_days = remaining_seconds/(3600*24)
    remaining_minute_percent = (remaining_days*100/365.25)
    # print("%0.2f"%remaining_minute_percent+"%")
    clock.config(text="%0.2f"%remaining_minute_percent+"%"+"\nseconds : %d"%remaining_seconds+"\nDays : %d"%remaining_days)
    clock.after(2, tick)

tick()
root.mainloop( )
