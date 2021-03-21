# for item in "Python":
#     print(item)

# for item in ["Ricardo", "Mosh", "John Cena"]:
#     print(item)


# for item in [1, 2, 3, 4]:
#     print(item)


# iterate over a large list of numbers

# for item in range(10):
#     print(item)

# for item in range(5, 10):
#     print(item)

# for item in range(5, 10, 2):
#     print(item)


# exercise
# write a program to calc total cost of all item in shopping cart

# # my solution
# prices = [10, 20, 30]
# total = 0

# for cost in prices:
#     total += cost

# print(total)

prices = [10, 20, 30]
total = 0

for price in prices:
    total = total + price

print(f"Total: {total}")