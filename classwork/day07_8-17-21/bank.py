class BankAccount:
    def __init__(self, name, action):
        self.name = name
        self.action = action

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
                "Target: 5.59",
                "Amazon REFUND: 27.59",
            ],
            "saiho yip": [
                112233,
                2.75,
                "CVS: 14.89",
                "Target: 200.89",
                "ExxonMobil Gas: 20.52",
            ],
        }


customer_name = "Ricardo Deodutt"

a = BankAccount("Ricardo Deodutt", "withdraw", 100)
b = BankAccount("Ricardo Deodutt", "deposit", 100)
print(__main__)