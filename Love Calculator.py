#Entering the two names

lover_name = input("What is your lover's name? ")
your_name = input("What is uour name? ")

combine_name = lover_name + your_name

#total name length
total_name_length = len(combine_name .replace(" ", ""))

#counting the number of times true appear in the combined name
total_love_count = 0

t = combine_name .upper().count('T')
total_love_count += t

r = combine_name .upper().count('R')
total_love_count += r

u = combine_name .upper().count('U')
total_love_count += u

e = combine_name .upper().count('E')
total_love_count += e


#counting the number of times love appear in the combined name
l = combine_name .upper().count('L')
total_love_count += l

o = combine_name .upper().count('O')
total_love_count += o

v = combine_name .upper().count('V')
total_love_count += v

e = combine_name .upper().count('E')
total_love_count += e



percentage_love = round(((total_love_count / total_name_length) * 100), 2)

#Checking if percentage of love is less than 10 or greater than 90

if percentage_love < 10 or percentage_love > 90:
    print(f"your score is {percentage_love}%, you go together like coke and mentos!")

#Checking if percentage of love is between 40 and 50
elif percentage_love > 40 and percentage_love <50:
    print(f"Your score is {percentage_love}%, and you're alright together!")

else:
    print(f"Your score is {percentage_love}%")

