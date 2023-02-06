'''
Withdrawing cash, Depositing money, Balance, quit
'''

class Atm():
    def __init__(self):
        self.balance = 2000

    def show_balance(self):
        print(self.balance)
    
    def deposit(self, n):
        self.balance += n
    
    def withdraw(self, n):
        self.balance -= n
    

atm = Atm()
atm.show_balance()
atm.deposit(500)
atm.show_balance()
atm.withdraw(100)
atm.show_balance()
