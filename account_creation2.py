'''
Account creation asking the user tu insert data
'''
from Main_Bank_VersionX import *
userName = input("Bank account creation: Insert your name: ")
userPassword = input("Insert password: ")
userBalance = int(input("Insert a start balance: "))


# using the object account
userAccont = Account(userName, userPassword, userBalance)
userAccont.show()
userAccont.deposit(100, "123")
userAccont.show()

