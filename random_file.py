import random

# random_integer = random.randint(1, 100)
#
# print(random_integer)

# sides = int(input("How many sides does the die have?"))
# random_integer = random.randint(1, sides)
#
# print('You rolled a {}'.format(random_integer))

#Creating coin flip exercise

#if random coin flip matches choice input by the user then they win
#otherwise if random coin flip does not match choice input by user they lose
#
# def flip_coin():
#     random_num = random.randint (1,2)
#     if random_num == 1:
#         side = "Heads"
#     else:
#         side = "Tails"
#     return side
#
# user_choice = input ("Choose Heads or Tails: ")
# result=flip_coin()
# print(f"Computers flip: " + str(result))
#
# if result == user_choice:
#     print("You win!")
# else:
#     print("You lose!")

# This program simulates rock, paper, scissors. The rst winning condition has been
# added.
# To nish the program you'll need to add all of the other winning and losing conditions.

import random
def random_choice():
    choice_number = random.randint(1, 3)
    if choice_number == 1:
        choice = 'rock'
    elif choice_number == 2:
        choice = 'scissors'
    else:
        choice = 'paper'
    return choice
my_choice = input('Choose rock, scissors or paper: ')
opponent_choice = random_choice()

print('Your opponent chose {}'.format(opponent_choice))

if my_choice == 'rock' and opponent_choice == 'scissors':
    print('You win!')
elif my_choice == 'rock' and opponent_choice == 'paper':
    print('You Win!')
elif my_choice == 'paper' and opponent_choice == 'rock':
    print("You Win!")
elif my_choice == 'paper' and opponent_choice == 'scissors':
    print("You lose!")
elif my_choice == 'scissors' and opponent_choice == 'paper':
    print("You Win!")
elif my_choice == 'scissors' and opponent_choice == 'rock':
    print("You lose!")
else:
    print("It's a draw")

