name = input("What is your name? ")

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))
bmi = round(weight / (height ** 2))

if bmi < 18.5:
    print(f"{name} you're underweight! Your BMI is {bmi}")

elif bmi < 25:
    print(f"{name} you have a normal weight! Your BMI is {bmi}")

elif bmi < 30:
    print(f"{name} you're slightly overweight! Your BMI is {bmi}")

elif bmi < 35:
    print(f"{name} you're obese! Your BMI is {bmi}")

else:
    print(f"{name} you're clinically obese! Your BMI is {bmi}")