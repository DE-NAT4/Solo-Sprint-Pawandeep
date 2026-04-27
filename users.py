#                      FUNCTIONS 
# =========================================================
import csv

def create_active_user_list():
    result = []
    with open('users.csv', mode='r', newline='') as data:
        reader = csv.DictReader(data)  
        for row in reader:
            if row['status'] == 'Active':  
                result.append(row) 
    return result


def create_disabled_user_list():
    result = []
    with open('users.csv', mode='r', newline='') as data:
        reader = csv.DictReader(data)  
        for row in reader:
            if row['status'] == 'Disabled': 
                result.append(row) 
    return result


def navigation_menu():
    print('''
        USER MANAGEMENT SYSTEM'
           - Main Menu -'
          
    > 1: Add User
    > 2: View Active/Disabled Accounts
    > 3: Enable/Disable an Account
    > 0: Exit 
          ''')


def account_status_change(active_users, disabled_users):
    print('''
        USER MANAGEMENT SYSTEM'
      - Change Account Statuses -' 
          ''')
    attempting = True
    while attempting == True:
        print("To DISABLE an account, please enter 0")
        option = int(input("To ENABLE an account, please enter 1: \n"))
        if option == 0:
            print_account(active_users, 'Active')
            target = int(input("\nPlease enter the index of the account to DISABLE:  "))
            try:
                name = active_users.pop(target)
                disabled_users.append(name)
                attempting = False
            except:
                print('''
        USER MANAGEMENT SYSTEM'
             - ERROR -' 
          ''')
                print("Invalid entry, please try again.")
            
        elif option == 1:
            print_account(disabled_users, 'Disabled')
            target = int(input("Please enter the index of the account to ENABLE:  "))
            try:
                name = disabled_users.pop(target)
                active_users.append(name)
                attempting = False
            except:
                print('''
        USER MANAGEMENT SYSTEM'
             - ERROR -' 
          ''')
                print("Invalid entry, please try again.")
        else:
            print('''
        USER MANAGEMENT SYSTEM'
             - ERROR -' 
          ''')
            print("Invalid entry, please try again.")


# DEF PRINT USER ACCOUNT NAMES
def print_accounts(activelist, disabledlist):
    print('''
        USER MANAGEMENT SYSTEM'
           - VIEW ACCOUNTS -'
          ''')
    print(f'Active Accounts:')
    for i in range(len(activelist)):
        print(f'{i} > {activelist[i]}')

    print(f'\nDisabled Accounts:')
    for i in range(len(disabledlist)):
        print(f'{i} > {disabledlist[i]}')

def print_account(list, status):
    print('''
        USER MANAGEMENT SYSTEM'
           - VIEW ACCOUNTS -'
          ''')
    print(f'{status} Accounts:')
    for i in range(len(list)):
        print(f'{i} > {list[i]}')

def save_data(active_users, disabled_users):
    data = [['status', 'name', 'password']]
    for name in active_users:
        data.append([name])
    for name in disabled_users:
        data.append([name])
    
    with open('users.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


