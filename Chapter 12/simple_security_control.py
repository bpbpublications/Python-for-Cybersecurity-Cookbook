# simple_security_control.py

"""
Description:
    A simple security control which reads /etc/login.defs and print the security weakness in the configuration.

Author:
    Nishant Krishna

Created:
    12 February, 2023
"""


import platform
import subprocess


class SimpleSecurityControl:
    PASS_MAX_DAYS_POLICY = 60
    PASS_MIN_DAYS_POLICY = 1
    PASS_WARN_AGE_POLICY = 7

    def check_config(self):
        if platform.system() == 'Linux':
            output = subprocess.check_output('grep \'^PASS\' /etc/login.defs', shell=True)
            output_list = output.decode('utf-8').split('\n')

            # Print all the login.defs config
            print('Password configuration from login.def:')
            print(output_list, '\n')

            # Find out if the configurations are as per the policy
            num_failed_check = 0
            for config_item_line in output_list:
                config_item = config_item_line.split('\t')

                if (config_item[0] == 'PASS_MAX_DAYS') and int(config_item[1]) > int(self.PASS_MAX_DAYS_POLICY):
                    print('Config Item: ', config_item[0], '\tExpected Value: ',
                          self.PASS_MAX_DAYS_POLICY, '\tFound Value: ', config_item[1])
                    num_failed_check += 1
                elif (config_item[0] == 'PASS_MIN_DAYS') and int(config_item[1]) < int(self.PASS_MIN_DAYS_POLICY):
                    print('Config Item: ', config_item[0], '\tExpected Value: ',
                          self.PASS_MIN_DAYS_POLICY, '\tFound Value: ', config_item[1])
                    num_failed_check += 1
                elif (config_item[0] == 'PASS_WARN_AGE') and int(config_item[1]) > int(self.PASS_WARN_AGE_POLICY):
                    print('Config Item: ', config_item[0], '\tExpected Value: ',
                          self.PASS_WARN_AGE_POLICY, '\tFound Value: ', config_item[1])
                    num_failed_check += 1

            if (num_failed_check > 0):
                print('\nNo. of failed checks: ', num_failed_check)

        else:
            print('This program can only be run on Linux')


if __name__ == "__main__":
    security_control = SimpleSecurityControl()
    security_control.check_config()
