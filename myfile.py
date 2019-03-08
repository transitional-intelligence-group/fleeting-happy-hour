
import sys

CURRENT_BALANCE = 0


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

def view_balance():
    clean_credits = 0
    clean_debits = 0
    with open('project_data.txt') as f:
        transactions = f.read().split('\n')
        for item in transactions:
            if item.startswith('+'):
                clean_credits += float(item.strip('+'))
                # print(clean_credits)
                #CURRENT_BALANCE += float(item.strip('+'))
                # sum_clean_credits = sum(clean_credits)
                # print(sum_clean_credits)
            elif item.startswith('-'):
                clean_debits += float(item.strip('-'))
                # print(clean_debits)
    CURRENT_BALANCE = clean_credits - clean_debits
    print()
    final_balance = '${:,.2f}'.format(CURRENT_BALANCE)
    print('Your current balance is:', final_balance)
    print()
    display_menu()

#print(CURRENT_BALANCE)

def withdraw():
    print()
    # withdraw_amount = input('How much would you like to withdraw? ')
    try:
        withdraw_amount = input('How much would you like to withdraw? ')
    except:
        print()
        print('What you entered was not a valid number. Try again.')
        print()
        display_menu()
    try:
        withdrawal = float(withdraw_amount)
    except:
        print()
        print('What you entered was not a valid number. Try again.')
        print()
        display_menu()
    with open('project_data.txt', 'a+') as f:
        f.write('-'+str(withdrawal)+'\n')
    print()
    print('Transaction recorded.')
    display_menu()


# def deposit():
#     print()
#     try:
#         deposit_amount = input('How much would you like to deposit? ')
#     except:
#         print()
#         print('What you entered was not a valid number. Try again.')
#         print()
#         display_menu()
#     try:
#         deposit = float(deposit_amount)
#     except:
#         print()
#         print('What you entered was not a valid number. Try again.')
#         print()
#         display_menu()
#     with open('project_data.txt', 'a+') as f:
#         f.write('+'+str(deposit)+'\n')
#     print()
#     print('Transaction recorded.')
#     display_menu()


# def record_transaction(withdrawal):
#     with open('project_data.txt', 'a+') as f:
#         f.write('-'+str(withdrawal)+'\n\n')
#     print()
#     print('Transaction recorded.')
#     display_menu()

# def record_transaction(deposit):
#     with open('project_data.txt', 'a+') as f:
#         f.write('+'+str(deposit)+'\n\n')
#     print()
#     print('Transaction recorded.')
#     display_menu()

def exit_program():
    print()
    print('Exiting. Thank you, goodbye!')
    print()
    sys.exit()

welcome()
display_menu()
