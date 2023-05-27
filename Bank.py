from Main_Bank_VersionX import Account

class Bank():
    def __init__(self):
        self.accountsDict = {}
        self.counter = 0
    
    def createAccount(self, name, password, money):
        oAccount = Account(name, "123", password, money)
        self.accountsDict[self.counter] = oAccount
        self.counter += 1


    def openAccount(self):
        pass

    def closeAccount(self):
        pass

    def balance(self):
        pass

    def deposit(self):
        pass

    def show(self):
        pass

    def withdraw(self):
        pass


    