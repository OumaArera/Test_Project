from random import shuffle

start_game = input("Do you want to play? Y or N: ").lower()

if start_game == "n":
    print("End of game!")
    quit()

else:
    print("Wrong pick! Type Y or N")

end_game = False


while not end_game and start_game == "y":

    cards = [
        11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10
    ]


    shuffle(cards)

    shuffled_cards = cards

    print(f"Cards after shuffling.\n{shuffled_cards}")

    player_cards = []

    dealer_cards = []

    player_cards.append(shuffled_cards[-1])

    dealer_cards.append(shuffled_cards[-2])

    player_cards.append(shuffled_cards[-3])

    dealer_cards.append(shuffled_cards[-4])

    del shuffled_cards[48:]

    remain_cards = shuffled_cards

    print(f"\nCurrent list. \n{remain_cards}")

    print(f"\nDealer cards = {dealer_cards[0]}")

    print(f"\nYour cards = {player_cards}")


    sum_of_player = sum(player_cards)

    sum_of_dealer = sum(dealer_cards)


    if sum_of_player == 21:
        print(f"\nPlayer cards = {player_cards}")
        print(f"\nDealer cards = {dealer_cards}")
        print("\nBlack Jack! Player win!")
        quit()

    elif sum_of_dealer == 21:
        print(f"\nPlayer cards = {player_cards}")
        print(f"\nDealer cards = {dealer_cards}")
        print("\nBlack Jack! Player lose!")
        quit()

    elif sum_of_dealer > 21:

        print(f"\nPlayer cards = {player_cards}")
        print(f"\nDealer cards = {dealer_cards}")
        print("\nBUST! Player wins!")
        quit()

    elif sum_of_player > 21:
        print(f"\nPlayer cards = {player_cards}")
        print(f"\nDealer cards = {dealer_cards}")
        print("\nBUST! Player lose!")
        quit()

    elif sum_of_player > 21 and 11 in player_cards and (sum_of_player - 10) > 21:
        print(f"\nPlayer cards = {player_cards}")
        print(f"\nDealer cards = {dealer_cards}")
        print("\nBUST! Player lose!")
        quit()

    elif sum_of_player > 21 and 11 not in player_cards:
        print(f"\nPlayer cards = {player_cards}")
        print(f"\nDealer cards = {dealer_cards}")
        print("\nBUST! Player lose!")
        quit()

    game_on = True

    while game_on and sum_of_player < 21:

        play_on = input("\nDo you want to play? Hit or Stay: ").lower()

        if play_on == "hit":

            new_card = remain_cards.pop()
            player_cards.append(new_card)
            sum_of_player += new_card
            print(f"\nYour cards = {player_cards}")

            if sum_of_player == 21:
                print(f"\nPlayer cards = {player_cards}")
                print(f"\nDealer cards = {dealer_cards}")
                print("\nBlack Jack! Player win!")
                quit()

            elif sum_of_dealer == 21:
                print(f"\nPlayer cards = {player_cards}")
                print(f"\nDealer cards = {dealer_cards}")
                print("\nBlack Jack! Player lose!")
                quit()

            elif sum_of_player > 21 and 11 in player_cards and (sum_of_player - 10) > 21:
                print(f"\nPlayer cards = {player_cards}")
                print(f"\nDealer cards = {dealer_cards}")
                print("\nBUST! Player lose!")
                quit()

            elif sum_of_player > 21 and 11 not in player_cards:
                print(f"\nPlayer cards = {player_cards}")
                print(f"\nDealer cards = {dealer_cards}")
                print("\nBUST! Player lose!")
                quit()

            elif sum_of_player > 21 and 11 in player_cards and (sum_of_player - 10) < 21:
                game_on = True


        elif play_on == "stay":

            new_card = remain_cards.pop()
            dealer_cards.append(new_card)
            sum_of_dealer += new_card


            while sum_of_dealer < 17:
                new_card = remain_cards.pop()
                dealer_cards.append(new_card)
                sum_of_dealer += new_card

            if sum_of_dealer > 21:
                print(f"\nPlayer cards = {player_cards}")
                print(f"\nDealer cards = {dealer_cards}")
                print("\nBUST! Player win!")
                quit()

            elif sum_of_dealer > 17 and sum_of_dealer <= 21 and sum_of_dealer > sum_of_player:
                print(f"\nPlayer cards = {player_cards}")
                print(f"\nDealer cards = {dealer_cards}")
                print("\nPlayer lose!")
                quit()

            elif sum_of_dealer > 17 and sum_of_dealer <= 21 and sum_of_dealer < sum_of_player:
                print(f"\nPlayer cards = {player_cards}")
                print(f"\nDealer cards = {dealer_cards}")
                print("\nPlayer win!")
                quit()

            elif sum_of_dealer > 17 and sum_of_dealer <= 21 and sum_of_dealer == sum_of_player:
                print(f"\nPlayer cards = {player_cards}")
                print(f"\nDealer cards = {dealer_cards}")
                print("\nDraw!")
                quit()

        else:
            print("\nWrong pick! Type Hit or Stay")

    game_on = True
    while game_on and sum_of_player > 21 and 11 in player_cards and (sum_of_player - 10) < 21 :

        play_on = input("\nDo you want to play? Hit or Stay: ").lower()

        if play_on == "hit":
            new_card = remain_cards.pop()
            player_cards.append(new_card)
            sum_of_player += new_card
            print(f"\nYour cards = {player_cards}")

            if sum_of_player == 21:
                print(f"\nPlayer cards = {player_cards}")
                print(f"\nDealer cards = {dealer_cards}")
                print("\nBlack Jack! Player win!")
                quit()

            elif sum_of_dealer == 21:
                print(f"\nPlayer cards = {player_cards}")
                print(f"\nDealer cards = {dealer_cards}")
                print("\nBlack Jack! Player lose!")
                quit()

            elif sum_of_player > 21 and 11 in player_cards and (sum_of_player - 10) > 21:
                print(f"\nPlayer cards = {player_cards}")
                print(f"\nDealer cards = {dealer_cards}")
                print("\nBUST! Player lose!")
                quit()

            elif sum_of_player > 21 and 11 not in player_cards:
                print(f"\nPlayer cards = {player_cards}")
                print(f"\nDealer cards = {dealer_cards}")
                print("\nBUST! Player lose!")
                quit()

            elif sum_of_player > 21 and 11 in player_cards and (sum_of_player - 10) < 21:
                game_on = True


        elif play_on == "stay":

            new_card = remain_cards.pop()
            dealer_cards.append(new_card)
            sum_of_dealer += new_card


            while sum_of_dealer < 17:
                new_card = remain_cards.pop()
                dealer_cards.append(new_card)
                sum_of_dealer += new_card

            if sum_of_dealer > 21:
                print(f"\nPlayer cards = {player_cards}")
                print(f"\nDealer cards = {dealer_cards}")
                print("\nBUST! Player win!")
                quit()

            elif sum_of_dealer > 17 and sum_of_dealer <= 21 and sum_of_dealer > sum_of_player:
                print(f"\nPlayer cards = {player_cards}")
                print(f"\nDealer cards = {dealer_cards}")
                print("\nPlayer lose!")
                quit()

            elif sum_of_dealer > 17 and sum_of_dealer <= 21 and sum_of_dealer < sum_of_player:
                print(f"\nPlayer cards = {player_cards}")
                print(f"\nDealer cards = {dealer_cards}")
                print("\nPlayer win!")
                quit()

            elif sum_of_dealer > 17 and sum_of_dealer <= 21 and sum_of_dealer == sum_of_player:
                print(f"\nPlayer cards = {player_cards}")
                print(f"\nDealer cards = {dealer_cards}")
                print("\nDraw!")
                quit()

        else:
            print("\nWrong pick! Type Hit or Stay")


    if sum_of_player == sum_of_dealer:
        print(f"\nPlayer cards = {player_cards}")
        print(f"\nDealer cards = {dealer_cards}")
        print("\nDraw!")
        quit()

    print(f"\nSum of player cards = {sum_of_player}")

    print(f"\nSum of dealer cards =  is {sum_of_dealer}")

