'''
Account creation using a dictionary
it's a better solution in case you want delete a bank account
'''

from Main_Bank_VersionX import *

accountsDict = {}
counter = 0

# creating first account
oAccount = Account('Joe', "123", 500)
accountsDict[counter] = oAccount
counter += 1

# creating second account
oAccount = Account("Mary", "456", 800)
accountsDict[counter] = oAccount
counter += 1

# using the 2 objects in the dictionary
accountsDict[0].show()
accountsDict[1].show()
accountsDict[1].deposit(300, accountsDict[1].password)
accountsDict[1].show()

# creating account from user inputs
userName = input("Creating bank account, insert name: ")
userPassword = input("Insert password: ")
userBalance = int(input("Starting balance: "))
oAccount = Account(userName, userPassword, userBalance)

# insert the new user in the dictionary
accountsDict[counter] = oAccount

# using the new object
print(accountsDict[2].show())
accountsDict[2].withdraw(700)
print(accountsDict[2].show())