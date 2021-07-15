import random

# for i in range(3):

#     print(random.random())
#     print(random.randint(10, 20))  # generates a random value between 0 to 1


# # randomly picking item from list
# # list of team memebers and randomly pick someone the team leader
# memebers = ["Ricardo", "Mosh", "Josh"]
# leader = random.choice(memebers)
# print(leader)


# write a program to roll a dice. everytime you roll the dice u get different values.

# dice1 = random.randint(1, 7)
# dice2 = random.randint(1, 7)

# print(f"({dice1}, {dice2})")

# start by importing random  module at top. we define a class called dice. we want to have a method called roll. in this method we want two random values from 1-6. so we have two variables. we need to return them in a tuple. in python when returning a tuple from a function, you dont have to add a ()........ now we create an object of this type. dice = Dice().... next we roll the dice and print result


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())