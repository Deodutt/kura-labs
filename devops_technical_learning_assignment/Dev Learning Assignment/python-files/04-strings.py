# course = "Python's for Dummies"
# course = 'Python for "Dummies"'


# define a string with multiple lines. use tripple quotes.
# course = """
# Hi John,

# Here is our first email to you.

# Thank you,
# The support teams

# """
# print(course)


course = "Python for Beginners"
another = course[:] # second variable will be copy of first variable
# print(course[0])
# print(course[-2])

print(
    course[0:3]
    # python intreper will return all characters from starting with the index 0  all the way to second index but does not retrun the last index. so 0, 1, 2

    course[0:]
    # if you dont supply end character, python will return all characters to end of string.

    
    course[1:]
    # the first index is removed.

        
    course[:5]
    # python interpreter will assume 0 is the first index.

    course[:]
    # so basically 0 will be assumed as start index. legnth of string will bne assumed as the end of index.

)

# small exercise
name = 'Jennifer'
print(name[1:-1])
# This will start from index 1 which is 'e' all the way from the second chracter to the end. exlcuding it
#ennife


