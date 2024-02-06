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

def flip_coin():
    random_num = random.randint (1,2)
    if random_num == 1:
        side = "Heads"
    else:
        side = "Tails"
    return side

user_choice = input ("Choose Heads or Tails: ")
result=flip_coin()
print(f"Computers flip: " + str(result))

if result == user_choice:
    print("You win!")
else:
    print("You lose!")


