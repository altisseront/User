class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_withdrawal(self, amount):
        self.balance -= amount

    def make_deposit(self, amount):
        self.balance += amount

    def display_user_balance(self):
        print(self.name, "=", self.balance)
        
    def transfer_money(self, recipient, amount):
        self.balance -= amount
        recipient.balance += amount
        print(self.name, "=", self.balance, recipient.name, "=", recipient.balance)

gilbert = User("gilbert", 0)
jimmy = User("jimmy", 0)
frederick = User("frederick", 0)


gilbert.make_deposit(400)
gilbert.make_deposit(200)
gilbert.make_deposit(100)
gilbert.make_withdrawal(50)
gilbert.display_user_balance()

jimmy.make_deposit(230)
jimmy.make_deposit(140)
jimmy.make_withdrawal(50)
jimmy.make_withdrawal(500)
jimmy.display_user_balance()

frederick.make_deposit(150)
frederick.make_withdrawal(10)
frederick.make_withdrawal(70)
frederick.make_withdrawal(20)
frederick.display_user_balance()

jimmy.transfer_money(gilbert, 200)