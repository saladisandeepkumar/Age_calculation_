#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
from calendar import isleap

# Judge the leap year
def judge_leap_year(year):
    return isleap(year)

# Returns the number of days in each month
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year else 28

# Input user details
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth (e.g., 1995): "))
birth_month = int(input("Enter your month of birth (1-12): "))
birth_day = int(input("Enter your day of birth (1-31): "))

# Get the current date
localtime = time.localtime(time.time())
current_year = localtime.tm_year
current_month = localtime.tm_mon
current_day = localtime.tm_mday

years = current_year - birth_year
months = 0
days = 0

if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
    years -= 1

# Calculate months
months = (current_year - birth_year) * 12 + current_month - birth_month
if current_day < birth_day:
    months -= 1

days = 0

for y in range(birth_year, current_year):
    days += 366 if judge_leap_year(y) else 365

leap_year = judge_leap_year(current_year)
for m in range(1, current_month):
    days += month_days(m, leap_year)

days += current_day
leap_year_birth = judge_leap_year(birth_year)
for m in range(1, birth_month):
    days -= month_days(m, leap_year_birth)

days -= birth_day

print(f"{name}'s age is {years} years, or {months} months, or {days} days.")

