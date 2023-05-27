'''
Account creation just using variables (objects)
'''

from Main_Bank_VersionX import *
import os

os.system('clear')

# account creations
oJoesAccount = Account("Joe", "123", 500)
oMarysAccount = Account("Mary", "456", 1000)


############### using the objects####
oJoesAccount.show()
oMarysAccount.show()

oJoesAccount.deposit(100)
print("added money for Joe")
oMarysAccount.deposit(100)
print("added money for Mary")
print()
oJoesAccount.show()
oMarysAccount.show()

oJoesAccount.withdraw(50)
oJoesAccount.show()
#####################################