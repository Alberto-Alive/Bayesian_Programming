# from pyplpath import *
# # import all
# from pypl import *

# # define a probabilistic variable
# dice= plSymbol("Dice", plIntegerType(1,6))

# #define a way to adress the values
# dice_value = plValues(dice)

# # define a uniform probability distribution on the variable
# P_dice = plUniform(dice)

# # print it
# print('P_dice =', P_dice)


# # perform two random draws with the distribution
# # and print the result
# for i in range(2):
#     P_dice.draw(dice_value)
#     print(i+1, 'th throw', dice_value)



import random

dice_vals = range(1, 7)

def draw_dice():
    """ simulate dice draw"""
    return random.choice(dice_vals)


# draw twice

for n in range(2):
    value = draw_dice()
    print(f"{n+1}th throw: {value}")