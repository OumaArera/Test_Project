print("Welome to Naivas Supermarket")

#Enter the bill amount
bill = float(input("Enter the bill: "))

#Enter the percentage tip
percentage_tip = float(input("Enter the float percentage: "))

#Calculating total bill ie including tip
total_bill = bill*(1 + (percentage_tip/100))

#Number of people sharing the bill
no_of_sharing = int(input("How many are sharing this bill? "))

#Each person contribution
each_contribution = total_bill / no_of_sharing

#Checking if the bill is to be shared or not
if no_of_sharing == 1:
    pass
else:
    print("Each of you will contribute:", round(each_contribution, 2))

#Calculating tip
tip = total_bill - bill

#Checking if customer gave tip or not
if tip == 0:
    print("Total bill =", round(total_bill), "\nThank you for shopping at Naivas. We value you!")
else:
    print("Total bill =", round(total_bill), "\nYour Tip to the cashier =", round(tip), "\nThank you for shopping at Naivas. We value you!")

