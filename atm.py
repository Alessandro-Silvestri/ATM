'''
Withdrawing cash, Depositing money, Balance, quit
'''

class Atm():
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print(self.balance)
    
    def deposit(self, n):
        self.balance += n
    
    def withdraw(self, n):
        if n > self.balance:
            print(f"the maximum withdraw is: {self.balance}")
        elif n <= 0:
            print("It's not possible to insert 0 ora a negative number")
        else:
            self.balance -= n

    def home_screen(self):
        print('''
                            #################################
                            #             ATM               #
                            #################################

                            1) withdraw
                            2) deposit
                            3) view balance
                            4) quit
        ''')   

atm = Atm(1500)
atm.home_screen()
