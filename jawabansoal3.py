#Nama       : Umar Hilmi
#NIM        : 221402077
#Nomor      : 3

import datetime

def get_future_date(number_of_days):
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=number_of_days)
    return future_date.strftime("%A on %d %B %Y")

def main():
    print("This Python program will reads in a number and prints the date that number of days from now")
    number_of_days = int(input("Enter the number of days: "))
    future_date = get_future_date(number_of_days)
    current_date = datetime.datetime.now()

    print("The", number_of_days, "days from now (", current_date.strftime("%A, %d %B %Y"), ") will be:", future_date)

if __name__ == "__main__":
    main()
