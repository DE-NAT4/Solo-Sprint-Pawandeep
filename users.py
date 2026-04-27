#                      FUNCTIONS 
# =========================================================
import csv

# DEF CREATE ACTIVE USERS LIST
def create_active_user_list():
    result = []
    with open('users.csv', mode='r', newline='') as data:
        reader = csv.reader(data)
        for row in reader:
            if row[0] == 'Active':
                result.append(row[1])
    return result

# DEF CREATE DISABLED USERS LIST
def create_disabled_user_list():
    result = []
    with open('users.csv', mode='r', newline='') as data:
        reader = csv.reader(data)
        for row in reader:
            if row[0] == 'Disabled':
                result.append(row[1])
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

# DEF ADD NEW USER ACCOUNT TO ENABLED LIST


# DEF DISABLE A USER ACCOUNT - REMOVE FROM ENABLED LIST AND ADD TO DISABLED


# DEF ENABLE A USER ACCOUNT - REMOVE FROM DISABLED LIST AND ADD TO ENABLED


# DEF PRINT USER ACCOUNT NAMES
def print_accounts(activelist, disabledlist):
    print('''
        USER MANAGEMENT SYSTEM'
           - VIEW ACCOUNTS -'
          ''')
    print(f'Active Accounts:')
    for name in activelist:
        print(f' > {name}')

    print(f'\nDisabled Accounts:')
    for name in disabledlist:
        print(f' > {name}')

# DEF ADD ALL ACCOUNT TYPES TO USERS.CSV
#         DATA STRUCTURE:
#               - ENABLED, USER_NAME
#               - ENABLED, USER_NAME
#               - ENABLED, USER_NAME
#               - DISABLED, USER_NAME
#               - DISABLED, USER_NAME
#               - ETC


