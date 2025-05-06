class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate= 0.02, balance= 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Account Balance: ${self.balance}")
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

marwan = User("Marwan Amer", "moa@live.ca")
karam = User("Karam Rossum", "karam@live.ca")
ahmad = User("Ahmad Sadeq", "ahmad@live.ca")

marwan.make_deposit(100).make_deposit(300).make_deposit(100).make_withdrawal(200).display_user_balance()