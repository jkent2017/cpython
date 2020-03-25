# This library will have various types of calendars and features
# relating to the calendars. This started as a desire to make the
# datetime library allow BCE dates for finding the day of the week,
# and now I just want to make a library for all types of calendars.

# This library will use datetime, but will modify the inputs to allow
# for more overall features
from datetime import *
from sys import stdout

# Leap years divisible by 400 always start on a Saturday?

# Provided a year, checks if it is a leap year
def isLeap(y):
    if y % 100 == 0:
        if y % 400 == 0:
            return 1
        else:
            return 0
    elif y % 4 == 0:
        return 1
    else:
        return 0
