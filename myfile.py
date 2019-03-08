
# import sys

# def welcome():
#     print('******* Welcome to your checkbook *******')
    
# def display_menu():
#     print(''' 
#     What would you like to do?

#     1) view current balance
#     2) record a debit (withdraw)
#     3) record a credit (deposit)
#     4) exit
#     ''')

def view_balance():
    with open('project_data.txt') as f:
        balance = f.read().split('\n')
        for line in balance:
            if line.startswith('+'):
                line.strip([+])
        new_bal = [int(line) for line in balance]

        print(sum(balance))

view_balance()





# def withdraw(money):
#     pass
# def deposit():
#     pass

# welcome()
# display_menu()
# while True:
#     if user_input == '1':
#         view_balance()
#     elif user_input == '2':
#         withdraw()
#     elif user_input == '3':
#         deposit()
#     elif user_input == '4':
#         sys.exit()
#     else:
#         print()
#         print('ERROR. Invalid input, enter 1-4 only.')
#         print()
#     display_menu()