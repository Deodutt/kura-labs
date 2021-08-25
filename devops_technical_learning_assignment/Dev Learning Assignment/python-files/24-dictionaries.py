# # Name: Ricardo Deodutt
# # Email: RicardoDeodutt@gmail.com
# # Phone
# # #These are key value pairs.

# customer = {"name": "John Cena", "age": 34, "is_verified": True}

# # can acess each item using []

# print(customer["name"])
# print(customer.get("birthday", "Jan 1 1980"))

# customer["name"] = "Jack Smith"
# customer["birthday"] = "Jack Smith"


# # exercise
# # program that ask for phone number

phone = input("Phone Number: ")

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "

print(output)