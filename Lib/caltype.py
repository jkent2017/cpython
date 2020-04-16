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

from calendar import isleap, weekday
from math import floor, ceil

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

    dayNum = weekday(year, month, day)

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
        elif ii == 2 and isleap(year) == True:
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
    days = ""
    date = str(date)
    if century != 0:
        year += str(century)
    year += (date[0] + date[1])

    days += (date[2] + date[3] + date[4])

    days = int(days)

    dInM = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isleap(int(year)) == True:
        dInM[1] = 29

    month = 0

    for ii in range(12):
        if days < dInM[ii]:
            month = ii + 1
            break

        days -= dInM[ii];

    date = str(days) + '/' + str(month) + '/' + str(year)

    return date

# From a Gregorian date and an Epoch, a Julian Day will be provided
# Epoch will be a number entered alongside the date
#
# Will return an integer
#
# List of Epochs:
# 0 - Julian Date - 12h Jan 1, 4713 BCE
# 1 - Reduced JD - 12h Nov 16, 1858
# 2 - Modified JD - 0h Nov 17, 1858
# 3 - Truncated JD - 0h May 24, 1968
# 4 - Dublin JD - 12h Dec 31, 1899
# 5 - CNES JD - 0h Jan 1, 1950
# 6 - CCSDS JD - 0h Jan 1, 1958
# 7 - Lilian Date - Oct 15, 1582
# 8 - Rata Die - Jan 1, 1 Proleptic Gregorian Calendar
# 9 - Mars Sol Date - 12h Dec 29, 1873
# 10 - Unix Time - 0h Jan 1, 1970
# 11 - .NET DateTime - 0h Jan 1, 1 Proleptic Gregorian Calendar
def gregJulday(date, epoch):
    day, month, year = (int(i) for i in date.split('/'))
    day = int(day)
    month = int(month)
    year = int(year)

    jdn = ((1461 * (year + 4800 + (month - 14)/12))/4 +
           (367 * (month - 2 - 12 * ((month - 14)/12)))/12 -
           (3 * ((year + 4900 + (month - 14)/12)/100))/4 +
           day - 32075)

    if epoch == 0:
        return jdn
    elif epoch == 1:
        return(jdn - 2400000)
    elif epoch == 2:
        return(jdn - 2400000.5)
    elif epoch == 3:
        return(floor(jdn - 2440000.5))
    elif epoch == 4:
        return(jdn - 2415020)
    elif epoch == 5:
        return(jdn - 2433282.5)
    elif epoch == 6:
        return(jdn - 2436204.5)
    elif epoch == 7:
        return(floor(jdn - 2299159.5))
    elif epoch == 8:
        return(floor(jdn - 1721424.5))
    elif epoch == 9:
        return((jdn - 2405522)/1.02749)
    elif epoch == 10:
        return((jdn - 2440587.5) * 86400)
    elif epoch == 11:
        return((jdn - 1721424.5) * 864000000000)

def juldayGreg(jdn, epoch):
    if epoch == 1:
        jdn += 2400000
    elif epoch == 2:
        jdn += 2400000.5
    elif epoch == 3:
        jdn = ceil(jdn + 2440000.5)
    elif epoch == 4:
        jdn += 2415020
    elif epoch == 5:
        jdn += 2433282.5
    elif epoch == 6:
        jdn += 2436204.5
    elif epoch == 7:
        jdn = ceil(jdn + 2299159.5)
    elif epoch == 8:
        jdn = ceil(jdn + 1721424.5)
    elif epoch == 9:
        jdn = jdn * 1.02749 + 2405522
    elif epoch == 10:
        jdn = jdn / 86400 + 2440587.5
    elif epoch == 11:
        jdn = jdn / 864000000000 + 1721424.5

    

    f = jdn + 1401 + (((4 * jdn + 274277) / 146097) * 3) / 4 - 38
    e = 4 * f + 3
    g = e % 1461 / 4
    h = 5 * g + 2
    day = floor((h % 153) / 5)
    month = floor((h / 153 + 2) % 12 + 1)
    year = floor((e / 1461) - 4716 + (12 + 2 - month) / 12)

    date = str(day) + '/' + str(month) + '/' + str(year)

    return date

