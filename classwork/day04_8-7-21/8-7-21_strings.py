# 1) Ask the user to enter their first name and then display the length of their first name. Then ask for their surname and display the length of their surname. Join their first name and surname together with a space between and display the result. Finally, display the length of their full name (including the space).

# first_name = input("Please enter your first name: ")
# print(f"{len(first_name)} letters long")
# last_name = input("Please enter your last name: ")
# print(f"{len(last_name)} letters long")
# print(f"{first_name} {last_name}, {len(first_name + last_name)} letters long.")

# 2) Ask the user to type in their favourite school subject. Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.

# user_subject = input("Please enter your favorite school subject: ")


# def subject():
#     string_input = ""
#     for i in user_subject:
#         string_input += i + "-"
#         # string_input += f"{i}-"
#     return string_input


# print(subject())


# 3) Show the user a line of text from your favourite poem and ask for a starting and ending point. Display the characters between those two points.

# [ ]
# 4) Ask the user to type in a word in upper case. If they type it in lower case, ask them to try again. Keep repeating this until they type in a message all in uppercase.

# user_word = input("Please enter a word in uppercase: ")

# while user_word != user_word.upper():
#     user_word = input("Please enter try again: ")
# print("Great, its all uppercase")

# [ ]
# 5) Ask the user to type in their postcode. Display the first two letters in uppercase.
# user_word = input("Please enter your city: ")

# converted = (
#     user_word[0:2].upper() + user_word[2:]
# )  # So this gets the characters from positon 0 to 2 and then uppercases it and spits out the rest of the words.
# print(converted)

# [ ]
# 5) Ask the user to type in their name and then tell them how many vowels are in their names

# [ ]
# 6) Ask the user to enter a new password. Ask them to enter it again. If the two passwords match, display “Thank you”. If the letters are correct but in the wrong case, display the message “They must be in the same case”, otherwise display the message “Incorrect”. 087 Ask the user to type in a word and then display it backwards on separate lines. For instance, if they type in “Hello” it should display as shown below:

# [ ]
# 7) Ask the user to type in a word and then display it backwards on separate lines. For instance, if they type in “Hello” it should display as shown below: Enter a word: Hello o l l e H

# user_word = input("Please enter a word: ")
# print(f"{user_word[::-1]}")

# Questions from "Python By Example"


# -------------------------------------------------