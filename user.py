class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    def make_deposit(self, amount):
        self.balance += amount
        return self

    def display_user_balance(self):
        print(self.name, "=", self.balance)
        
    def transfer_money(self, recipient, amount):
        self.balance -= amount
        recipient.balance += amount
        print(self.name, "=", self.balance, recipient.name, "=", recipient.balance)

gilbert = User("gilbert", 0)
jimmy = User("jimmy", 0)
frederick = User("frederick", 0)


gilbert.make_deposit(400).make_deposit(200).make_deposit(100).make_withdrawal(50).display_user_balance()
jimmy.make_deposit(230).make_deposit(140).make_withdrawal(200).make_withdrawal(200).display_user_balance()

frederick.make_deposit(150).make_withdrawal(30).make_withdrawal(40).make_withdrawal(20).display_user_balance()


jimmy.transfer_money(gilbert, 200)