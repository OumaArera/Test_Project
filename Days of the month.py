#Function to determne if year is leap
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False

#defining the function
def days_in_month(year, month):

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #Checking if month is February and year is leap
    if month == 2 and is_leap(year):
       return f"Day of the month of {month} is 29 days."

    #month is not 2 and year is leap or not leap
    else:
       return f"Day of the month of {month} is {month_days[month - 1]}"



year_selected = int(input("Enter the year "))

month_selected = int(input("Enter the month "))

#Months cannot exceed 12
if month_selected > 12:
    print("Value too big to be a month")
    month_selected = int(input("Enter the month "))

days = days_in_month(year_selected, month_selected)
print(days)
