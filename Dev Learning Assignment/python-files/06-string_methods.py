course = "Python for Dummies"
# print(len(course))


# another function to conmverting a string to uppercase and lowercase. We access it by using . operators
# print(course.upper())
# course.<method>
# when a function belongs to something else.
# this method does not change or modify the original string. it mmakes a new string and prints it.

# print(course.lower())


# times where you want to find a character or sequence of characters
# print(
#     course.find("P")
#     course.find("o")
#     course.find("Beginners") #returns 11 because the word beginner starts at index 11
# )  # this will return the index of the first occurance of the character.
# IT IS CASE SENSITIVE
# WHEN YOU GET -1 ITS BECAUSE ITS NOT IN THE STRING

# method of repalcing character.

print(course.replace("Dummies", "Absolute Beginners"))

print(
    "Python" in course
)  # produces a boolean value so this is a boolean expression.... True
print(
    "python" in course
)  # produces a boolean value so this is a boolean expression.... True


# len()  # to count number of characters in a string. general purpose function

# specific fucntions for a string. refered to as method
# course.upper()
# course.lower()
# course.title()
# course.find()
# course.replace()
# "...." in course