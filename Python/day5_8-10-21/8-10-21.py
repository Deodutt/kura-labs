# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def get_area(self):
#         return self.length * self.width


# p1 = Rectangle(20, 20)
# p2 = Rectangle(20, 20)
# print(p1.get_area())

# print(id(p1))
# print(id(p2))


# class Square(Rectangle):
#     def __init__(self, length):  # overriding
#         self.length = length
#         self.width = length
#         super().__init__(length, length)


# first_square = Square(10)

# print(first_square.get_area())
# ---------------------# ---------------------# ---------------------# ---------------------# ---------------------# ---------------------# ---------------------


# class BankAccount:
#     def __init__(self, name):
#         self.customers = {
#             "Ricardo Deodutt": 877393,
#             "Daniel Adeyanju": 123456,
#             "Saiho Yip": 112233,
#         }

#         self.balance = {
#             "Ricardo Deodutt": 12000,
#             "Daniel Adeyanju": 5000,
#             "Saiho Yip": 2.75,
#         }
#         # {name: [accountnumber ,balance, tran1, tran2, tran3 ]}
#         self.transactions = ["ExxonMobil Gas: 33.52", "Key Food : 14.25"]
#         # {
#         #     "ExxonMobil Gas": "33.52",
#         #     "Key Food": "14.25",
#         #     "The Home Depot": "21.75",
#         #     "Target": "-5.59",
#         #     "Amazon REFUND": "+27.59",
#         #     "CVS": "-14.89",
#         # }

#         self.newcustomers = {
#             "Ricardo Deodutt": [
#                 877393,
#                 12000,
#                 "ExxonMobil Gas: 33.52",
#                 "Key Food : 14.25",
#             ],
#             "Daniel Adeyanju": [
#                 123456,
#                 5000,
#                 "The Home Depot: 21.75",
#                 "Target: -5.59",
#                 "Amazon REFUND: +27.59",
#             ],
#             "Saiho Yip": [112233, 2.75, "CVS: -14.89"],
#         }

#     def getBalance(self):
#         obtained_balance = self.balance.get(customer_name)
#         print(f"You have a current balance of ${obtained_balance}.")
#         self.customer_decision()

#     def deposit(self):
#         obtained_balance = self.balance.get(customer_name)
#         deposit_amount = int(input("How much would you like to deposit? $"))
#         new_balance = obtained_balance + deposit_amount

#         print(f"Please wait......... Successfully added!")
#         self.balance[customer_name] = new_balance
#         print(f"New Balance: ${self.balance.get(customer_name)}")
#         self.transactions.append(f"{customer_name} added {deposit_amount}")
#         self.customer_decision()

#     def withdrawal(self):
#         obtained_balance = self.balance.get(customer_name)
#         withdraw_amount = int(input("How much would you like to withdraw? $"))
#         new_balance = obtained_balance - withdraw_amount

#         print(f"Please wait......... Successfully withdrew!\n Please take your money!")
#         self.balance[customer_name] = new_balance
#         print(f"New Balance: ${self.balance.get(customer_name)}")
#         self.customer_decision()

#     def transaction(self):
#         print(self.transactions)

#     def verification(self):
#         obtained_account_number = self.customers.get(customer_name)

#         state = False
#         while state == False:
#             customer_account_number = int(
#                 input(
#                     "Now please input your 6 digit account number you want to look up: "
#                 )
#             )

#             if obtained_account_number != customer_account_number:
#                 print("The information you entered is incorrect ")

#             elif obtained_account_number == customer_account_number:
#                 state = True

#     def customer_decision(self):
#         customer_decisions = int(
#             input(
#                 "\nPlease enter the number of what you would like to do\n1. Get Balance Information\n2. Make a Deposit\n3. Make a Withdrawal\n4. Get previous Transactions\n5. Exit\n\nChoice: "
#             )
#         )

#         if customer_decisions == 1:
#             self.getBalance()
#         elif customer_decisions == 2:
#             self.deposit()
#         elif customer_decisions == 3:
#             self.deposit()
#         elif customer_decisions == 4:
#             self.transaction()
#         elif customer_decisions == 5:
#             print("Goodbye!")
#             exit
#         else:
#             print("Incorrect response!")
#             self.customer_decision()


# customer_name = input(
#     "Hello! Welcome to Ricardo's banking services!\nPlease input your name: "
# )

# p1 = BankAccount(customer_name)
# print(p1.newcustomers.get("Ricardo Deodutt"))
# p1.verification()

from datetime import date  # used for appending transactions.


class BankAccount:
    def __init__(self, name):

        self.customer_accounts = {
            "ricardo deodutt": [
                877393,
                12000,
                "ExxonMobil Gas: 33.52",
                "Key Food : 14.25",
            ],
            "daniel adeyanju": [
                123456,
                5000,
                "The Home Depot: 21.75",
                "Target: -5.59",
                "Amazon REFUND: 27.59",
            ],
            "saiho yip": [
                112233,
                2.75,
                "CVS: -14.89",
                "Target: 200.89",
                "ExxonMobil Gas: 20.52",
            ],
        }

    # This method outputs the balance of the current user.
    def getBalance(self):
        obtained_balance = self.customer_accounts.get(
            customer_name
        )  # uses the get dictionary method to obtain the (key)value which is a list. and assign it to obtained_balance
        balance = obtained_balance[
            1
        ]  # This uses the list that was obtained from the dictironary and assigns the first index (which is account balance) to balance

        print(
            f"You have a current balance of ${balance}."
        )  # simple print out of balance
        self.customer_decision()  # Calling the customer_decision() function to ask user what to do next

    # This method ask a user how much they want to deposit and updates value in the dictionary.
    def deposit(self):
        obtained_balance = self.customer_accounts.get(customer_name)
        # balance = obtained_balance[1]
        deposit_amount = int(
            input("How much would you like to deposit? $")
        )  # ask user for amount
        new_balance = (
            obtained_balance[1] + deposit_amount
        )  # adds the value the user inputted and the value that was in the dictionary and assigns it to new_balance variable.

        self.customer_accounts.get(customer_name)[
            1
        ] = new_balance  # Updates the account balance
        print(f"Please wait......... Successfully added!")
        print(
            f"New Balance: ${self.customer_accounts.get(customer_name)[1]}"
        )  # printing the current balance
        today = date.today()  # used to get the current date. Needed for append.
        self.customer_accounts.get(customer_name).append(
            f"{customer_name.title()} has added ${deposit_amount} on {today}"  # I am adding on to the list that is inside of the dictionary. (The value in the keyvalue pair.)
        )
        self.customer_decision()  # Calls the customer_decision() function

    # Similar to deposit method.
    def withdrawal(self):
        obtained_balance = self.customer_accounts.get(
            customer_name
        )  # gets the value from dictionary
        withdraw_amount = int(
            input("How much would you like to withdraw? $")
        )  # ask how much to take out.
        new_balance = (
            obtained_balance[1] - withdraw_amount
        )  # does math to get new balance.

        print(f"Please wait......... Successfully withdrew!\nPlease take your money!")
        self.customer_accounts.get(customer_name)[
            1
        ] = new_balance  # updates the new balance
        print(
            f"New Balance: ${self.customer_accounts.get(customer_name)[1]}"
        )  # prints the new balance
        today = date.today()  # gets the date for appending
        self.customer_accounts.get(customer_name).append(
            f"{customer_name.title()} has withdrew ${withdraw_amount} on {today}"  # appends a string to the list
        )
        self.customer_decision()  # runs the customer_decision() method

    # This prints everything in the list after the second index.
    def transaction(self):
        obtained_transactions = self.customer_accounts.get(
            customer_name
        )  # gets the list
        transaction_list = obtained_transactions[
            2:
        ]  # create a new list using the old list but a sliced version. 2: means to take everything after the 2nd index.
        print(transaction_list)  # prints out the transaction list
        self.customer_decision()

    def transfer(self):
        obtained_user = self.customer_accounts.get(
            customer_name
        )  # gets the value from dictionary for the current user.
        transfer_user = str(
            input(
                "Please input the user you would like to transfer to: "
            )  # ask user for the other account to transfer to
        ).lower()

        transfer_user_amount = self.customer_accounts.get(
            transfer_user
        )  # gets the other uses record (aka the value from the keyvalue pair in the dictionary)

        # This part basically checks if the user that was entered was correct. When the code uses the get method. If the user doesnt exist it would put the value as None.
        # If it shows None, then it runs the method again which basically ask the user for the input again.
        if transfer_user_amount == None:
            print("Incorrect user!")
            self.transfer()
        else:
            pass

        # Then ask user how much to transfer.
        transfer_amount = int(
            input(
                f"How much money do you want to transfer to {transfer_user.title()}? $"  # The .title() method basically capitalizes each word in a string.
            )
        )

        # calulates the new_balance and updates the current account balance.
        new_balance = obtained_user[1] - transfer_amount
        self.customer_accounts.get(customer_name)[1] = new_balance

        # calulates the new_balance and updates the transfer userss account balance.
        new_balance = transfer_user_amount[1] + transfer_amount
        self.customer_accounts.get(transfer_user)[1] = new_balance

        print(f"Please wait......... Successfully Sent!")
        # prints outs both users balance. (I did this to show it updated each. I did not create a logout function to log into other users.)
        print(
            f"New Balance for {customer_name.title()}: ${self.customer_accounts.get(customer_name)[1]}"
        )
        print(
            f"New Balance for {transfer_user.title()}: ${self.customer_accounts.get(transfer_user)[1]}"
        )

        # appending
        today = date.today()
        self.customer_accounts.get(customer_name).append(
            f"{customer_name.title()} has transferred ${transfer_amount} to {transfer_user.title()} on {today}"
        )
        self.customer_accounts.get(transfer_user).append(
            f"You have recieved {transfer_amount} from {customer_name.title()} on {today}"
        )
        self.customer_decision()

    # This method is ran after user inputs their name.
    def verification(self):
        # print(self.customer_accounts.get(customer_name))
        obtained_account_number = self.customer_accounts.get(
            customer_name
        )  # This assigns the value from the dictionary to "obtained_account_number". The value is a list data type.
        obtained_account_number_index = obtained_account_number[
            0
        ]  # This assigns the first value in the list (which is account number) to "obtained_account_index"

        # This part uses a while loop to check if a user inputted the corresponding account number that matches the customer name.
        state = False
        while state == False:
            customer_account_number = int(
                input(
                    "Now please input your 6 digit account number you want to look up: "
                )
            )

            if obtained_account_number_index != customer_account_number:
                print("The information you entered is incorrect ")

            elif obtained_account_number_index == customer_account_number:
                state = True

    # Runs all the time asking the user what they would like to do.
    def customer_decision(self):
        customer_decisions = int(
            input(
                "\nPlease enter the number of what you would like to do\n1. Get Balance Information\n2. Make a Deposit\n3. Make a Withdrawal\n4. Get previous Transactions\n5. Transfer money to another user\n5. Exit\n\nChoice: "
            )
        )

        if customer_decisions == 1:
            self.getBalance()
        elif customer_decisions == 2:
            self.deposit()
        elif customer_decisions == 3:
            self.withdrawal()
        elif customer_decisions == 4:
            self.transaction()
        elif customer_decisions == 5:
            self.transfer()
        elif customer_decisions == 6:
            print("Goodbye!")
            exit
        else:
            print("Incorrect response!")
            self.customer_decision()


customer_name = input(
    "Hello! Welcome to Ricardo's banking services!\nPlease input your name: "
).lower()

p1 = BankAccount(customer_name)
p1.verification()
p1.customer_decision()