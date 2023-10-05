#This is my game logo
#Credit to http://patorjk.com/software/taag/#p=display&f=Dancing%20Font&t=Number%20Guess

logo = """  
  _   _       _   _   __  __     ____  U _____ u   ____           ____     _   _ U _____ u ____    ____     
 | \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u     U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u  
<|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/     \| |  _ / \| |\| | |  _|" <\___ \/<\___ \/   
U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <        | |_| |   | |_| | | |___  u___) | u___) |   
 |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\        \____|  <<\___/  |_____| |____/>>|____/>>  
 ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_       _)(|_  (__) )(   <<   >>  )(  (__))(  (__) 
 (_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__)     (__)__)     (__) (__) (__)(__)    (__)                                                    
"""

print(logo)

#Player makes a bid
print("\nWelcome to Number Guess. Make a bid!")

import random

#Player chooses the level of the game
game_level = input("\nChoose a level to play. 'Easy', 'Hard', 'Expert' ").lower()

#For the easy level there are rules here to adhere to
#1. Your range must not be less than 99 numbers
#2. You only have 10 guesses to make
##. The winner gets two times their bid
if game_level == "easy":

    print("\nYou got 10 attempts to play!")

    starting_number = int(input("\nEnter the lower limit: "))

    ending_number = int(input("\nEnter the upper limit: "))

    def easy_game():
        '''
        Takes the parameters of the easy game and determine if player wins or loses
        '''

        #Computer will pick a random number and we ask the player to guess it
        random_number = random.randint(starting_number, ending_number+1)

        guess = int(input("\nGuess the lucky number: "))

        #The case where the player guess is equal to the random number
        #the player win
        if guess == random_number:
            print(f"\nYou got the lucky number {random_number} in 1 attempt.")
            quit()

        #Player did not get the number but they are above the lucky number
        elif guess > random_number:
            print("\nYou went over!")

        #Player did not get the lucky number but they are below the lucky number
        elif guess < random_number:
            print("\nYou went below")

        #We set the number of game tries to 0
        game_tries = 0

        #We create a while loop in the case they did not get the lucky number
        #Since the player already made a guess, he is remaining with 9 chances of guessing
        while guess != random_number and game_tries < 9:

            #The player makes another guess
            another_guess = int(input("\nGuess another lucky number: "))

            #The player's next choice is equal to thelucky number so they win
            if another_guess == random_number:
                game_tries += 1
                print(f"\nYou got the lucky number {random_number} in {game_tries + 1} attempts.")
                quit()

            #Player's next choice is not the lucky number and is above the lucky number
            #We also check if the number of tries == 9
            #if so we end the game and display the lucky number
            elif another_guess > random_number:
                game_tries += 1
                print("\nYour guess went over!")
                if game_tries == 9:
                    print(f"\nYou lost! Lucky number was {random_number}")
                    quit()
                print(f"\nYou have {9 - game_tries} guesses left!")

            # Player's next choice is not the lucky number and is below the lucky number
            # We also check if the number of tries == 9
            # if so we end the game and display the lucky number
            elif another_guess < random_number:
                game_tries += 1
                print("\nYour guess went below!")
                if game_tries == 9:
                    print(f"\nYou lost! Lucky number was {random_number}")
                    quit()
                print(f"\nYou have {9 - game_tries} guesses left!")

    easy_game()

#For the easy level there are rules here to adhere to
#1. Your range must not be less than 50 numbers
#2. You only have 5 guesses to make
##. The winner gets three times their bid
elif game_level == "hard":
    starting_number = int(input("\nEnter the lower limit: "))

    ending_number = int(input("\nEnter the upper limit: "))

    def hard_game():
        '''
        This function runs thehard game and determine if player wins or lose
        '''

        random_number = random.randint(starting_number, ending_number + 1)

        guess = int(input("\nGuess the lucky number: "))
        if guess == random_number:
            print(f"\nYou got the lucky number {random_number} in 1 attempt.")
            quit()

        elif guess > random_number:
            print("\nYou went over!")

        elif guess < random_number:
            print("\nYou went below")

        game_tries = 0

        while guess != random_number and game_tries < 4:

            another_guess = int(input("\nGuess another lucky number: "))

            if another_guess == random_number:
                game_tries += 1
                print(f"\nYou got the lucky number {random_number} in {game_tries + 1} attempts.")
                quit()

            elif another_guess > random_number:
                game_tries += 1
                print("\nYour guess went over!")
                if game_tries == 4:
                    print(f"\nYou lost! Lucky number was {random_number}")
                    quit()
                print(f"\nYou have {4 - game_tries} guesses left!")

            elif another_guess < random_number:
                game_tries += 1
                print("\nYour guess went below!")
                if game_tries == 4:
                    print(f"\nYou lost! Lucky number was {random_number}")
                    quit()
                print(f"\nYou have {4 - game_tries} guesses left!")

    hard_game()

#For the easy level there are rules here to adhere to
#1. Your range must not be less than 10 numbers
#2. You only have 3 guesses to make
##. The winner gets three and half times their bid
elif game_level == "expert":

    starting_number = int(input("\nEnter the lower limit: "))

    ending_number = int(input("\nEnter the upper limit: "))


    def expert_game():
        '''
        Function runs the expert game and determine if player is lucky or not
        '''

        random_number = random.randint(starting_number, ending_number + 1)

        guess = int(input("\nGuess the lucky number: "))
        if guess == random_number:
            print(f"\nYou got the lucky number {random_number} in 1 attempt.")
            quit()

        elif guess > random_number:
            print("\nYou went over!")

        elif guess < random_number:
            print("\nYou went below")

        game_tries = 0

        while guess != random_number and game_tries < 2:

            another_guess = int(input("\nGuess another lucky number: "))

            if another_guess == random_number:
                game_tries += 1
                print(f"\nYou got the lucky number {random_number} in {game_tries + 1} attempts.")
                quit()

            elif another_guess > random_number:
                game_tries += 1
                print("\nYour guess went over!")
                if game_tries == 2:
                    print(f"\nYou lost! Lucky number was {random_number}")
                    quit()
                print(f"\nYou have {2 - game_tries} guesses left!")

            elif another_guess < random_number:
                game_tries += 1
                print("\nYour guess went below!")
                if game_tries == 2:
                    print(f"\nYou lost! Lucky number was {random_number}")
                    quit()
                print(f"\nYou have {2 - game_tries} guesses left!")

    expert_game()
