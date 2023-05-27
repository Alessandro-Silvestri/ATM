'''
Account creation putting all the in a list
'''

from Main_Bank_VersionX import *
accounts_list = []

# objects creation and adding in the list
oAccount = Account("Joe", "123", 1000)
accounts_list.append(oAccount)

oAccount = Account("Mary", "456", 800)
accounts_list.append(oAccount)

# using the objects
# the indexes are the bank account number
accounts_list[1].show()
accounts_list[0].show()
accounts_list[0].deposit(50, accounts_list[0].password)
accounts_list[0].show()

# creating the object with user input and then putting in the list
userName = input("Creating another account,  Name: ")
userPassword = input("Insert password: ")
userBalace = int(input("Start balance: "))

oAccount = Account(userName, userPassword, userBalace)
accounts_list.append(oAccount)

# using the last object
accounts_list[2].show()
accounts_list[2].deposit(150, accounts_list[2].password)
accounts_list[2].show()