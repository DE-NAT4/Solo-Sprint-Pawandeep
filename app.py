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
        new_user = input("What is the new user's name:  ")
        active_users.append(new_user)

    elif navigation_input == 2:
        print_accounts(active_users, disabled_users)

    elif navigation_input == 3:
        account_status_change(active_users, disabled_users)
        print_accounts(active_users, disabled_users)

    if navigation_input == 0:
        app_is_running = 'False'


    

