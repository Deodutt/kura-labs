# names = ["Ricardo", "Colt", "Mosh", "Abdul", "John"]
# print(names)
# print(names[0])
# print(names[-2])

# print(names[2:])

# print(names[2:4]) # does not include 4

# print(names[:])  # return all item from beinging to end


# names[0] = "Jon"  # to replace an item.


# Exercise
# Write a program to find the largest number in a list

# MY SOLUTION
# numbers = [1, 24, 5426, 3, 204, 202]
# old = numbers[0]

# for x in numbers:
#     print(x)
#     if x > old:
#         old = x

# print(f"Largest number is {old}")


numbers = [3, 6, 2, 7, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)