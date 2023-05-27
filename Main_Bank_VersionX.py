'''
ATM Account - Class
Withdrawing cash, Depositing money, Balance, quit
'''

class Account():
    def __init__(self, name:str, password:str, balance:int):
        self.balance = balance
        self.password = password
        self.name = name
        self.withdraw_choice = ["1", "2", "3", "4", "5", "6", "7"]
        self.withdraw_nums = {
            "1": 10,
            "2": 20,
            "3": 40,
            "4": 50,
            "5": 60,
            "6": 80,
            "7": 100
        }

    def show(self):
        return self.balance
    
    def deposit(self, n:int, pw:str):
        if pw == self.password:
             self.balance += n
        else:
             print("Wrong password, program ended")
             quit()
             
    def withdraw(self, n):
        self.balance -= n