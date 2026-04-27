from users import *

active_users = create_active_user_list()
disabled_users = create_disabled_user_list()
print_accounts(active_users, 'Active')
print_accounts(disabled_users, 'Disabled')
