#Treasure Island game

print("Welcome to Treasure Island! \nYour mission is to find the treasure! Let's go!")

choice1 = input("Choose a side either 'right' or 'left': ")
if choice1.lower() == "left":
    print("You're stranded by Lake Lolwe and you need to cross to the Island. \nYou can either choose to swim or wait for a boat. It's all up to you!")
    choice2 = input("Choose between 'swim' and 'wait': ")
    if choice2.lower() == "wait":
        print("You have successfully crossed the lake and you're now at the door! \nYou need to choose between three colours: 'red', 'blue' or 'yellow'!")
        choice3 = input("Choose a colour: 'red', 'blue', 'yellow': ")
        if choice3.lower() == "yellow":
            print("Hurray! You have won! The treasure is yours!")
        elif choice3.lower() == "red":
            print("You have been burned by raging fires! Game over!")
        else:
            print("You have been devoured by beasts! Game Over!")
    else:
        print("You have been attacked by trout! Game over!")
else:
    print("You fell into a ditch! Gme over!")