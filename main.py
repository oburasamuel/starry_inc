class User:

    def __init__(self, username, balance=0):
        
        self.username = username
        self.balance = balance

    def deposit(self, amount):
        self.amount += amount

        print(f'{self.username} deposited ${amount}. New balance: ${self.balance}')