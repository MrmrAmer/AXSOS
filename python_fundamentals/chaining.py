class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

marwan = User("Marwan Amer", "moa@live.ca")
karam = User("Karam Rossum", "karam@live.ca")
ahmad = User("Ahmad Sadeq", "ahmad@live.ca")

marwan.make_deposit(100).make_deposit(300).make_deposit(100).make_withdrawal(200).display_user_balance()

karam.make_deposit(200).make_deposit(600).make_withdrawal(100).make_withdrawal(200).display_user_balance()

ahmad.make_deposit(200).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

marwan.transfer_money(ahmad, 200)
marwan.display_user_balance()
ahmad.display_user_balance()