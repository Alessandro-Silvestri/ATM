'''
Bank Management with intercative menu'
'''

from Main_Bank_VersionX import *
import os

while True:
    # interactive menu 
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press o to open a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()
    user_input = input('What do you want to do? ')
    user_input = user_input.lower()
    user_input = user_input[0] # grab the first letter
    print()

    if user_input == "1": # Choice 1: withdraw
        os.system('clear')
        atm.home_withdraw()
        user_input = input("> ")
        
        if user_input in atm.withdraw_choice:
            atm.withdraw(atm.withdraw_nums.get((user_input)))
            atm.view_balance()
    
        elif user_input == "8":
            print('other choice')
            while True:
                # I ask the amount and I check if it is more than the funds
                user_input = int(input('write the amount: '))
                if user_input > atm.balance:
                    print('Not sufficient funds')
                    continue
                elif user_input == 0 or user_input < 0:
                    print("wrong input")
                    continue
                else:
                    atm.withdraw(user_input)
                    atm.view_balance()
                    break
        else:
            print("wrong choice")
        
    elif user_input == "2": # Choice 2: deposit
        user_input = int(input('Deposit: write the amount: '))
        atm.deposit(user_input)
        atm.view_balance()

    elif user_input == "b": # Choice 3: view balance
        atm.view_balance()

    elif user_input == "q": # Choice 4: quit
        print('Thank you, bye')
