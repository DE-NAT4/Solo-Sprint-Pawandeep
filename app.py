from users import *

# =========================================================
# INITIALISATION 


active_users = create_active_user_list()
disabled_users = create_disabled_user_list()


# =========================================================

app_is_running = True
while app_is_running == True:

    # NAVIGATION MENU
    navigation_menu()
    navigation_input = int(input('Please enter an index:  '))


    if navigation_input == 1:
        pass

    # ELIF 2: LIST ACCOUNTS
        # USER INPUT: VIEW ACTIVE OR DISABLED ACCOUNTS

    # ELIF 3: ENABLE/DISABLE USER
        # USER INPUT: ENABLE OR DISABLE
        # VIEW ACCOUNTS
        # USER INPUTS: SELECT ACCOUNT

    if navigation_input == 0:
        app_is_running = 'False'
    

