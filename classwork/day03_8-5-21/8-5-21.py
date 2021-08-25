# 1) Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number, otherwise show the first number first and then the second.

# first_number = int(input("Please enter the first number: "))
# second_number = int(input("Please enter the second number: "))

# if first_number > second_number:
#     print(f"{second_number} < {first_number}")
# else:
#     print(f"{first_number} < {second_number}")


# 2) Ask the user to enter a number that is under 20. If they enter a number that is 20 or more, display the message “Too high”, otherwise display “Thank you”.

# user_number = int(input("Please enter a number under 20: "))

# if user_number > 20:
#     print(f"Too high!")
# else:
#     print(f"Thank you!")

# 3) Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range, display the message “Thank you”, otherwise display the message “Incorrect answer"

# user_number = int(input("Please enter a number between 10 and 20: "))

# if user_number > 10 and user_number < 20:
#     print(f"Thank you")
# else:
#     print(f"Incorrect answer!")


# 4) Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”, otherwise display the message “I don’t like [colour], I prefer red”.

# user_color = input("Please enter your favorite Color: ")

# if user_color == "red" or user_color == "RED" or user_color == "Red":
#     print(f"I like red too")

# else:
#     print(f"I dont like {user_color}, I prefer red")


# 5) Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what case they type it in. If they answer “yes”, ask if it is windy. If they answer “yes” to this second question, display the answer “It is too windy for an umbrella”, otherwise display the message “Take an umbrella”. If they did not answer yes to the first question, display the answer “Enjoy your day”.

# user_weather = input("Is it raining today? ").lower()
# # print(user_weather)

# if user_weather == "yes":
#     user_weather_windy = input("Is it also windy today? ").lower()
#     if user_weather_windy == "yes":
#         print(f"It is too windy for an umbrella")
#     else:
#         print(f"Take an umbrella!")
# else:
#     print(f"Enjoy your day sir")


# 6) Ask the user’s age. If they are 18 or over, display the message “You can vote”, if they are aged 17, display the message “You can learn to drive”, if they are 16, display the message “You can buy a lottery ticket”, if they are under 16, display the message “You can go Trickor- Treating”.

# user_age = int(input("What is your age?? "))

# if user_age >= 18:
#     print(f"You can vote!")
# elif user_age == 17:
#     print(f"You can learn to drive")
# elif user_age == 16:
#     print(f"You can buy a lottery ticket!")

# # elif user_age < 16:
# else:
#     print(f"You can go trick or treating!")

# 7) Ask the user to enter a number. If it is under 10, display the message “Too low”, if their number is between 10 and 20, display “Correct”, otherwise display “Too high”.

# user_number = int(input("Please enter a number: "))

# if user_number < 10:
#     print(f"Too Low")
# elif user_number > 10 and user_number < 20:
#     print(f"Correct!")
# else:
#     print(f"Too High!")


# 8) Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”, if they enter a 2, display “Well done”, if they enter a 3, display “Correct”. If they enter anything else, display “Error message”.

# user_guess = int(input("Please enter 1, 2 or 3: "))

# if user_guess == 1:
#     print(f"Thank you")
# elif user_guess == 2:
#     print(f"Well done")
# elif user_guess == 3:
#     print(f"Correct")
# else:
#     print(f"Error Message")


# # 9) Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”, if they enter a 2, display “Well done”, if they enter a 3, display “Correct”. If they enter anything else, display “Error message”.

# user_guess = int(input("Please enter 1, 2 or 3: "))

# if user_guess == 1:
#     print(f"Thank you")
# elif user_guess == 2:
#     print(f"Well done")
# elif user_guess == 3:
#     print(f"Correct")
# else:
#     print(f"Error Message")
