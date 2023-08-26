from Main_Bank_VersionX import Account

class Bank():
    def __init__(self):
        self.accountsDict = {}
        self.counter = 0
    
    def createAccount(self, name, password, money):
        oAccount = Account(name, password, money)
        self.accountsDict[self.counter] = oAccount
        self.counter += 1
    
    def open_account(self):
        '''creating a new account with interaction'''
        print("\n*** Open Account ***")
        name = input("Insert your name: ")
        pw = input("Insert your pw: ")
        first_amount = int(input("Insert amount £: "))
        self.createAccount(name=name, password=pw, money=first_amount)

    def closeAccount(self):
        print("\n*** Close Account ***")
        account_number = int(input("Insert the account number: "))
        pw = input("Insert your password: ")
        if pw == self.accountsDict[account_number].password:
            print(f"pw ok!")
            if self.accountsDict[account_number].balance > 0:
                print(f"You had {self.accountsDict[account_number].balance} in your bank account wich they will return to you")
            self.accountsDict.pop(account_number)
            print(f"Account: {account_number} eliminated")
        else:
            print("wrong password\nprogram ended")

    def balance(self):
        print("\n*** Balance ***")
        account_number = int(input("Insert the account number: "))
        pw = input("Insert your password: ")
        if pw == self.accountsDict[account_number].password:
            print("pw ok!")
            print(f"Balance: {self.accountsDict[account_number].show()}")
        else:
            print("wrong password\nprogram ended")

    def deposit(self):
        print("\n*** Deposit ***")
        account_number = int(input("Insert the account number: "))
        pw = input("Insert your password: ")
        if pw == self.accountsDict[account_number].password:
            print("pw ok!")
            deposit = int(input("insert the amount you want deposit: "))
            self.accountsDict[account_number].deposit(deposit)
            print(f"deposit of {deposit} done!")
        else:
            print("wrong password\nprogram ended")

    def withdraw(self):
        print("\n*** Withdraw ***")
        account_number = int(input("Insert the account number: "))
        pw = input("Insert your password: ")
        if pw == self.accountsDict[account_number].password:
            print("pw ok!")
            wit = int(input("insert the withdraw amount: "))
            self.accountsDict[account_number].withdraw(wit)
            print(f"withdraw of {wit} done!")
        else:
            print("wrong password\nprogram ended")
    
    def show(self):
        '''show the info of a specific account'''
        print("\n*** Show info account ***")
        account_number = int(input("Insert the account number: "))
        pw = input("Insert your password: ")
        if pw == self.accountsDict[account_number].password:
            print("pw ok!")
            name = self.accountsDict[account_number].name
            balance = self.accountsDict[account_number].balance
            print(f"Account N: {account_number} Name: {name} Balance: {balance}")
        else:
            print("wrong password\nprogram ended")

    def show_all_account(self):
        '''for debug/admin'''
        print("\n*** Accounts list ***")
        if self.accountsDict == {}:
            print("<empty>")
        else:    
            for i, j in self.accountsDict.items():
                print(f"N.:{i} Name: {j.name} Pw: {j.password} Balance: {j.balance}")


    



    