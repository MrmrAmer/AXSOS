class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        
    def transfer_money(self, other_user, amount):
        # self.account_balance -= amount
        # other_user.account_balance += amount
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

marwan = User("Marwan Amer", "moa@live.ca")
karam = User("Karam Rossum", "karam@live.ca")
ahmad = User("Ahmad Sadeq", "ahmad@live.ca")

marwan.make_deposit(100)
marwan.make_deposit(300)
marwan.make_deposit(100)
marwan.make_withdrawal(200)
marwan.display_user_balance()

karam.make_deposit(200)
karam.make_deposit(600)
karam.make_withdrawal(100)
karam.make_withdrawal(200)
karam.display_user_balance()

ahmad.make_deposit(200)
ahmad.make_withdrawal(100)
ahmad.make_withdrawal(100)
ahmad.make_withdrawal(100)
ahmad.display_user_balance()

marwan.transfer_money(ahmad, 200)
marwan.display_user_balance()
ahmad.display_user_balance()