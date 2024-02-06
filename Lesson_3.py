#Budget of £10, write a program to decide which burger
#restaurant to go to

#input price of burger

burger_price= input("How much is the burger?")

veg_option =input("Is there a vegetarian option? y/n: " )


budget = float(burger_price) <=10
veg = veg_option == "y"

is_good_choice = budget and veg

#print(f'Your burger is within the budget: {budget} and is vegetarian = {veg_option}')
print('Restaurant meets criteria: {}'.format(is_good_choice))


#new_exercise

mars_choice= input('Would you like to visit Mars? y/n: ')
is_willing = mars_choice == 'y'

affordable =input('Can you afford to visit Mars y/n: ')
can_afford = affordable == 'y'

should_visit_mars = is_willing and can_afford

print(f'You should visit Mars: {should_visit_mars}')