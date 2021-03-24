# #DOES NOT WORK. YOU NEED TO RENAME FILE WITHJ NO NUMBERS IN THE START.


# import 36-modules_converters
# # converter = __import__("36-modules_converters")

# from converter import kg_to_lbs

# # importlib.__import__(name, globals=None, locals=None, fromlist=(), level=0)
# # https://docs.python.org/3/library/importlib.html#importlib.import_module

# print(kg_to_lbs(100)
# # print(converter.kg_to_lbs(70))


# EXERCISE TO FIND LARGEST NUMBER IN LIST
# numbers = [10, 3, 6, 2]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)


# write a function called find_max() should take a list and return largest number in list. then put the function in a seperate module called utils. utils will have bunch of ultility functions. then import the util module into current module and call the function. get result and print it on the terminal.

import modules_converters_and_utils-36
from utils import find_max

numbers = [10, 3, 6, 2]
max2 = find_max(numbers)
print(max2)