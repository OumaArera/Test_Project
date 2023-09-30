#we first import random
#create a random number between 0 and 1 where 1 is head and 0 is tail
import random
random_number = random.randint(0,1)
print(f"Random number is {random_number}")
if random_number == 1:
    print("Head!")

else:
    print("Tail!")