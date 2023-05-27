from Main_Bank_VersionX import *

# creating the dictionary and 2 bank accounts
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

# creating the menu'
while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press o to open a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()
    action = input("Choose an option: ")

    # administrator choices: "s", "o"
    # show accounts list
    if action == "s":
        print("***** Account list *****")
        for i, j in accountsDict.items():
            print(i, j.name)
        quit()
    # create a new account
    elif action == "o":
        print("***** New account *****")
        userName = input("Insert name: ")
        userPassword = input("Insert Password: ")
        userBalance = input("Insert start balance: ")
        accountsDict[counter] = Account(userName, userPassword, userBalance)
        print("New account list:")
        #show the new list account
        for i, j in accountsDict.items():
            print(i, j.name)
        quit()

    userBankaccount = int(input("Insert your bank account: ")) 
    # check if the bank account exists in the dictionary
    if not userBankaccount in accountsDict:
        print("The account doesn't exist \nProgram ended")
        quit()
    userPassword = input("Password: ")
    break

# check password
if accountsDict[userBankaccount].password != userPassword:
    print("Wrong password, \nProgram ended")
    quit()

objAccount = accountsDict[userBankaccount]
print(f"Hi {objAccount.name}")
print(f"Bank account n. {userBankaccount}")

# menu choices
if action == "b":
    # balance
    print("")
    print("***** BALANCE *****")
    print(objAccount.show())
    quit()
elif action == "d":
    # deposit
    print("***** deposit *****")
    userInput = int(input("Insert the amount to deposit: "))
    objAccount.deposit(userInput, objAccount.password)
    print(f"New balance: {objAccount.show()}")
elif action == "w":
    # withdrawal
    print("***** withdraw *****")
    userInput = int(input("Insert the withdrawal: "))
    objAccount.withdraw(userInput)
    print(f"New balance: {objAccount.show()}") 
    # quit
elif action == "q":
    print("***** Program ended *****")
    print("Program ended")
    quit()

