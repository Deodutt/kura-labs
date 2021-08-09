# 1. Write a function that takes the length of a side of a square as an argument and returns the area of the square.


def lengthCalc(side):
    return side ** 2


print(lengthCalc(20))


# 2. Write a function that takes the heigth and width of a triangle and returns the area.


# def areaTriangle(height, width):
#     return 0.5 * height * width


# print(areaTriangle(10, 10))


# 3. Write a function that takes a string as an argument and returns a tuple consisting of two elements:
# A list of all the characters in the string.
# A count of the number of characters in the string.


# def stringConvert(string_argument):
#     tuples = []
#     charCount = len(string_argument)

#     for x in string_argument:
#         tuples += x
#     # print(f"{tuples} {charCount}")   #had this before but it printed out None at the bottom. You gotta return.
#     return (tuples, charCount)


# print(stringConvert("Python"))

# 4. Write a function that takes two integers, passed as strings, and returns the sum, difference, and product as a tuple (all values as integers).


# def stringCalc(x, y):
#     x = int(x)
#     y = int(y)
#     totalSum = x + y
#     totalDifference = x / y
#     totalProduct = x * y
#     return (totalSum, totalDifference, totalProduct)


# # print(stringCalc("2 3 1"))
# print(stringCalc("10", "2"))


# 5. Write a function that takes a list as the argument and returns a tuple consisting of two elements:
# A list with the items in reverse order.
# A list of the items in the original list that have an odd index.


def stringCalc(x, y):
    x = int(x)
    y = int(y)
    totalSum = x + y
    totalDifference = x / y
    totalProduct = x * y
    return (totalSum, totalDifference, totalProduct)


# print(stringCalc("2 3 1"))
print(stringCalc("10", "2"))


# Optional Challenge Problem: Write a function that returns the score for a word. The score of the word is the sum of the scores of its letters. Each letter's score is equal to it's position in the alphabet.
# So, for example:

# A = 1, B = 2, C = 3, D = 4, E = 5
# abe = 8 = (1 + 2 + 5)
# Hint: The string library has a property ascii_lowercase that can save some typing here.
