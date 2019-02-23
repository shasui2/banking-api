import os

accountName = ''
accountId = ''
balance = 0
previousTransaction = 0


def cls():
    os.system("clear")


def main(cname, cid):
    accountName = cname
    accountId = cid
    showMenu()


def deposit(amount):
    global balance, previousTransaction
    balance += amount
    previousTransaction = amount


def withdraw(amount):
    global balance, previousTransaction
    balance = balance - amount
    previousTransaction = -amount


def getPreviousTransaction():
    if previousTransaction > 0:
        print('You deposited: ', previousTransaction)
    elif previousTransaction < 0:
        print('You withdrew: ', previousTransaction)
    else:
        print('There is no transaction.')


def showMenu():
    print('--------------------------------------')
    print('National Bank of Jamie')
    print('--------------------------------------')
    print('A. Check Balance')
    print('B. Deposit')
    print('C. Withdraw')
    print('D. Previous Transaction')
    print('E. Exit')
    print('--------------------------------------')
    option = ''
    amount = 0

    while option != 'e':
        option = input('Select an option:')
        if option == 'a':
            print('Your balance is: ', balance)
        elif option == 'b':
            try:
                amount = int(input('Enter amount of deposit:'))
                deposit(amount)
            except ValueError:
                print('Not a valid number!')
        elif option == 'c':
            try:
                amount = int(input('Enter amount of withdraw:'))
                withdraw(amount)
            except ValueError:
                print('Not a valid number!')
        elif option == 'd':
            getPreviousTransaction()
        elif option == 'e':
            print('************************************')
        else:
            print('Option invalid! Please try again!')

    print('Thank you for using our service!')


main("MyAccount", "xyz-001")
