import sys

class Account:

    def __init__(self, name, balance, password, accNumber):
        self.name = name
        self.balance = balance
        self.password = password
        self.accNumber = accNumber


class BankingSystem:

    def __init__(self):
        self.accounts = []

    def createAccount(self):

        password = None

        global accCounter
        accCounter += 1

        self.accNumber = accCounter

        name = input("\nEnter account owners name: ")
        balance = int(input("Enter initial deposit amount: "))
        lock = input("Would you like to setup a password for your account? (y/n): ")

        if lock == 'y':
            password = input("\nEnter your password: ")
            self.password = password
        else:
            self.password = None

        for account in self.accounts:
            while account.name == name:
                print("\nAn account with that name already exists.")
                name = input("Enter a different name: ")

        self.accounts.append((Account(name, balance, self.password, self.accNumber)))
        print("\nAccunt has succesfully been added")
        print("Your account number is ", self.accNumber)

    def viewAccount(self):

        accountNumber = int(input("\nEnter your account number: "))

        check = any(account.accNumber == accountNumber for account in self.accounts)

        if check == True:
            for account in self.accounts:
                if account.accNumber == accountNumber:
                    if account.password == None:
                        print(f"\nAccount number: {account.accNumber}")
                        print(f"Account user name: {account.name}")
                        print(f"Account balance: ${account.balance:,}")
                        print(f"Account password: {account.password}")
                    else:
                        checker = input("Enter your password: ")
                        while checker != account.password:
                            checker = input("Incorrect password. Try again: ")
                        print(f"\nAccount number: {account.accNumber}")
                        print(f"Account user name: {account.name}")
                        print(f"Account balance: ${account.balance:,}")
                        print(f"Account password: {account.password}")
        else:
            print("No such account number has been found.")

    def deposit(self):

        accNumber = int(input("\nEnter your account number: "))

        amount = int(input("How much would you like to deposit? "))

        check = any(account.accNumber == accNumber for account in self.accounts)

        if check == True:
            for account in self.accounts:
                if account.accNumber == accNumber:
                    if account.password == None:
                        account.balance = account.balance + amount
                        print("\nDeposit succesfull")
                        print(f"Account balance: ${account.balance:,}\n")
                    else:
                        checker = input("Enter your password: ")
                        while checker != account.password:
                            checker = input("Incorrect password. Try again: ")
                        account.balance = account.balance + amount
                        print("\nDeposit succesfull")
                        print(f"Account balance: ${account.balance:,}\n")
        else:
            print("No such account number has been found.")

    def withdraw(self):

        accNumber = int(input("\nEnter your account number: "))
        amount = int(input("How much would you like to withdraw? "))

        check = any(account.accNumber == accNumber for account in self.accounts)

        if check == True:
            for account in self.accounts:
                if account.accNumber == accNumber:
                    if account.password == None:
                        if account.balance >= amount:
                            account.balance = account.balance - amount
                            print("\nWithdrawal succesfull")
                            print(f"Account balance: ${account.balance:,}\n")
                        else:
                            print("Not enough money in account for withdrawal.")
                    else:
                        checker = input("Enter your password: ")
                        while checker != account.password:
                            checker = input("Incorrect password. Try again: ")
                        if account.balance >= amount:
                            account.balance = account.balance - amount
                            print("\nWithdrawal succesfull")
                            print(f"Account balance: ${account.balance:,}\n")
                        else:
                            print("Not enough money in account for withdrawal.")
        else:
            print("No such account number has been found.")

    def transfer(self):

        account1 = int(input("\nEnter your account number: "))

        check1 = any(account.accNumber == account1 for account in self.accounts)

        if check1 == False:
            print("No such account number has been found")
        else:
            account2 = int(input("Enter the account number you wish to transfer to: "))
            check2 = any(account.accNumber == account2 for account in self.accounts)

        if check2 == False:
            print("No such account number has been found")

        else:
            amount = int(input("\nEnter the amount you'd like to transfer: "))

            for account in self.accounts:
                if account.accNumber == account1:
                    if account.password == None:
                        if account.balance >= amount:
                            account.balance = account.balance - amount
                            print("\nTransfer succesfull")
                            print(f"Account {account1} balance: ${account.balance:,}\n")
                        else:
                            print("Not enough money in account for withdrawal.")
                    else:
                        checker = input("Enter your password: ")
                        while checker != account.password:
                            checker = input("Incorrect password. Try again: ")
                        if account.balance >= amount:
                            account.balance = account.balance - amount
                            print("\nTransfer succesfull")
                            print(f"Account {account1} balance: ${account.balance:,}\n")
                        else:
                            print("Not enough money in account for withdrawal.")

            for account in self.accounts:
                if account.accNumber == account2:
                    account.balance = account.balance + amount
                    print("\nDeposit succesfull")
                    print(f"Account {account1} balance: ${account.balance:,}\n")

    def close(self):

        global accCounter

        confirm = input(
            "\nAre you sure you want to close your account? Your account information will be deleted from the database. (y/n)")

        if confirm == "y":
            accNumber = int(input("\nEnter your account number: "))

            check = any(account.accNumber == accNumber for account in self.accounts)

            if check == False:
                print("No such account number has been found")
            else:
                for account in self.accounts:
                    if account.accNumber == accNumber:
                        if account.password == None:
                            if account.balance > 0:
                                print(
                                    "\nWARNING! You still have money on this account, you should transfer it to another account first.")
                                bank.transfer()
                            else:
                                self.accounts.remove(account)
                                accCounter -= 1
                                print("\nAccount succesfully deleted.")
                        else:
                            checker = input("Enter your password: ")
                            while checker != account.password:
                                checker = input("Incorrect password. Try again: ")
                            if account.balance > 0:
                                print(
                                    "\nWARNING! You still have money on this account, you should transfer it to another account first.")
                                bank.transfer()
                            else:
                                self.accounts.remove(account)
                                accCounter -= 1
                                print("\nAccount succesfully deleted.")
        else:
            pass

    def update(self):

        accNumber = int(input("\nEnter your account number: "))

        check = any(account.accNumber == accNumber for account in self.accounts)

        if check == True:

            action = input("\nType 'n' to change your name or 'p' to change your password: ")

            if action == 'n':
                for account in self.accounts:
                    if account.accNumber == accNumber:
                        updateName = input("Enter new user name: ")
                        account.name = updateName
                        print(f"\nUpdate succesful, user name is now {account.name}")
                        break

            elif action == 'p':
                for account in self.accounts:
                    if account.accNumber == accNumber:
                        if account.password == None:
                            newPass = input(
                                "\nYou currently dont have a password. Would you like to create one? (y/n): ")

                            if newPass == 'y':
                                password = input("Enter your password: ")
                                account.password = password
                                print(f"\nUpdate succesful, password is now {account.password}")
                                break
                        else:
                            checker = input("Enter your password: ")
                            while checker != account.password:
                                checker = input("Incorrect password. Try again: ")
                            updatePassword = input("Enter new password: ")
                            account.password = updatePassword
                            print(f"\nUpdate succesful, password is now {account.password}")
                            break

            else:
                print("Invalid input, try again: ")
        else:
            print("No such account number has been found")


bank = BankingSystem()

accCounter = 1000

while True:
    print("\n--- Banking System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Account")
    print("5. Transfer money")
    print("6. Close account")
    print("7. Update account information")
    print("8. Exit")

    try:
        choice = int(input("Choose an option: "))

        while choice < 1 or choice > 8:
            choice = int(input("Invalid choice, please try again: "))

        if choice == 1:
            bank.createAccount()
        elif choice == 2:
            bank.deposit()
        elif choice == 3:
            bank.withdraw()
        elif choice == 4:
            bank.viewAccount()
        elif choice == 5:
            bank.transfer()
        elif choice == 6:
            bank.close()
        elif choice == 7:
            bank.update()
        elif choice == 8:
            print("\nExiting now. Thank you for using our bank.")
            sys.exit()

    except ValueError:
        print("Invalid input, please enter a valid number.")