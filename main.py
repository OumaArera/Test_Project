

bill = float(input("Enter the bill: "))
percentage_tip = float(input("Enter the float percentage: "))
total_bill = bill*(1 + (percentage_tip/100))
no_of_sharing = int(input("How many are sharing this bill? "))
each_contribution = total_bill / no_of_sharing

if no_of_sharing == 1:
    pass
else:
    print("Each of you will contribute:", round(each_contribution, 2))

tip = total_bill - bill

if tip == 0:
    print("Total bill =", round(total_bill), "\nThank you for shopping at Naivas. We value you!")
else:
    print("Total bill =", round(total_bill), "\nYour Tip to the cashier =", round(tip), "\nThank you for shopping at Naivas. We value you!")