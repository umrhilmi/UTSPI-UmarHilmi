#Nama       : Umar Hilmi
#NIM        : 221402077
#Nomor      : 1

import datetime

current_year = datetime.datetime.now().year
num_days = (datetime.datetime(current_year + 1, 1, 1) - datetime.datetime(current_year, 1, 1)).days

print("This program will reads a whole number and divides it by number of days this year and displays the result with eleven decimal places if they exist (rounded up).")
whole_number = int(input("Enter a whole number: "))
result = whole_number / num_days

print(f"Result: {result:.11f}")