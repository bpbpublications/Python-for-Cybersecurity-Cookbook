# windows_accounts_check.py

"""
Description:
    Get details about Windows accounts and privileges.


Author:
    Nishant Krishna

Created:
    13 January, 2023
"""

import windows_tools.users as windows_users


class WindowsAccounts:
    def check_windows_accounts(self):
        # Use windows_tools to get various information about users
        print('Current user: ', windows_users.whoami())
        print('Is user admin: ', windows_users.is_admin())
        print('Is user local admin: ', windows_users.is_user_local_admin())
        print('PySID of the user: ', windows_users.get_pysid_from_username(windows_users.whoami()))
        print('Local group members:', windows_users.get_local_group_members(group_sid='S-1-5-32-545'))


if __name__ == "__main__":
    accounts = WindowsAccounts()
    accounts.check_windows_accounts()
