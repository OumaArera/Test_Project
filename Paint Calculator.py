from math import ceil


def paint_calc(height, width, cover):
    num_cans = (height * width) / cover

    num_cans = ceil(num_cans)
    print(f"\nYou'll need {num_cans} cans of paint")


test_h = int(input("Enter height "))  # Height of wall (m)
test_w = int(input("Enter width "))  # Width of wall (m)
coverage = 5

paint_calc(test_h, test_w, coverage)
