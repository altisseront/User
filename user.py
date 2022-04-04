class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        self.balance *= self.int_rate
        return self
    @classmethod
    def displayAllBalances(cls):
        for account in cls.all_accounts:
            print(account.balance)

# account1 = BankAccount(1.05, 0)
# account2 = BankAccount(1.02, 100)

# account1.deposit(50).deposit(70).deposit(15).withdraw(12).yield_interest().display_account_info()
# account2.deposit(700).deposit(50).withdraw(87.5).withdraw(99).withdraw(140).withdraw(4.5).yield_interest().display_account_info()

# BankAccount.displayAllBalances()


class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate=1.2, balance=0)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        
    def transfer_money(self, recipient, amount):
        self.account.withdraw(amount)
        recipient.account.deposit(amount)
        self.account.display_account_info()
        recipient.account.display_account_info(0)


gilbert = User("gilbert")
gilbert.make_deposit(500).display_user_balance()

# gilbert = User("gilbert", 0)
# jimmy = User("jimmy", 0)
# frederick = User("frederick", 0)


# gilbert.make_deposit(400).make_deposit(200).make_deposit(100).make_withdrawal(50).display_user_balance()
# jimmy.make_deposit(230).make_deposit(140).make_withdrawal(200).make_withdrawal(200).display_user_balance()

# frederick.make_deposit(150).make_withdrawal(30).make_withdrawal(40).make_withdrawal(20).display_user_balance()


# jimmy.transfer_money(gilbert, 200)

