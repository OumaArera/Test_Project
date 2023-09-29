year = int(input("ENter year -4 digit: "))

#checking if year is divisible by 4

if year % 4 == 0:
    #checking if after being divisible by 4 it is not divisible by 100 then it is a leap year
    if year % 100 != 0:
        print(f"{year} is a leap year!")

    #if the year is divisible by 100 but still divisible by 400 then it is a leap year
    else:
        if year % 400 == 0:
            print(f"{year} is a leap year!")
        #Year is not divisible by 400 but is divisible by 100 and 400 is not a leap year
        else:
            print(f"{year} is Not a leap year!")
# Year is not divisible by 4 is automatically not a leap year
else:
    print(f"{year} is Not a leap year!")