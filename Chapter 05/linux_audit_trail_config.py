# linux_audit_trail_config.py

"""
Description:
    Enables audit for few files in Linux

Author:
    Nishant Krishna

Created:
    02 August, 2022
"""


import platform
import subprocess


class LinuxAuditTrailConfig:
    def get_config(self, config):
        if platform.system() == 'Linux':
            output = subprocess.check_output('auditctl -l', shell=True)
            output_list = output.decode('utf-8').split('\n')

            # Print all the audit config
            print('All audit config:')
            print(output_list, '\n')

            # Find out if the audit config is present for supplied config
            for config_item in output_list:
                if config in config_item:
                    print('Audit config for ', config, ' found:')
                    print(config_item)

        else:
            print('This program can only be run on Linux')


if __name__ == "__main__":
    linux_audit_trail_config = LinuxAuditTrailConfig()
    linux_audit_trail_config.get_config('passwd')
