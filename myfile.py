
import sys

def welcome():
def display_menu():
    pass
def view_balance():
    pass
def withdraw(money):
    pass
def deposit():
    pass

welcome()
dislay_menu()
while True:
    if user_input == '1':
        view_balance()
    elif user_input == '2':
        withdraw()
    elif user_input == '3':
        deposit()
    elif user_input == '4':
        sys.exit()
    else:
        print()
        print('ERROR. Invalid input, enter 1-4 only.')
        print()
    display_menu()