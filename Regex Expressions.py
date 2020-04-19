import re

#url_regex = re.compile(r"https?(://){1}[0-9a-zA-Z,./<>:;]+\.[a-zA-Z0-9]+")
#checking = url_regex.search("this is a test http://www.goobnmge.com does this work?")
#if checking == None:
 #   print("No Matches Found")
#else:
 #   print(checking.group())
"""
def cleanUpDate(text):
    dates_regex = re.compile(r"(^[0-3]\d)\/([0-1][0-9])\/([1-2]\d{3})$")
    year = int(dates_regex.search(text).groups()[2])
    month = int(dates_regex.search(text).groups()[1])
    day = int(dates_regex.search(text).groups()[0])
    print(day, month, year)
    lyear = False
    invaliddate= False
    while not invaliddate:
        if year % 400==0 or (year%4==0 and not year%100 == 0): #leap year
            lyear = True
            if lyear and month==2 and day>29:
                print("This is not a valid date because {} is not a valid day in February".format(day))
                break
        if month>12 or day>31:
            if month>12:
                print("The month is incorrect.")
            elif day>31:
                print("The day is incorrect")
            break
        else:
            invaliddate = True
            break
    while invaliddate:
        if (month == 4) or (month == 6) or (month == 9) or (month == 11):
            if day>30:
                print("This is not a valid date because {} is not a day in {} calender month.".format(day, month))
                break
        else:
            invaliddate = True
            break
    if invaliddate:
        print("The date that you have provided is a valid date. The Year {}, Month {} and Day {} works".format(year, month, day))

text = "30/15/1200"
cleanUpDate("19/04/2400")
"""
char = input("Character you would like to strip from the string: ")
context = input("Your String that you want strip using Character: ")

import re

def regex_strip(char, context):
    strip_content = None
    if char == "":
        empty_regex = re.compile(r"^\s+|\s+$")
        strip_content = empty_regex.sub("", context)
        return strip_content
    else:
        strip_content = re.sub(r"^{}+|{}+$".format(char,char),"", regex_strip("", context))
        return strip_content

print(regex_strip(char, context))


