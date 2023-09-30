# Customer making order in either Small(S), Medium(M) or Large(L)
order = input("Enter your order: S, M, L: ")
bill = 0

# customer has ordered small
if order.lower() == 's':
    bill += 15

    # checking if customer wants spices
    spice = input("Do you want pepperoni? Y or N: ")
    if spice.lower() == 'y':
        bill += 2

    # customer wants extra cheese
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese.lower() == 'y':
        bill += 1

    print(f"Your bill is ${bill}")

# customer has ordered medium
elif order.lower() == 'm':
    bill += 20

    # checking if customer wants spices
    spice = input("Do you want pepperoni? Y or N: ")
    if spice.lower() == 'y':
        bill += 3

    # customer wants extra cheese
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese.lower() == 'y':
        bill += 1

    print(f"Your bill is ${bill}")

# customer has ordered large
elif order.lower() == 'l':
    bill += 25

    # checking if customer wants spices
    spice = input("Do you want pepperoni? Y or N: ")
    if spice.lower() == 'y':
        bill += 3

    # customer wants extra cheese
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese.lower() == 'y':
        bill += 1

    print(f"Your bill is ${bill}")