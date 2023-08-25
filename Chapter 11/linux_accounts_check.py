# linux_accounts_check.py

"""
Description:
    Get details about Linux accounts and privileges.


Author:
    Nishant Krishna

Created:
    15 January, 2023
"""

import grp
import pwd
import os


class LinuxAccounts:
    def check_linux_accounts(self):
        # Get details about all the users and all the groups defined on the system
        print('\nlist of users: \n', pwd.getpwall())
        print('List of groups: \n', grp.getgrall())

        # Get details about one user
        print('\nDetails about a single user:')
        print('UID: ', pwd.getpwnam('nishant').pw_uid)
        print('Name: ', pwd.getpwnam('nishant').pw_name)
        print('GID: ', pwd.getpwnam('nishant').pw_gid)
        print('Shell: ', pwd.getpwnam('nishant').pw_shell)
        print('Home directory: ', pwd.getpwnam('nishant').pw_dir)

        # Get details about user's groups
        print('Groups: ', os.getgrouplist('nishant', pwd.getpwnam('nishant').pw_gid))


if __name__ == "__main__":
    accounts = LinuxAccounts()
    accounts.check_linux_accounts()
