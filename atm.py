'''
Withdrawing cash, Depositing money, Balance, quit
'''

class Atm():
    def __init__(self, balance):
        self.balance = balance
        self.withdraw_nums = {
            "1": 10,
            "2": 20,
            "3": 40,
            "4": 50,
            "5": 60,
            "6": 80,
            "7": 100
        }

    def view_balance(self):
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

                            (1) withdraw
                            (2) deposit
                            (3) view balance
                            (4) quit
        ''')

    def home_withdraw(self):
            print('''
                            #################################
                            #            WITHDRAW           #
                            #################################

                            (1) 10 £              60 £  (5)
                            (2) 20 £              80 £  (6)     
                            (3) 40 £              100 £ (7)
                            (4) 50 £              other (8)
            ''')

atm = Atm(1500)
atm.home_screen()


user_input = input("> ")
if user_input == "1":
    pass
elif user_input == "2":
    pass
elif user_input == "3":
    atm.view_balance()
elif user_input == "4":
    pass
