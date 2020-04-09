#########################################################################
# This library will have various types of calendars and features        #
# relating to the calendars. This started as a desire to make the       #
# datetime library allow BCE dates for finding the day of the week,     #
# and now I just want to make a library for all types of calendars.     #
#                                                                       #
# The issue with datetime is that it seems to only use Gergorian, and   #
# it doesn't allow for BCE dates. Calendar does, but because it views   #
# 1 BCE as year 0, all BCE years are offset by +1, such as 20 BCE       #
# being viewed as -19 in calendar.                                      #
#                                                                       #
# caltype does not have a year 0. December 31 0001 BCE with go to       #
# January 1 0001 CE. This 'year 0' seems to be an issue in of itself.   #
# January 1 0001 CE is under the assumption to be Monday                #
#########################################################################

# This library uses aspects of datetime and calendar, and datetime is
# imported in calendar
import calendar

# Leap years divisible by 400 always start on a Saturday?

# Returns the day of the week of a date as a string. Must be given as
# day, month, year in that order. Must be in DD/MM/YYYY format
#
# Does not need to be written with 0's in place of null spots.
# 21/3/456 works.
def getWeekday(date):
    days =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
           "Saturday", "Sunday"]

    day, month, year = (int(i) for i in date.split('/'))

    if year < 0:
        year += 1

    dayNum = calendar.weekday(year, month, day)

    return(days[dayNum])

def getDays(day, month, year):
    num = 0
    num += day
    month -= 1

    ii = 1
    for ii in range(month):
        if ii == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            num += 31
        elif ii == 4 or 6 or 9 or 11:
            num += 30
        elif ii == 2 and calendar.isleap(year) == True:
            num += 29
        else:
            num += 28

    num = str(num)

    if len(num) == 3:
        return num
    if len(num) == 2:
        return ("0" + num)
    if len(num) == 1:
        return ("00" + num)

def gregJulshort(date):
    day, month, year = (int(i) for i in date.split('/'))

    julshort = ""

    year = abs(year)

    if year > 9 and year < 100:
        year = str(year)
        julshort += (year[0] + year[1])

    elif year > 99 and year < 1000:
        year = str(year)
        julshort += (year[1] + year[2])

    elif year > 999:
        year = str(year)
        julshort += (year[2] + year[3])

    else:
        year = str(year)
        julshort += ('0' + year[0])

    days = str(getDays(day, month, year))
    julshort += days

    return julshort

# Provided a Julian Short date and the century, a
# Gregorian date is returned. Century should be a positive
# or negative integer, with -5 being 5 BCE and 5 being 5 CE
def julshortGreg(date, century):
    year = ""
    date = str(date)
    if century != 0:
        year += str(century)
    year += (date[0] + date[1])

