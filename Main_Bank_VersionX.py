'''
ATM Account - Class
Withdrawing cash, Depositing money, Balance
'''

class Account():
    def __init__(self, name:str, password:str, balance:int):
        self.balance = balance
        self.password = password
        self.name = name

    def show(self):
        return self.balance
    
    def deposit(self, n:int):
        self.balance += n
             
    def withdraw(self, n):
        self.balance -= n