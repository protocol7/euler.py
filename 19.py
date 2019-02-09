#!/usr/bin/env python3

def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0

def months(year):
    if leap_year(year):
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 0 # 1900-01-01 is a Monday
sundays = 0
for year in range(1900, 2001):
    for m in months(year):
        day = (day + m) % 7

        if year > 1900 and day == 6:
            sundays += 1

print(sundays)
