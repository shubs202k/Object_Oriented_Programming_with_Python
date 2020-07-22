from abc import abstractmethod,ABCMeta
from random import randint

class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0

    @abstractmethod
    def authenticate():
        return 0

    @abstractmethod
    def withdraw():
        return 0

    @abstractmethod
    def deposit():
        return 0

    @abstractmethod
    def displayBalance():
        return 0

class SavingsAccount(Account):
    def __init__(self):
        self.savingsAccounts = {}

    # Create New Account
    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000,99999)
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]
        print('Account creation successful. Your Account number is ', self.accountNumber)

    # Authenticate an user
    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNumber][0] == name:
                print("Authentication Successful")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False

    # Withdraw amount
    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccounts[self.accountNumber][1]:
            print("Insufficient balance")
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawalAmount
            print("Withdrawal was Successful")
            self.displayBalance()

    # Deposit Amount
    def deposit(self, depositAmount):
        self.savingsAccounts[self.accountNumber][1] += depositAmount
        print("Deposit was successful")
        self.displayBalance()

    # Avalaible Balance
    def displayBalance(self):
        print("Available balance: ", self.savingsAccounts[self.accountNumber][1])

savingsAccount = SavingsAccount()

while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")

    userChoice = int(input())

    if userChoice is 1:
        # Create account for a new customer
        print("Enter your name: ")
        name = input()
        print("Enter the initial deposit: ")
        deposit = int(input())
        savingsAccount.createAccount(name, deposit)
    elif userChoice is 2:
        # Authenticate account for an existing customer
        print("Enter your name: ")
        name = input()
        print("Enter your account number: ")
        accountNumber = int(input())
        authenticationStatus = savingsAccount.authenticate(name, accountNumber)

        if authenticationStatus is True:
            # If customer has an account
            while True:
                print("Enter 1 to Withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display available balance")
                print("Enter 4 to go back to the previous menu")

                userChoice = int(input())

                if userChoice is 1:
                    print('Enter a withdrawal amount')
                    withdrawalAmount = int(input())
                    savingsAccount.withdraw(withdrawalAmount)
                elif userChoice is 2:
                    print("Enter amount to deposit")
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)
                elif userChoice is 3:
                    savingsAccount.displayBalance()
                elif userChoice is 4:
                    break
    elif userChoice is 3:
        quit()
