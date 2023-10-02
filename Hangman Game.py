#Welcoming the player
#Stating the rules of the game
name = input("What is your name? ")
print(f"\nWelcome {name} to the Hangman Game! \nSo this morning I was at the farm. I collected a basket full of different fruits. \nNow I want to share these juicy fruits with you so that we can enjoy munching them! \nBut then we will have to play a game called Hangman.\n\n")
print("Now literally you will be guessing the name of the fruit I will pick from the basket. \nI will tell you the first and last letter in the name then you fill the rest by yourself. \nBut I won't show you the fruit. If you make seven wrong guesses, you lose!\n\n")
print("I'm so excited to play with you! Let's go!\n\n")

import random


#List of names that a random word will come from
word_list = ["Apple", "Banana", "Cherry", "Grapefruit", "Blueberry", "Coconut", "Grapes", "Guava", "Jackfruit", "Orange", "Lemon", "Avocado", "Mango", "Papaya", "Passion", "Pineapple", "Watermelon","Pears"]

#A random word
chosen_word = random.choice(word_list)

#Converting chosen_word to lower cases
random_word = chosen_word.lower()

if chosen_word == "Apple":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Banana":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Cherry":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Grapefruit":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Blueberry":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Coconut":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Grapes":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Guava":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Jackfruit":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Orange":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Lemon":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Avocado":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Mango":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Papaya":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Passion":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Pineapple":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Watermelon":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")

elif chosen_word == "Pears":
    print(f"It starts with {chosen_word[0]} and ends with {chosen_word[-1]}")


#We set the guessed word at an empty string
guessed_word = []

#We assign the length of chosen word a different variable
word_length = len(chosen_word)

#Checking if the length of chosen word is equal to that of guessed word
#As long as they are not equal, we append "_" to the list
while len(chosen_word) != len(guessed_word):
    guessed_word.append("_")

#Setting the count entry to zero
life = 0

#Checkinf if the chosen word is same as guessed word
#AS long as they are not equal, we keep running the loop
while random_word != guessed_word:

    # Checking if "_" is still in guessed word
    # Literally saying that guessed is equal to chosen word
    # At this point we end the game and announce the winner
    #The loop stops running
    if "_" not in guessed_word:
        print("\nEnd of game! You won!")
        quit()

    #Since guessed word is not equal to chosen word,
    #We make a guess

    guess = input("\nGuess a letter in the random word.(Please make your entries in samll letters): ")

    #Checking if the player's guess is in the chosen word
    #if it is not, we retun an error and count the entry
    if guess not in random_word:
        print(f"\nYour guess of {guess} is wrong! You lose a life!\n")
        life += 1


    if guess in guessed_word:
        print(f"\nYou already picked {guess}, pick another letter\n")

    #Setting count at 7 means head, neck, two hands, trunk, and two legs.
    #So each time the player picks a wrong letter, part of the body above is formed on the hanger
    #At 7 all the body is formed and our guy is hanged
    if life == 7:
        print("You hanged our guy! You lost!")
        quit()

    for position in range(word_length):

        #we assign letter to the position in the chosen word if the guess is equal to letter
        letter = random_word[position]
        if guess == letter:
            guessed_word[position] = letter #appending the letter at the position

    print(f"\n{guessed_word}")


