#Our Calculator is good now
#It can handle simple arithmetic operations
#It can handle trigonometry
#It can handle log, and exponentials

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

from math import factorial
from math import sin
from math import cos
from math import tan
from math import exp
from math import pi
from math import log10
from math import log
from math import sqrt
from math import asin
from math import acos
from math import atan
from math import acosh
from math import cosh
# from Calculator Logo import logo

#We define the function
def calculator(symbol,entry1, entry2):
    '''
    Calculator takes the two entries and work out the operation
    '''

    product = 0

    if symbol == "x":
        product = entry1 * entry2

        #Continuing with operation
        continue_operation = True
        other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

        #If one wishes to continue with operations
        if other_operation == "y":

            #Operations continue in a loop unless terminated
            while True:

                operator3 = input("\nType an operation type ").lower()

                # Terminate the loop
                # returns the answer
                if operator3 == "=":
                    # continue_operation = False
                    print(f"\n= {product}")
                    quit()

                third_entry = float(input("\nEnter number "))

                #Multiplying
                if operator3 == "x":
                    product = product * third_entry

                #Dividing
                elif operator3 == "/":
                    product = product / third_entry

                #Adding
                elif operator3 == "+":
                    product = product + third_entry

                #Subtracting
                elif operator3 == "-":
                    product = product - third_entry

                #Log operation
                elif operator3 == "log":
                    product = log(product)

                #Exponential operation
                elif operator3 == "e":
                    product = exp(product)

                #Sin operation
                elif operator3 == "sin":
                    product = cosh(product)

                #Cosine operation
                elif operator3 == "cos":
                    product = cos(product)

                #Coshine operation
                elif operator3 == "cosh":
                    product = cosh(product)

                #Tan operation
                elif operator3 == "tan":
                    product = tan(product)

                #Sin inverse
                elif operator3 == "sin-1":
                    product = asin(product)

                #Cos inverse
                elif operator3 == "cos-1":
                    product = acos(product)

                #Cosh inverse
                elif operator3 == "cosh-1":
                    product = acosh(product)

                #Raising product to power n
                elif operator3 == "^":
                    product = product ** third_entry

                #Square root of product
                elif operator3 == "rt":
                    product = sqrt(product)

                #Multiplying product by pi
                elif operator3 == "pi":
                    product = product * pi

                #Finding modulus of product
                elif operator3 == "%":
                    product = product % third_entry


        return product

    #Dividing
    elif symbol == "/":
        product = entry1 / entry2

        #Continuing with operation
        continue_operation = True
        other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

        #If one wishes to continue with operations
        if other_operation == "y":

            #Operations continue in a loop unless terminated
            while continue_operation:

                operator3 = input("\nType an operation type ").lower()

                # Terminate the loop
                # returns the answer
                if operator3 == "=":
                    # continue_operation = False
                    print(f"\n= {product}")
                    quit()

                third_entry = float(input("\nEnter number "))

                #Multiplying
                if operator3 == "x":
                    product = product * third_entry

                #Dividing
                elif operator3 == "/":
                    product = product / third_entry

                #Adding
                elif operator3 == "+":
                    product = product + third_entry

                #Subtracting
                elif operator3 == "-":
                    product = product - third_entry

                #Log operation
                elif operator3 == "log":
                    product = log(product)

                #Exponential operation
                elif operator3 == "e":
                    product = exp(product)

                #Sin operation
                elif operator3 == "sin":
                    product = cosh(product)

                #Cosine operation
                elif operator3 == "cos":
                    product = cos(product)

                #Coshine operation
                elif operator3 == "cosh":
                    product = cosh(product)

                #Tan operation
                elif operator3 == "tan":
                    product = tan(product)

                #Sin inverse
                elif operator3 == "sin-1":
                    product = asin(product)

                #Cos inverse
                elif operator3 == "cos-1":
                    product = acos(product)

                #Cosh inverse
                elif operator3 == "cosh-1":
                    product = acosh(product)

                #Raising product to power n
                elif operator3 == "^":
                    product = product ** third_entry

                #Square root of product
                elif operator3 == "rt":
                    product = sqrt(product)

                #Multiplying product by pi
                elif operator3 == "pi":
                    product = product * pi

                #Finding modulus of product
                elif operator3 == "%":
                    product = product % third_entry


        return product

    #Adding
    elif symbol == "+":
        product = entry1 + entry2

        #Continuing with operation
        continue_operation = True
        other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

        #If one wishes to continue with operations
        if other_operation == "y":

            #Operations continue in a loop unless terminated
            while continue_operation:

                operator3 = input("\nType an operation type ").lower()

                # Terminate the loop
                # returns the answer
                if operator3 == "=":
                    # continue_operation = False
                    print(f"\n= {product}")
                    quit()

                third_entry = float(input("\nEnter number "))

                #Multiplying
                if operator3 == "x":
                    product = product * third_entry

                #Dividing
                elif operator3 == "/":
                    product = product / third_entry

                #Adding
                elif operator3 == "+":
                    product = product + third_entry

                #Subtracting
                elif operator3 == "-":
                    product = product - third_entry

                #Log operation
                elif operator3 == "log":
                    product = log(product)

                #Exponential operation
                elif operator3 == "e":
                    product = exp(product)

                #Sin operation
                elif operator3 == "sin":
                    product = cosh(product)

                #Cosine operation
                elif operator3 == "cos":
                    product = cos(product)

                #Coshine operation
                elif operator3 == "cosh":
                    product = cosh(product)

                #Tan operation
                elif operator3 == "tan":
                    product = tan(product)

                #Sin inverse
                elif operator3 == "sin-1":
                    product = asin(product)

                #Cos inverse
                elif operator3 == "cos-1":
                    product = acos(product)

                #Cosh inverse
                elif operator3 == "cosh-1":
                    product = acosh(product)

                #Raising product to power n
                elif operator3 == "^":
                    product = product ** third_entry

                #Square root of product
                elif operator3 == "rt":
                    product = sqrt(product)

                #Multiplying product by pi
                elif operator3 == "pi":
                    product = product * pi

                #Finding modulus of product
                elif operator3 == "%":
                    product = product % third_entry

                #Terminate the loop
                #returns the answer
                elif operator3 == "=":
                    print(f"= {product}")

        return product

    #Subtracting
    elif symbol == "-":
        product = entry1 - entry2

        #Continuing with operation
        continue_operation = True
        other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

        #If one wishes to continue with operations
        if other_operation == "y":

            #Operations continue in a loop unless terminated
            while continue_operation:

                operator3 = input("\nType an operation type ").lower()

                # Terminate the loop
                # returns the answer
                if operator3 == "=":
                    # continue_operation = False
                    print(f"\n= {product}")
                    quit()

                third_entry = float(input("\nEnter number "))

                #Multiplying
                if operator3 == "x":
                    product = product * third_entry

                #Dividing
                elif operator3 == "/":
                    product = product / third_entry

                #Adding
                elif operator3 == "+":
                    product = product + third_entry

                #Subtracting
                elif operator3 == "-":
                    product = product - third_entry

                #Log operation
                elif operator3 == "log":
                    product = log(product)

                #Exponential operation
                elif operator3 == "e":
                    product = exp(product)

                #Sin operation
                elif operator3 == "sin":
                    product = cosh(product)

                #Cosine operation
                elif operator3 == "cos":
                    product = cos(product)

                #Coshine operation
                elif operator3 == "cosh":
                    product = cosh(product)

                #Tan operation
                elif operator3 == "tan":
                    product = tan(product)

                #Sin inverse
                elif operator3 == "sin-1":
                    product = asin(product)

                #Cos inverse
                elif operator3 == "cos-1":
                    product = acos(product)

                #Cosh inverse
                elif operator3 == "cosh-1":
                    product = acosh(product)

                #Raising product to power n
                elif operator3 == "^":
                    product = product ** third_entry

                #Square root of product
                elif operator3 == "rt":
                    product = sqrt(product)

                #Multiplying product by pi
                elif operator3 == "pi":
                    product = product * pi

                #Finding modulus of product
                elif operator3 == "%":
                    product = product % third_entry

        return product

    #Raising to power
    elif symbol == "^":
        product = entry1 ** entry2

        #Continuing with operation
        continue_operation = True
        other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

        #If one wishes to continue with operations
        if other_operation == "y":

            #Operations continue in a loop unless terminated
            while continue_operation:

                operator3 = input("\nType an operation type ").lower()

                # Terminate the loop
                # returns the answer
                if operator3 == "=":
                    # continue_operation = False
                    print(f"\n= {product}")
                    quit()

                third_entry = float(input("\nEnter number "))

                #Multiplying
                if operator3 == "x":
                    product = product * third_entry

                #Dividing
                elif operator3 == "/":
                    product = product / third_entry

                #Adding
                elif operator3 == "+":
                    product = product + third_entry

                #Subtracting
                elif operator3 == "-":
                    product = product - third_entry

                #Log operation
                elif operator3 == "log":
                    product = log(product)

                #Exponential operation
                elif operator3 == "e":
                    product = exp(product)

                #Sin operation
                elif operator3 == "sin":
                    product = cosh(product)

                #Cosine operation
                elif operator3 == "cos":
                    product = cos(product)

                #Coshine operation
                elif operator3 == "cosh":
                    product = cosh(product)

                #Tan operation
                elif operator3 == "tan":
                    product = tan(product)

                #Sin inverse
                elif operator3 == "sin-1":
                    product = asin(product)

                #Cos inverse
                elif operator3 == "cos-1":
                    product = acos(product)

                #Cosh inverse
                elif operator3 == "cosh-1":
                    product = acosh(product)

                #Raising product to power n
                elif operator3 == "^":
                    product = product ** third_entry

                #Square root of product
                elif operator3 == "rt":
                    product = sqrt(product)

                #Multiplying product by pi
                elif operator3 == "pi":
                    product = product * pi

                #Finding modulus of product
                elif operator3 == "%":
                    product = product % third_entry

        return product

    #Power to the nth number
    elif symbol == "nrt":
        product = entry1 ** (1/entry2)

        #Continuing with operation
        continue_operation = True
        other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

        #If one wishes to continue with operations
        if other_operation == "y":

            #Operations continue in a loop unless terminated
            while continue_operation:

                operator3 = input("\nType an operation type ").lower()

                # Terminate the loop
                # returns the answer
                if operator3 == "=":
                    # continue_operation = False
                    print(f"\n= {product}")
                    quit()

                third_entry = float(input("\nEnter number "))

                #Multiplying
                if operator3 == "x":
                    product = product * third_entry

                #Dividing
                elif operator3 == "/":
                    product = product / third_entry

                #Adding
                elif operator3 == "+":
                    product = product + third_entry

                #Subtracting
                elif operator3 == "-":
                    product = product - third_entry

                #Log operation
                elif operator3 == "log":
                    product = log(product)

                #Exponential operation
                elif operator3 == "e":
                    product = exp(product)

                #Sin operation
                elif operator3 == "sin":
                    product = cosh(product)

                #Cosine operation
                elif operator3 == "cos":
                    product = cos(product)

                #Coshine operation
                elif operator3 == "cosh":
                    product = cosh(product)

                #Tan operation
                elif operator3 == "tan":
                    product = tan(product)

                #Sin inverse
                elif operator3 == "sin-1":
                    product = asin(product)

                #Cos inverse
                elif operator3 == "cos-1":
                    product = acos(product)

                #Cosh inverse
                elif operator3 == "cosh-1":
                    product = acosh(product)

                #Raising product to power n
                elif operator3 == "^":
                    product = product ** third_entry

                #Square root of product
                elif operator3 == "rt":
                    product = sqrt(product)

                #Multiplying product by pi
                elif operator3 == "pi":
                    product = product * pi

                #Finding modulus of product
                elif operator3 == "%":
                    product = product % third_entry

        return product

    #Modulus
    elif symbol == "%":
        product = entry1 % entry2

        #Continuing with operation
        continue_operation = True
        other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

        #If one wishes to continue with operations
        if other_operation == "y":

            #Operations continue in a loop unless terminated
            while continue_operation:

                operator3 = input("\nType an operation type ").lower()

                # Terminate the loop
                # returns the answer
                if operator3 == "=":
                    # continue_operation = False
                    print(f"\n= {product}")
                    quit()

                third_entry = float(input("\nEnter number "))

                #Multiplying
                if operator3 == "x":
                    product = product * third_entry

                #Dividing
                elif operator3 == "/":
                    product = product / third_entry

                #Adding
                elif operator3 == "+":
                    product = product + third_entry

                #Subtracting
                elif operator3 == "-":
                    product = product - third_entry

                #Log operation
                elif operator3 == "log":
                    product = log(product)

                #Exponential operation
                elif operator3 == "e":
                    product = exp(product)

                #Sin operation
                elif operator3 == "sin":
                    product = cosh(product)

                #Cosine operation
                elif operator3 == "cos":
                    product = cos(product)

                #Coshine operation
                elif operator3 == "cosh":
                    product = cosh(product)

                #Tan operation
                elif operator3 == "tan":
                    product = tan(product)

                #Sin inverse
                elif operator3 == "sin-1":
                    product = asin(product)

                #Cos inverse
                elif operator3 == "cos-1":
                    product = acos(product)

                #Cosh inverse
                elif operator3 == "cosh-1":
                    product = acosh(product)

                #Raising product to power n
                elif operator3 == "^":
                    product = product ** third_entry

                #Square root of product
                elif operator3 == "rt":
                    product = sqrt(product)

                #Multiplying product by pi
                elif operator3 == "pi":
                    product = product * pi

                #Finding modulus of product
                elif operator3 == "%":
                    product = product % third_entry

        return product

    #Log to base n
    elif symbol == "logn":
        product = log(entry1,entry2)

        #Continuing with operation
        continue_operation = True
        other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

        #If one wishes to continue with operations
        if other_operation == "y":

            #Operations continue in a loop unless terminated
            while continue_operation:

                operator3 = input("\nType an operation type ").lower()

                # Terminate the loop
                # returns the answer
                if operator3 == "=":
                    # continue_operation = False
                    print(f"\n= {product}")
                    quit()

                third_entry = float(input("\nEnter number "))

                #Multiplying
                if operator3 == "x":
                    product = product * third_entry

                #Dividing
                elif operator3 == "/":
                    product = product / third_entry

                #Adding
                elif operator3 == "+":
                    product = product + third_entry

                #Subtracting
                elif operator3 == "-":
                    product = product - third_entry

                #Log operation
                elif operator3 == "log":
                    product = log(product)

                #Exponential operation
                elif operator3 == "e":
                    product = exp(product)

                #Sin operation
                elif operator3 == "sin":
                    product = cosh(product)

                #Cosine operation
                elif operator3 == "cos":
                    product = cos(product)

                #Coshine operation
                elif operator3 == "cosh":
                    product = cosh(product)

                #Tan operation
                elif operator3 == "tan":
                    product = tan(product)

                #Sin inverse
                elif operator3 == "sin-1":
                    product = asin(product)

                #Cos inverse
                elif operator3 == "cos-1":
                    product = acos(product)

                #Cosh inverse
                elif operator3 == "cosh-1":
                    product = acosh(product)

                #Raising product to power n
                elif operator3 == "^":
                    product = product ** third_entry

                #Square root of product
                elif operator3 == "rt":
                    product = sqrt(product)

                #Multiplying product by pi
                elif operator3 == "pi":
                    product = product * pi

                #Finding modulus of product
                elif operator3 == "%":
                    product = product % third_entry

        return product



first_entry = float(input("\nEnter the first value: "))

#Operation symbol
operator = input("\nSelect symbol, x,/, +, -, ^, rt, !, e, nrt, cos, cosh, sin, tan, pi, %, log, logn, sin-1, cos-1, tan-1, cosh-1: ").lower()

#checking for square root
if operator == "rt":
    product =sqrt(first_entry)

    #Continuing with operation
    continue_operation = True
    other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

    #If one wishes to continue with operations
    if other_operation == "y":

        #Operations continue in a loop unless terminated
        while continue_operation:

            operator3 = input("\nType an operation type ").lower()

            # Terminate the loop
            # returns the answer
            if operator3 == "=":
                # continue_operation = False
                print(f"\n= {product}")
                quit()

            third_entry = float(input("\nEnter number "))

            #Multiplying
            if operator3 == "x":
                product = product * third_entry

            #Dividing
            elif operator3 == "/":
                product = product / third_entry

            #Adding
            elif operator3 == "+":
                product = product + third_entry

            #Subtracting
            elif operator3 == "-":
                product = product - third_entry

            #Log operation
            elif operator3 == "log":
                product = log(product)

            #Exponential operation
            elif operator3 == "e":
                product = exp(product)

            #Sin operation
            elif operator3 == "sin":
                product = cosh(product)

            #Cosine operation
            elif operator3 == "cos":
                product = cos(product)

            #Coshine operation
            elif operator3 == "cosh":
                product = cosh(product)

            #Tan operation
            elif operator3 == "tan":
                product = tan(product)

            #Sin inverse
            elif operator3 == "sin-1":
                product = asin(product)

            #Cos inverse
            elif operator3 == "cos-1":
                product = acos(product)

            #Cosh inverse
            elif operator3 == "cosh-1":
                product = acosh(product)

            #Raising product to power n
            elif operator3 == "^":
                product = product ** third_entry

            #Square root of product
            elif operator3 == "rt":
                product = sqrt(product)

            #Multiplying product by pi
            elif operator3 == "pi":
                product = product * pi

            #Finding modulus of product
            elif operator3 == "%":
                product = product % third_entry


    print(f"\n= {product}")
    quit()

#checking if it is factorial
elif operator == "!":
    product = factorial(first_entry)

    #Continuing with operation
    continue_operation = True
    other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

    #If one wishes to continue with operations
    if other_operation == "y":

        #Operations continue in a loop unless terminated
        while continue_operation:

            operator3 = input("\nType an operation type ").lower()

            # Terminate the loop
            # returns the answer
            if operator3 == "=":
                # continue_operation = False
                print(f"\n= {product}")
                quit()

            third_entry = float(input("\nEnter number "))

            #Multiplying
            if operator3 == "x":
                product = product * third_entry

            #Dividing
            elif operator3 == "/":
                product = product / third_entry

            #Adding
            elif operator3 == "+":
                product = product + third_entry

            #Subtracting
            elif operator3 == "-":
                product = product - third_entry

            #Log operation
            elif operator3 == "log":
                product = log(product)

            #Exponential operation
            elif operator3 == "e":
                product = exp(product)

            #Sin operation
            elif operator3 == "sin":
                product = cosh(product)

            #Cosine operation
            elif operator3 == "cos":
                product = cos(product)

            #Coshine operation
            elif operator3 == "cosh":
                product = cosh(product)

            #Tan operation
            elif operator3 == "tan":
                product = tan(product)

            #Sin inverse
            elif operator3 == "sin-1":
                product = asin(product)

            #Cos inverse
            elif operator3 == "cos-1":
                product = acos(product)

            #Cosh inverse
            elif operator3 == "cosh-1":
                product = acosh(product)

            #Raising product to power n
            elif operator3 == "^":
                product = product ** third_entry

            #Square root of product
            elif operator3 == "rt":
                product = sqrt(product)

            #Multiplying product by pi
            elif operator3 == "pi":
                product = product * pi

            #Finding modulus of product
            elif operator3 == "%":
                product = product % third_entry


    print(f"\n= {product}")
    quit()

#Exponential
elif operator == "e":
    product = exp(first_entry)

    #Continuing with operation
    continue_operation = True
    other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

    #If one wishes to continue with operations
    if other_operation == "y":

        #Operations continue in a loop unless terminated
        while continue_operation:

            operator3 = input("\nType an operation type ").lower()

            # Terminate the loop
            # returns the answer
            if operator3 == "=":
                # continue_operation = False
                print(f"\n= {product}")
                quit()

            third_entry = float(input("\nEnter number "))

            #Multiplying
            if operator3 == "x":
                product = product * third_entry

            #Dividing
            elif operator3 == "/":
                product = product / third_entry

            #Adding
            elif operator3 == "+":
                product = product + third_entry

            #Subtracting
            elif operator3 == "-":
                product = product - third_entry

            #Log operation
            elif operator3 == "log":
                product = log(product)

            #Exponential operation
            elif operator3 == "e":
                product = exp(product)

            #Sin operation
            elif operator3 == "sin":
                product = cosh(product)

            #Cosine operation
            elif operator3 == "cos":
                product = cos(product)

            #Coshine operation
            elif operator3 == "cosh":
                product = cosh(product)

            #Tan operation
            elif operator3 == "tan":
                product = tan(product)

            #Sin inverse
            elif operator3 == "sin-1":
                product = asin(product)

            #Cos inverse
            elif operator3 == "cos-1":
                product = acos(product)

            #Cosh inverse
            elif operator3 == "cosh-1":
                product = acosh(product)

            #Raising product to power n
            elif operator3 == "^":
                product = product ** third_entry

            #Square root of product
            elif operator3 == "rt":
                product = sqrt(product)

            #Multiplying product by pi
            elif operator3 == "pi":
                product = product * pi

            #Finding modulus of product
            elif operator3 == "%":
                product = product % third_entry


    print(f"\n= {product}")
    quit()

#Sin operation
elif operator == "sin":
    product = sin(first_entry)

    #Continuing with operation
    continue_operation = True
    other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

    #If one wishes to continue with operations
    if other_operation == "y":

        #Operations continue in a loop unless terminated
        while continue_operation:

            operator3 = input("\nType an operation type ").lower()

            # Terminate the loop
            # returns the answer
            if operator3 == "=":
                # continue_operation = False
                print(f"\n= {product}")
                quit()

            third_entry = float(input("\nEnter number "))

            #Multiplying
            if operator3 == "x":
                product = product * third_entry

            #Dividing
            elif operator3 == "/":
                product = product / third_entry

            #Adding
            elif operator3 == "+":
                product = product + third_entry

            #Subtracting
            elif operator3 == "-":
                product = product - third_entry

            #Log operation
            elif operator3 == "log":
                product = log(product)

            #Exponential operation
            elif operator3 == "e":
                product = exp(product)

            #Sin operation
            elif operator3 == "sin":
                product = cosh(product)

            #Cosine operation
            elif operator3 == "cos":
                product = cos(product)

            #Coshine operation
            elif operator3 == "cosh":
                product = cosh(product)

            #Tan operation
            elif operator3 == "tan":
                product = tan(product)

            #Sin inverse
            elif operator3 == "sin-1":
                product = asin(product)

            #Cos inverse
            elif operator3 == "cos-1":
                product = acos(product)

            #Cosh inverse
            elif operator3 == "cosh-1":
                product = acosh(product)

            #Raising product to power n
            elif operator3 == "^":
                product = product ** third_entry

            #Square root of product
            elif operator3 == "rt":
                product = sqrt(product)

            #Multiplying product by pi
            elif operator3 == "pi":
                product = product * pi

            #Finding modulus of product
            elif operator3 == "%":
                product = product % third_entry

    print(f"\n= {product}")
    quit()

#Sine inverse
elif operator == "sin-1":
    product = asin(first_entry)

    #Continuing with operation
    continue_operation = True
    other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

    #If one wishes to continue with operations
    if other_operation == "y":

        #Operations continue in a loop unless terminated
        while continue_operation:

            operator3 = input("\nType an operation type ").lower()

            # Terminate the loop
            # returns the answer
            if operator3 == "=":
                # continue_operation = False
                print(f"\n= {product}")
                quit()

            third_entry = float(input("\nEnter number "))

            #Multiplying
            if operator3 == "x":
                product = product * third_entry

            #Dividing
            elif operator3 == "/":
                product = product / third_entry

            #Adding
            elif operator3 == "+":
                product = product + third_entry

            #Subtracting
            elif operator3 == "-":
                product = product - third_entry

            #Log operation
            elif operator3 == "log":
                product = log(product)

            #Exponential operation
            elif operator3 == "e":
                product = exp(product)

            #Sin operation
            elif operator3 == "sin":
                product = cosh(product)

            #Cosine operation
            elif operator3 == "cos":
                product = cos(product)

            #Coshine operation
            elif operator3 == "cosh":
                product = cosh(product)

            #Tan operation
            elif operator3 == "tan":
                product = tan(product)

            #Sin inverse
            elif operator3 == "sin-1":
                product = asin(product)

            #Cos inverse
            elif operator3 == "cos-1":
                product = acos(product)

            #Cosh inverse
            elif operator3 == "cosh-1":
                product = acosh(product)

            #Raising product to power n
            elif operator3 == "^":
                product = product ** third_entry

            #Square root of product
            elif operator3 == "rt":
                product = sqrt(product)

            #Multiplying product by pi
            elif operator3 == "pi":
                product = product * pi

            #Finding modulus of product
            elif operator3 == "%":
                product = product % third_entry

    print(f"\n= {product}")
    quit()

#Cosine operation
elif operator == "cos":
    product = cos(first_entry)

    #Continuing with operation
    continue_operation = True
    other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

    #If one wishes to continue with operations
    if other_operation == "y":

        #Operations continue in a loop unless terminated
        while continue_operation:

            operator3 = input("\nType an operation type ").lower()

            # Terminate the loop
            # returns the answer
            if operator3 == "=":
                # continue_operation = False
                print(f"\n= {product}")
                quit()

            third_entry = float(input("\nEnter number "))

            #Multiplying
            if operator3 == "x":
                product = product * third_entry

            #Dividing
            elif operator3 == "/":
                product = product / third_entry

            #Adding
            elif operator3 == "+":
                product = product + third_entry

            #Subtracting
            elif operator3 == "-":
                product = product - third_entry

            #Log operation
            elif operator3 == "log":
                product = log(product)

            #Exponential operation
            elif operator3 == "e":
                product = exp(product)

            #Sin operation
            elif operator3 == "sin":
                product = cosh(product)

            #Cosine operation
            elif operator3 == "cos":
                product = cos(product)

            #Coshine operation
            elif operator3 == "cosh":
                product = cosh(product)

            #Tan operation
            elif operator3 == "tan":
                product = tan(product)

            #Sin inverse
            elif operator3 == "sin-1":
                product = asin(product)

            #Cos inverse
            elif operator3 == "cos-1":
                product = acos(product)

            #Cosh inverse
            elif operator3 == "cosh-1":
                product = acosh(product)

            #Raising product to power n
            elif operator3 == "^":
                product = product ** third_entry

            #Square root of product
            elif operator3 == "rt":
                product = sqrt(product)

            #Multiplying product by pi
            elif operator3 == "pi":
                product = product * pi

            #Finding modulus of product
            elif operator3 == "%":
                product = product % third_entry

    print(f"\n= {product}")
    quit()

#Cosine inverse
elif operator == "cos-1":
    product = acos(first_entry)

    #Continuing with operation
    continue_operation = True
    other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

    #If one wishes to continue with operations
    if other_operation == "y":

        #Operations continue in a loop unless terminated
        while continue_operation:

            operator3 = input("\nType an operation type ").lower()

            # Terminate the loop
            # returns the answer
            if operator3 == "=":
                # continue_operation = False
                print(f"\n= {product}")
                quit()

            third_entry = float(input("\nEnter number "))

            #Multiplying
            if operator3 == "x":
                product = product * third_entry

            #Dividing
            elif operator3 == "/":
                product = product / third_entry

            #Adding
            elif operator3 == "+":
                product = product + third_entry

            #Subtracting
            elif operator3 == "-":
                product = product - third_entry

            #Log operation
            elif operator3 == "log":
                product = log(product)

            #Exponential operation
            elif operator3 == "e":
                product = exp(product)

            #Sin operation
            elif operator3 == "sin":
                product = cosh(product)

            #Cosine operation
            elif operator3 == "cos":
                product = cos(product)

            #Coshine operation
            elif operator3 == "cosh":
                product = cosh(product)

            #Tan operation
            elif operator3 == "tan":
                product = tan(product)

            #Sin inverse
            elif operator3 == "sin-1":
                product = asin(product)

            #Cos inverse
            elif operator3 == "cos-1":
                product = acos(product)

            #Cosh inverse
            elif operator3 == "cosh-1":
                product = acosh(product)

            #Raising product to power n
            elif operator3 == "^":
                product = product ** third_entry

            #Square root of product
            elif operator3 == "rt":
                product = sqrt(product)

            #Multiplying product by pi
            elif operator3 == "pi":
                product = product * pi

            #Finding modulus of product
            elif operator3 == "%":
                product = product % third_entry

    print(f"\n= {product}")
    quit()

#Tan operation
elif operator == "tan":
    product = tan(first_entry)

    #Continuing with operation
    continue_operation = True
    other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

    #If one wishes to continue with operations
    if other_operation == "y":

        #Operations continue in a loop unless terminated
        while continue_operation:

            operator3 = input("\nType an operation type ").lower()

            # Terminate the loop
            # returns the answer
            if operator3 == "=":
                # continue_operation = False
                print(f"\n= {product}")
                quit()

            third_entry = float(input("\nEnter number "))

            #Multiplying
            if operator3 == "x":
                product = product * third_entry

            #Dividing
            elif operator3 == "/":
                product = product / third_entry

            #Adding
            elif operator3 == "+":
                product = product + third_entry

            #Subtracting
            elif operator3 == "-":
                product = product - third_entry

            #Log operation
            elif operator3 == "log":
                product = log(product)

            #Exponential operation
            elif operator3 == "e":
                product = exp(product)

            #Sin operation
            elif operator3 == "sin":
                product = cosh(product)

            #Cosine operation
            elif operator3 == "cos":
                product = cos(product)

            #Coshine operation
            elif operator3 == "cosh":
                product = cosh(product)

            #Tan operation
            elif operator3 == "tan":
                product = tan(product)

            #Sin inverse
            elif operator3 == "sin-1":
                product = asin(product)

            #Cos inverse
            elif operator3 == "cos-1":
                product = acos(product)

            #Cosh inverse
            elif operator3 == "cosh-1":
                product = acosh(product)

            #Raising product to power n
            elif operator3 == "^":
                product = product ** third_entry

            #Square root of product
            elif operator3 == "rt":
                product = sqrt(product)

            #Multiplying product by pi
            elif operator3 == "pi":
                product = product * pi

            #Finding modulus of product
            elif operator3 == "%":
                product = product % third_entry

    print(f"\n= {product}")
    quit()

#Tan inverse
elif operator == "tan-1":
    product = atan(first_entry)

    #Continuing with operation
    continue_operation = True
    other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

    #If one wishes to continue with operations
    if other_operation == "y":

        #Operations continue in a loop unless terminated
        while continue_operation:

            operator3 = input("\nType an operation type ").lower()

            # Terminate the loop
            # returns the answer
            if operator3 == "=":
                # continue_operation = False
                print(f"\n= {product}")
                quit()

            third_entry = float(input("\nEnter number "))

            #Multiplying
            if operator3 == "x":
                product = product * third_entry

            #Dividing
            elif operator3 == "/":
                product = product / third_entry

            #Adding
            elif operator3 == "+":
                product = product + third_entry

            #Subtracting
            elif operator3 == "-":
                product = product - third_entry

            #Log operation
            elif operator3 == "log":
                product = log(product)

            #Exponential operation
            elif operator3 == "e":
                product = exp(product)

            #Sin operation
            elif operator3 == "sin":
                product = cosh(product)

            #Cosine operation
            elif operator3 == "cos":
                product = cos(product)

            #Coshine operation
            elif operator3 == "cosh":
                product = cosh(product)

            #Tan operation
            elif operator3 == "tan":
                product = tan(product)

            #Sin inverse
            elif operator3 == "sin-1":
                product = asin(product)

            #Cos inverse
            elif operator3 == "cos-1":
                product = acos(product)

            #Cosh inverse
            elif operator3 == "cosh-1":
                product = acosh(product)

            #Raising product to power n
            elif operator3 == "^":
                product = product ** third_entry

            #Square root of product
            elif operator3 == "rt":
                product = sqrt(product)

            #Multiplying product by pi
            elif operator3 == "pi":
                product = product * pi

            #Finding modulus of product
            elif operator3 == "%":
                product = product % third_entry

    print(f"\n= {product}")
    quit()

#Cosh operation
elif operator == "cosh":
    product = cosh(first_entry)

    #Continuing with operation
    continue_operation = True
    other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

    #If one wishes to continue with operations
    if other_operation == "y":

        #Operations continue in a loop unless terminated
        while continue_operation:

            operator3 = input("\nType an operation type ").lower()

            # Terminate the loop
            # returns the answer
            if operator3 == "=":
                # continue_operation = False
                print(f"\n= {product}")
                quit()

            third_entry = float(input("\nEnter number "))

            #Multiplying
            if operator3 == "x":
                product = product * third_entry

            #Dividing
            elif operator3 == "/":
                product = product / third_entry

            #Adding
            elif operator3 == "+":
                product = product + third_entry

            #Subtracting
            elif operator3 == "-":
                product = product - third_entry

            #Log operation
            elif operator3 == "log":
                product = log(product)

            #Exponential operation
            elif operator3 == "e":
                product = exp(product)

            #Sin operation
            elif operator3 == "sin":
                product = cosh(product)

            #Cosine operation
            elif operator3 == "cos":
                product = cos(product)

            #Coshine operation
            elif operator3 == "cosh":
                product = cosh(product)

            #Tan operation
            elif operator3 == "tan":
                product = tan(product)

            #Sin inverse
            elif operator3 == "sin-1":
                product = asin(product)

            #Cos inverse
            elif operator3 == "cos-1":
                product = acos(product)

            #Cosh inverse
            elif operator3 == "cosh-1":
                product = acosh(product)

            #Raising product to power n
            elif operator3 == "^":
                product = product ** third_entry

            #Square root of product
            elif operator3 == "rt":
                product = sqrt(product)

            #Multiplying product by pi
            elif operator3 == "pi":
                product = product * pi

            #Finding modulus of product
            elif operator3 == "%":
                product = product % third_entry

    print(f"\n= {product}")
    quit()

#Cosh inverse
elif operator == "cosh-1":
    product = acosh(first_entry)

    #Continuing with operation
    continue_operation = True
    other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

    #If one wishes to continue with operations
    if other_operation == "y":

        #Operations continue in a loop unless terminated
        while continue_operation:

            operator3 = input("\nType an operation type ").lower()

            # Terminate the loop
            # returns the answer
            if operator3 == "=":
                # continue_operation = False
                print(f"\n= {product}")
                quit()

            third_entry = float(input("\nEnter number "))

            #Multiplying
            if operator3 == "x":
                product = product * third_entry

            #Dividing
            elif operator3 == "/":
                product = product / third_entry

            #Adding
            elif operator3 == "+":
                product = product + third_entry

            #Subtracting
            elif operator3 == "-":
                product = product - third_entry

            #Log operation
            elif operator3 == "log":
                product = log(product)

            #Exponential operation
            elif operator3 == "e":
                product = exp(product)

            #Sin operation
            elif operator3 == "sin":
                product = cosh(product)

            #Cosine operation
            elif operator3 == "cos":
                product = cos(product)

            #Coshine operation
            elif operator3 == "cosh":
                product = cosh(product)

            #Tan operation
            elif operator3 == "tan":
                product = tan(product)

            #Sin inverse
            elif operator3 == "sin-1":
                product = asin(product)

            #Cos inverse
            elif operator3 == "cos-1":
                product = acos(product)

            #Cosh inverse
            elif operator3 == "cosh-1":
                product = acosh(product)

            #Raising product to power n
            elif operator3 == "^":
                product = product ** third_entry

            #Square root of product
            elif operator3 == "rt":
                product = sqrt(product)

            #Multiplying product by pi
            elif operator3 == "pi":
                product = product * pi

            #Finding modulus of product
            elif operator3 == "%":
                product = product % third_entry

    print(f"\n= {product}")
    quit()

#Pi operation
elif operator == "pi":
    product = pi(first_entry)

    #Continuing with operation
    continue_operation = True
    other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

    #If one wishes to continue with operations
    if other_operation == "y":

        #Operations continue in a loop unless terminated
        while continue_operation:

            operator3 = input("\nType an operation type ").lower()

            # Terminate the loop
            # returns the answer
            if operator3 == "=":
                # continue_operation = False
                print(f"\n= {product}")
                quit()

            third_entry = float(input("\nEnter number "))

            #Multiplying
            if operator3 == "x":
                product = product * third_entry

            #Dividing
            elif operator3 == "/":
                product = product / third_entry

            #Adding
            elif operator3 == "+":
                product = product + third_entry

            #Subtracting
            elif operator3 == "-":
                product = product - third_entry

            #Log operation
            elif operator3 == "log":
                product = log(product)

            #Exponential operation
            elif operator3 == "e":
                product = exp(product)

            #Sin operation
            elif operator3 == "sin":
                product = cosh(product)

            #Cosine operation
            elif operator3 == "cos":
                product = cos(product)

            #Coshine operation
            elif operator3 == "cosh":
                product = cosh(product)

            #Tan operation
            elif operator3 == "tan":
                product = tan(product)

            #Sin inverse
            elif operator3 == "sin-1":
                product = asin(product)

            #Cos inverse
            elif operator3 == "cos-1":
                product = acos(product)

            #Cosh inverse
            elif operator3 == "cosh-1":
                product = acosh(product)

            #Raising product to power n
            elif operator3 == "^":
                product = product ** third_entry

            #Square root of product
            elif operator3 == "rt":
                product = sqrt(product)

            #Multiplying product by pi
            elif operator3 == "pi":
                product = product * pi

            #Finding modulus of product
            elif operator3 == "%":
                product = product % third_entry

    print(f"\n= {product}")
    quit()

#Log to base 10
elif operator == "log":
    product = log10(first_entry)

    #Continuing with operation
    continue_operation = True
    other_operation = input("\nDo you want to continue with operation? Y or N ").lower()

    #If one wishes to continue with operations
    if other_operation == "y":

        #Operations continue in a loop unless terminated
        while continue_operation:

            operator3 = input("\nType an operation type ").lower()

            # Terminate the loop
            # returns the answer
            if operator3 == "=":
                # continue_operation = False
                print(f"\n= {product}")
                quit()

            third_entry = float(input("\nEnter number "))

            #Multiplying
            if operator3 == "x":
                product = product * third_entry

            #Dividing
            elif operator3 == "/":
                product = product / third_entry

            #Adding
            elif operator3 == "+":
                product = product + third_entry

            #Subtracting
            elif operator3 == "-":
                product = product - third_entry

            #Log operation
            elif operator3 == "log":
                product = log(product)

            #Exponential operation
            elif operator3 == "e":
                product = exp(product)

            #Sin operation
            elif operator3 == "sin":
                product = cosh(product)

            #Cosine operation
            elif operator3 == "cos":
                product = cos(product)

            #Coshine operation
            elif operator3 == "cosh":
                product = cosh(product)

            #Tan operation
            elif operator3 == "tan":
                product = tan(product)

            #Sin inverse
            elif operator3 == "sin-1":
                product = asin(product)

            #Cos inverse
            elif operator3 == "cos-1":
                product = acos(product)

            #Cosh inverse
            elif operator3 == "cosh-1":
                product = acosh(product)

            #Raising product to power n
            elif operator3 == "^":
                product = product ** third_entry

            #Square root of product
            elif operator3 == "rt":
                product = sqrt(product)

            #Multiplying product by pi
            elif operator3 == "pi":
                product = product * pi

            #Finding modulus of product
            elif operator3 == "%":
                product = product % third_entry


    print(f"\n= {product}")
    quit()

second_entry = float(input("\nEnter the second number "))

print(f"\n= {calculator(operator,first_entry, second_entry)}")
