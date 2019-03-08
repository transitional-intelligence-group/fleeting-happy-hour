
import sys

def welcome():
    print('******* Welcome to your checkbook *******')
    
def display_menu():
    print(''' 
    What would you like to do?

    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit
    ''')
    user_input = input('Enter choice: ')
    
    if user_input == '1':
        view_balance()
    elif user_input =='2':
        withdraw()
    elif user_input == '3':
        deposit()
    elif user_input == '4':
        exit_program()
    else:
        print()
        print('ERROR. Invalid input; try again.')
        print()
        display_menu()

# def view_balance():
#     with open('project_data.txt') as f:
#         balance = f.read().split('\n')
#         for line in balance:
#             if line.startswith('+'):
#                 line.strip([+])
#         new_bal = [int(line) for line in balance]

#         print(sum(balance))

# view_balance()



def view_balance():
    print('view_balance invoked.')
    pass



# def withdraw():
#     print()
#     # withdraw_amount = input('How much would you like to withdraw? ')
#     try:
#         withdraw_amount = input('How much would you like to withdraw? ')
#     except:
#         print()
#         print('What you entered was not a valid number. Try again.')
#         print()
#         display_menu()
#     try:
#         withdrawal = float(withdraw_amount)
#     except:
#         print()
#         print('What you entered was not a valid number. Try again.')
#         print()
#         display_menu()
#     with open('project_data.txt', 'a+') as f:
#         f.write('-'+str(withdrawal)+'\n')
#     print()
#     print('Transaction recorded.')
#     display_menu()


def deposit():
    print()
    try:
        deposit_amount = input('How much would you like to deposit? ')
    except:
        print()
        print('What you entered was not a valid number. Try again.')
        print()
        display_menu()
    try:
        deposit = float(deposit_amount)
    except:
        print()
        print('What you entered was not a valid number. Try again.')
        print()
        display_menu()
    with open('project_data.txt', 'a+') as f:
        f.write('+'+str(deposit)+'\n')
    print()
    print('Transaction recorded.')
    display_menu()


# def record_transaction(withdrawal):
#     with open('project_data.txt', 'a+') as f:
#         f.write('-'+str(withdrawal)+'\n\n')
#     print()
#     print('Transaction recorded.')
#     display_menu()

def record_transaction(deposit):
    with open('project_data.txt', 'a+') as f:
        f.write('+'+str(deposit)+'\n\n')
    print()
    print('Transaction recorded.')
    display_menu()

def exit_program():
    print()
    print('Exiting. Thank you, goodbye!')
    print()
    sys.exit()

welcome()
display_menu()
