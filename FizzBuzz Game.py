name = input("Welcome to FizzBuz! What is your name? ")
print(f"Welcome {name}, let's play!")

#range
lower_number = int(input("Enter the lower margin: "))
upper_number = int(input("Enter the upper margin: "))
for num in range (lower_number,upper_number+1):
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")

    elif num % 3 == 0:
        print("Fizz")

    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
