# numbers = [5, 2, 1, 7, 4]

# numbers.append(20)  # add a new item to a list

# numbers.insert(
#     0, 10
# )  # add a new item to a at the start. first number is index position and second value is the object you want to add to the list. all the rest items are pushed to right
# print(numbers)


# numbers.remove(5)

# numbers.clear()  # empty out list.
# numbers.pop()  # pops out the last value
# numbers.index(5)  # returns the index of the first occurance of the item
# print(50 in numbers)

# numbers.count(5)  # count amount of occurance

# numbers.sort()  # to sort the list.
# numbers.reverse()  # simply reverses the list

# numbers2 = numbers.copy()  # to easily copy thje list


# Exercise. write a program to remove the duplicates in a list

numbers = [1, 1, 3, 4, 2, 9, 0, 9, 2, 34, 42531, 12, 34]
uniques = []

for x in numbers:
    if x not in uniques:
        uniques.append(x)
print(uniques)