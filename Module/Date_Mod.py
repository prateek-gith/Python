from datetime import date

# date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)



# calling the today
# function of date class
today = date.today()

# Python program to
# print current date
print("Today's date is", today)

# Converting the date to the string
Str = date.isoformat(today)
print("String Representation", Str)