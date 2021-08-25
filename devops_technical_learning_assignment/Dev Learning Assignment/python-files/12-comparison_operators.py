# temperature = 36

# if temperature > 30:
#     print("Its a hot day!!")
# else:
#     print("Its not a hot day")


# exercise

name = input("Please enter your name: ")
characters = len(name)

if characters < 3:
    print("Name must be at least 3 chracters long")
elif characters > 50:
    print("Names must be a maximum number of 50 characters")
else:
    print(f"{name} looks good!")
