# linux_iptables.py

"""
Description:
    Get details about Linux iptables.


Author:
    Nishant Krishna

Created:
    14 January, 2023
"""
import pyptables


class LinuxIptables:
    def check_linux_iptables(self):
        # Print the iptable entries
        linux_iptables = pyptables.default_tables()
        print('iptables entries: ', linux_iptables.to_iptables())

        # Now let's add a new rule into
        forward_rules = linux_iptables['filter']['FORWARD']
        forward_rules.append(pyptables.Accept(proto='tcp', dport='443'))

        # Write the rules to make them persistent
        print('Persisting the rules...')
        pyptables.restore(linux_iptables)

        # Now check if the rules are written in the
        print('Updated iptables entries: ', linux_iptables.to_iptables())


if __name__ == "__main__":
    iptables = LinuxIptables()
    iptables.check_linux_iptables()
