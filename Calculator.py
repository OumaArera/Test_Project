#This calculator does operations of not more than two entries

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

#We define the function
def calculator(symbol,entry1, entry2):
    '''
    Calculator takes the two entries and work out the operation
    '''

    if symbol == "x":
        product = entry1 * entry2
        return product

    #Dividing
    elif symbol == "/":
        product = entry1 / entry2
        return product

    #Adding
    elif symbol == "+":
        product = entry1 + entry2
        return product

    #Subtracting
    elif symbol == "-":
        product = entry1 - entry2
        return product

    #Raising to power
    elif symbol == "^":
        product = entry1 ** entry2
        return product
    elif symbol == "nrt":
        product = entry1 ** (1/entry2)
        return product

    elif symbol == "|":
        product = entry1 % entry2
        return product

    elif symbol == "logn":
        product = log(entry1,entry2)
        return product



first_entry = int(input("\nEnter the first value: "))

#Operation symbol
operator = input("\nSelect symbol, x,/, +, -, ^, rt, !, e, nrt, cos, cosh, sin, tan, pi, %, |, log, logn, sin-1, cos-1, tan-1, cosh-1: ").lower()

#checking for square root
if operator == "rt":
    square_root =sqrt(first_entry)
    print(f"\n= {square_root}")
    quit()

#checking if it is factorial
elif operator == "!":
    fact = factorial(first_entry)
    print(f"\n= {fact}")
    quit()

#Exponential
elif operator == "e":
    product = exp(first_entry)
    print(f"\n= {product}")
    quit()

#Sin operation
elif operator == "sin":
    product = sin(first_entry)
    print(f"\n= {product}")
    quit()

#Sine inverse
elif operator == "sin-1":
    product = asin(first_entry)
    print(f"\n= {product}")
    quit()

#Cosine operation
elif operator == "cos":
    product = cos(first_entry)
    print(f"\n= {product}")
    quit()

#Cosine inverse
elif operator == "cos-1":
    product = acos(first_entry)
    print(f"\n= {product}")
    quit()

#Tan operation
elif operator == "tan":
    product = tan(first_entry)
    print(f"\n= {product}")
    quit()

#Tan inverse
elif operator == "tan-1":
    product = atan(first_entry)
    print(f"\n= {product}")
    quit()

#Cosh operation
elif operator == "cosh":
    product = cosh(first_entry)
    print(f"\n= {product}")
    quit()

#Cosh inverse
elif operator == "cosh-1":
    product = acosh(first_entry)
    print(f"\n= {product}")
    quit()

#Pi operation
elif operator == "pi":
    product = pi(first_entry)
    print(f"\n= {product}")
    quit()

#Log to base 10
elif operator == "log":
    product = log10(first_entry)
    print(f"\n= {product}")
    quit()

second_entry = int(input("\nEnter the second number"))


print(f" = {calculator(operator,first_entry, second_entry)}")
