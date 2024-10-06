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

    username = input("Enter a username: ")

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
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            create_account()

        elif choice == '2':
            user = login()

            if user:
                while True:
                    display_menu()
                    option = input("Choose an option: ")

                    if option == '1':
                        amount = float(input("Enter deposit amount: "))
                        user.deposit(amount)

                    elif option == '2':
                        amount = float(input("Enter withdrawal amount: "))

                        user.withdrawal(amount)

                    elif option == '3':
                        recipient_name = input("Enter recipient username: ")

                        if recipient_name in users:
                            recipient = users[recipient_name]
                            amount = float(input(f'Enter amount to transfer to {recipient_name}: '))
                            user.transfer(amount, recipient)

                        else:
                            print("recipient username not found.")
                    
                    elif option == '4':
                        print(f'{user.username} Balance: ${user.balance}')

                    elif option == '5':
                        print("Logging out...")

                        break

                    else:
                        print("Invalid option. Please try again.")


        elif choice == '3':
            print("Exiting the application. Goodbye!")

            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == '__main__':

    main()


        