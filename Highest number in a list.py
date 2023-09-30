my_list = [78, 45, 90, 47, 123, 345, 98, 456, 889]

highest_value = 0

for num in my_list:
    if num > highest_value:
        highest_value = num

print("Highest value =", highest_value)