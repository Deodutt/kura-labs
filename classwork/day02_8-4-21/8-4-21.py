# hello = "hello"  # String literals can use single quotes
# world = "world"  # or double quotes; it does not matter
# fname = "Ricardo"  # or double quotes; it does not matter
# print(hello, len(hello))
# # print(fname, len(fname))

# print(f"{fname} {len(fname)}")


# user_first_name = input("What is your first name? ")
# user_last_name = input("What is your last name? ")
# print(f"Your name is {user_first_name} {user_last_name}")


# s = "hello"
# print(s.capitalize())  # Capitalize a string
# print(s.upper())  # Convert a string to uppercase; prints "HELLO"
# print(s.rjust(7))  # Right-justify a string, padding with spaces
# print(s.center(7))  # Center a string, padding with spaces

# print(s.replace("l", "(ell)"))  # Replace all instances of one substring with another
# Basically where you see an L, it will replace it with (ell)


# print("  world ".strip())  # Strip leading and trailing whitespace


# Follow along CLASS WORK

# 1) Ask for the user’s first name and display the output message Hello [First Name] .
# user_first_name = input("What is your first name? ")
# print(f"Hello {user_first_name}")

# 2) Ask for the user’s first name and then ask for their surname and display the output message Hello [First Name] [Surname].
# user_first_name = input("What is your first name? ")
# user_surname_name = input("What is your surname(last) name? ")
# print(f"Hello {user_first_name} {user_surname_name}")


# 3) Write code that will display the joke “What do you call a bear with no teeth?” and on the next line display the answer “A gummy bear!” Try to create it using only one line of code.
# print(f"What do you call a bear with no teeth? \nA gummy bear!")


# 4) Ask the user to enter two numbers. Add them together and display the answer as The total is [answer].
# first_number = int(input("Please enter the first number "))
# second_number = int(input("Please enter the second number "))
# ## total = first_number + second_number
# print(f"The total is {first_number + second_number}")

# 5) Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third. Display the answer as The answer is [answer].
# first_number = int(input("Please enter the first number "))
# second_number = int(input("Please enter the second number "))
# third_number = int(input("Please enter the third number "))

# print(f"The answer is {(first_number + second_number) * third_number}")


# 6) Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left and display the answer in a user friendly format.

# starer = int(input("How many slices of pizza did you start with? "))
# ate = int(input("How many slices of pizza have you ate so far? "))
# print(f"There is a total of {starer - ate} slices of pizza left!!")


# 7) Ask the user for their name and their age. Add 1 to their age and display the output [Name] next birthday you will be [new age].

# user_name = input("Please enter your name ")
# user_age = int(input("How old are you? "))

# print(f"{user_name} next birthday you will be {user_age + 1}")


# 8) Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each a person must pay.

# total_price = float(input("How much was the bill? "))
# total_diners = int(input("How many people were eating? "))
# print(f"Each person must pay ${total_price / total_diners}")


# 9) Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.

# number_of_days = int(input("How many days would you like to convert? "))
# hours = number_of_days * 24
# minutes = hours * 60
# seconds = minutes * 60

# print(
#     f"There are {hours} hours, {minutes} minutes, and {seconds} seconds in {number_of_days}days"
# )

# 10) There are 2,204 pounds in a kilogram. Ask the user to enter a weight in kilograms and convert it to pounds.
# user_weight = int(input("How much kilograms do you weight? "))
# converted_weight = user_weight / 0.45359237
# print(f"You weight {converted_weight} lbs")

# 11) Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format.
# import random

# user_number = int(input("Please enter a number greater than 100: "))
# random_number = random.randint(1, 10)

# print(
#     f"The smaller number:{random_number} goes into the larger number:{user_number} approximately {user_number/random_number} times! "
# )


# user_large_number = int(input("Please enter a number over 100: "))
# user_small_number = int(input("Please enter a number under 10: "))
# print(
#     f"The smaller number:{user_small_number} goes into the larger number:{user_large_number} approximately {user_large_number/user_small_number} times! "
# )


############################################################################################################################

# xs = [3, 1, 2]  # Create a list
# print(xs, xs[2])
# print(xs[-1])  # Negative indices count from the end of the list; prints "2"


# # reassign an item in the list
# xs[2] = "foo"  # Lists can contain elements of different types
# print(xs)

# # appending multiple items
# xs.append("bar, test")  # Add a new element to the end of the list

# # remove the last element of list
# x = xs.pop()  # Remove and return the last element of the list
# print(x, xs)
# # List methods.


# Slicing is useful to get elements for strings.
animals = ["cat", "dog", "monkey"]
for animal in animals:
    print(animal)

# Goes through the animals list and keep pritning the index