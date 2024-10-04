class User:

    def __init__(self, username, balance=0):
        
        self.username = username
        self.balance = balance

    def deposit(self, amount):
        self.amount += amount

        print(f'{self.username} deposited ${amount}. New balance: ${self.balance}')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

            print(f'{self.username} withdraw ${amount}. New balance: ${self.balance}')

        else:
            print(f'{self.username} has insufficient funds to withdraw ${amount}. Current balance is {self.balance}')

    def transfer(self, amount, recipient):

        if self.balance >= amount:
            self.balance -= amount

            recipient.balance += amount

            print(f'{self.username} transferred ${amount} to {recipient.username}.')
