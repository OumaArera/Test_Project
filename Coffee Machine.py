#OnA Cafe means Ouma n Arera Cafe
#The logo is curtesy of
# http://patorjk.com/software/taag/#p=display&f=Standard&t=OnA%20Cafe
logo = '''
 __        __   _                             _        
 \ \      / /__| | ___ ___  _ __ ___   ___   | |_ ___  
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \  | __/ _ \ 
   \ V  V /  __/ | (_| (_) | | | | | |  __/  | || (_) |
   _\_/\_/ \___|_|\___\___/|_| |_| |_|\___|   \__\___/ 
  / _ \ _ __    / \      / ___|__ _ / _| ___           
 | | | | '_ \  / _ \    | |   / _` | |_ / _ \          
 | |_| | | | |/ ___ \   | |__| (_| |  _|  __/          
  \___/|_| |_/_/   \_\   \____\__,_|_|  \___|          
                                                 
'''
print(logo)
print("\nEspresso = $1.50")
print("\nLatte = $2.50")
print("\nCappuccino = $3.00")
#Water and milk units in mililiters
#Coffee unit in in grams
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,

}

#We create a cash counter and assign it a variable
#At the begining it has zero dollars
cash = 0

making_coffee = True

#We create a while loop to ensure the machine continues serving after it is done
while making_coffee:

    user_input = input("\nWhat would you like today? (Espresso/ Latte/ Capuccino) ").lower()

    #off is a special code for maintainer to manage the machine
    #It is only the maintainer who is privy to this secret word
    #When it's promted, it shutts the machine down
    if user_input == "off":
        print("\nShutting down!")
        quit()
    #User has chosen Espresso
    elif user_input == "espresso":

        #We check if there are enough resources to make coffee
        if resources['water'] >= 50 and resources['coffee'] >= 18:

            #Since there are enough resources,
            #We process the transaction
            quarter = int(input("\nHow many Quarters do you have? "))
            dime = int(input("\nHow many Dimes do you have? "))
            nickel = int(input("\nHow many Nickels do you have? "))
            penny = int(input("\nHow many Pennies do you have? "))
            total = ((quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01))

            #User has enough money to buy Espresso
            if total == 1.50:

                #Calculate the user's change
                change = round((total -1.5), 2)

                #Print receipt
                print(f"\nRECEIPT\n\nReceived = ${total}\n\nChange = ${change}\n\nTOTAL = ${round((total - change), 2)}\n\nWelcome again!")

                #Add cash from user to our cash counter
                cash += total

                #Process Espresso
                resources['water'] = resources['water'] - 50
                resources['coffee'] = resources['coffee']- 18
                print("\nHere is your Espresso. Enjoy!")

            #User's money is above the money required to buy the espresso
            #We give change back the process thetransaction
            elif total > 1.50:

                #Calculate user's change
                change = round((total - 1.50), 2)

                #print receipt
                print(f"\nRECEIPT\n\nReceived = ${total}\n\nChange = ${change}\n\nTOTAL = ${round((total - change), 2)}\n\nWelcome again!")

                #Add cash to our cashh counter
                cash += 1.5

                #prepare Espresso
                resources['water'] = resources['water'] - 50
                resources['coffee'] = resources['coffee'] - 18
                print("\nHere is your Espresso. Enjoy!")

            #User has less money
            #we refund allow next user
            else:
                print(f"\nSorry that is not enough money! \n\n${total} refunded")


        #In this case we do not have enough water
        #We inform the user so and exit
        elif resources['water'] < 50:
            print(f"\nSorry there is not enough water! \n\nremaining water = {resources['water']}ml")
            quit()
        # In this case we do not have enough coffee
        # We inform the user so and exit
        elif resources['coffee'] < 18:
            print(f"\nSorry there is not enough coffee! \n\nremaining coffee = {resources['coffee']}g")
            quit()

    #User selected latte
    elif user_input == "latte":

        # We check if there are enough resources to make latte
        if resources['water'] >= 200 and resources['milk'] >=150 and resources['coffee'] >= 18:

            # Since there are enough resources,
            # We process the transaction
            quarter = int(input("\nHow many Quarters do you have? "))
            dime = int(input("\nHow many Dimes do you have? "))
            nickel = int(input("\nHow many Nickels do you have? "))
            penny = int(input("\nHow many Pennies do you have? "))
            total = ((quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01))

            # User has enough money to buy Espresso
            if total == 2.50:

                #We calculate the user's change if any
                change = round((total - 2.50), 2)

                #Print receipt
                print(f"\nRECEIPT\n\nReceived = ${total}\n\nChange = ${change}\n\nTOTAL = ${round((total - change), 2)}\n\nWelcome again!")

                #We add cash to our cash counter
                cash += total

                #We process Latte
                resources['water'] = resources['water'] - 200
                resources['milk'] = resources['milk'] - 150
                resources['coffee'] = resources['coffee'] - 24
                print("\nHere is your Latte.Enjoy!")

            # User's money is above the money required to buy the espresso
            # We give change back the process thetransaction
            elif total > 2.50:

                #We calculate user's change
                change =round ((total - 2.50), 2)

                #Print Receipt
                print(f"\nRECEIPT\n\nReceived = ${total}\n\nChange = ${change}\n\nTOTAL = ${round((total - change), 2)}\n\nWelcome again!")

                #Add cash to our cash counter
                cash += 2.5

                #Process Latte
                resources['water'] = resources['water'] - 200
                resources['milk'] = resources['milk'] - 150
                resources['coffee'] = resources['coffee'] - 24
                print("\nHere is your Latte. Enjoy!")

            # User has less money
            # we refund allow next user
            else:
                print(f"\nSorry that is not enough money! \n\n${total} refunded")


        # In this case we do not have enough water
        # We inform the user so and exit
        elif resources['water'] < 200:
            print(f"\nSorry there is not enough water! \n\nRemaining water = {resources['water']}ml")
            quit()

        # In this case we do not have enough milk
        # We inform the user so and exit
        elif resources['milk'] < 150:
            print(f"\nSorry there isnot enough milk! \n\nRemaining milk = {resources['milk']}ml")
            quit()

        # In this case we do not have enough coffee
        # We inform the user so and exit
        elif resources['coffee'] < 24:
            print(f"\nSorry there is not enough coffee! \n\nRemaining coffee = {resources['coffee']}g")
            quit()



    elif user_input == "cappuccino":

        # We check if there are enough resources to make cappuccino
        if resources['water'] >= 250 and resources['milk'] >= 150 and resources['coffee'] >= 18:

            # Since there are enough resources,
            # We process the transaction
            quarter = int(input("\nHow many Quarters do you have? "))
            dime = int(input("\nHow many Dimes do you have? "))
            nickel = int(input("\nHow many Nickels do you have? "))
            penny = int(input("\nHow many Pennies do you have? "))
            total = ((quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01))

            # User has enough money to buy Espresso
            if total == 3.00:

                #We calculate user's change if any
                change = round((total - 3.00), 2)

                #Print receipt
                print(f"\nRECEIPT\n\nReceived = ${total}\n\nChange = ${change}\n\nTOTAL = ${round((total - change), 2)}\n\nWelcome again!")

                #Add cash to our cash count
                cash += total

                #Process Cappuccino
                resources['water'] = resources['water'] - 250
                resources['milk'] = resources['milk'] - 100
                resources['coffee'] = resources['coffee'] - 24
                print("\nHere is your Cappuccino. Enjoy!")

            # User's money is above the money required to buy the espresso
            # We give change back the process thetransaction
            elif total > 3.0:

                #Calculate user's change
                change = round((total - 3.00), 2)

                #Print receipt
                print(f"\nRECEIPT\n\nReceived = ${total}\n\nChange = ${change}\n\nTOTAL = ${round((total - change), 2)}\n\nWelcome again!")

                #Add cash to our cash counter
                cash += 3.00

                #Process Cappuccino
                resources['water'] = resources['water'] - 250
                resources['milk'] = resources['milk'] - 100
                resources['coffee'] = resources['coffee'] - 24
                print("\nHere is your Cappuccino. Enjoy!")

            # User has less money
            # we refund allow next user
            else:
                print(f"\nSorry that is not enough money! \n\n${total} refunded")


        # In this case we do not have enough water
        # We inform the user so and exit
        elif resources['water'] < 250:
            print(f"\nSorry there is not enough water! \n\nRemaining water = {resources['water']}ml")
            quit()

        # In this case we do not have enough milk
        # We inform the user so and exit
        elif resources['milk'] < 100:
            print(f"\nSorry there isnot enough milk! \n\nRemaining milk = {resources['milk']}ml")
            quit()

        # In this case we do not have enough coffee
        # We inform the user so and exit
        elif resources['coffee'] < 24:
            print(f"\nSorry there is not enough coffee! \n\nRemaining coffee = {resources['coffee']}g")
            quit()

    #This too is a special code for the maintainer of the machine
    # to replenish the machine or check the amount of money the
    #machine has collected
    elif user_input == "report":
        print(f"\nWater = {resources['water']}ml")
        print(f"\nMilk = {resources['milk']}ml")
        print(f"\nCoffee = {resources['coffee']}g")
        print(f"\nCash = ${cash}")

    #User enters something strange
    else:
        print("\nSorry I don't have that for now! \n\nKindly look up at our menu.")