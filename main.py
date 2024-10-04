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
            print(f'{self.username} New balance: ${self.balance}')
            print(f'{recipient.username} New balance: ${recipient.balance}')

        else:
            print(f'{self.username} has insufficient funds to transfer ${amount}. Current balance: ${self.balance}')


users = {}

def create_account():

    username = input('Enter a username: ')

    if username in users:

            print("Username already exists. Please choose a different username.")

    else:
        balance = float(input("Enter initial deposit amount: "))
        users[username] = User(username, balance)
        print(f'Account created for {username} with balance: ${balance}')


def login():
    username = input("enter your username: ")

    if username in users:
        return users[username]

    else:
        print("User don't exist. Please create an account first.")


def display_menu():
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Check balance")
    print("5. Logout")


def main():

    while True:
        print("\nWelcome to the Sampay Payement App")
        print("1. Create Account")
        