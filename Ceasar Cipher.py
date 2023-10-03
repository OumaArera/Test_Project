# Alphabet is the pool where the code picks letters
# I have repeated the entries to escape the list out of range error

alphabet = [" ", "'", "?", ",", ".", "!", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
            "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "'", "?", ",", ".", "!", "a", "b", "c", "d",
            "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
            "z"]
game_on = True
#We keep running the game
# while game_on:

# This line helps to find out if one wants to encrypt or decrypt
direction = input("Type 'encode' if you're encrypting and 'decode' when decrypting \n")

# Message
text = input("Enter your massage \n").lower()

# This is the shifting amount
shift = int(input("Type the shift number \n"))
shift = shift % 32


# The function
def encrypt(my_text, my_shift):
    # We create an empty crypted and decrypted message
    encrypted_message = ""
    decrypted_message = ""

    # Checking if one wants to encrypt
    if direction.lower() == "encode":

        # Checking for the characters in text
        for char in my_text:

            # Checking if the entered character is in the alphabet
            # Incase it is not in the list, we maintain them without shifting
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + my_shift

                # Adding the character to empty encrypted_message
                encrypted_message += alphabet[new_position]

            else:
                encrypted_message += char

        print(f"Your encrypted message is '{encrypted_message}'.")

    # Checking if one wants to encrypt
    elif direction.lower() == "decode":

        # Checking for the characters in text
        for char in my_text:

            # Checking if the entered character is in the alphabet
            # Incase it is not in the list, we maintain them without shifting
            if char in alphabet:

                position = alphabet.index(char)
                new_position = position - my_shift
                decrypted_message += alphabet[new_position]
                decrypted_message = decrypted_message.capitalize()

            else:
                decrypted_message += char

        print(f"Your decrypted message is '{decrypted_message}'.")

# continue_game = input("Type Yes if you want to continue playing and No if you want to exit ").lower()
# if continue_game == "no":
#     game_on = False
#     print("Game finished!")


encrypt(text, shift)

