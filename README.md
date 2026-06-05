# Solo-Sprint-Pawandeep
Solo sprint project to create a user account management system at the terminal.

## Planning
### app.py
from users import *

# =========================================================
# INITIALISATION 


active_users = create_active_user_list()
disabled_users = create_disabled_user_list()
print_accounts(active_users, 'Active')
print_accounts(disabled_users, 'Disabled')


# =========================================================



# NAVIGATION MENU

# CLIENT INPUT

# ELIF 1: ADD USER

# ELIF 2: LIST ACCOUNTS
    # USER INPUT: VIEW ACTIVE OR DISABLED ACCOUNTS

# ELIF 3: ENABLE/DISABLE USER
    # USER INPUT: ENABLE OR DISABLE
    # VIEW ACCOUNTS
    # USER INPUTS: SELECT ACCOUNT

# ELIF 4: EXIT

### users.py
#           FUNCTIONS 
# =============================================


# DEF ADD NEW USER ACCOUNT TO ENABLED LIST


# DEF DISABLE A USER ACCOUNT - REMOVE FROM ENABLED LIST AND ADD TO DISABLED


# DEF ENABLE A USER ACCOUNT - REMOVE FROM DISABLED LIST AND ADD TO ENABLED


# DEF PRINT USER ACCOUNT NAMES


# DEF ADD ALL ACCOUNT TYPES TO USERS.CSV
#         DATA STRUCTURE:
#               - ENABLED, USER_NAME
#               - ENABLED, USER_NAME
#               - ENABLED, USER_NAME
#               - DISABLED, USER_NAME
#               - DISABLED, USER_NAME
#               - ETC

