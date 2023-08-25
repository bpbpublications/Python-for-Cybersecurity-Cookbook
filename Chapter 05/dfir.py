# dfir.py

"""
Description:
    This is a rudimentary Digital Forensics and Incident Response (DFIR) for checking the content of the directory and the checksums of their files.


Author:
    Nishant Krishna

Created:
    05 August, 2022
"""

import os
import hashlib
import csv
import psutil

# Set the location of output file to the current directory
__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))


class Dfir:
    def generate_fingerprints(self) -> None:
        """Generate fingerprints (checksums) of all the Python files in the current directory
        """
        file_list = os.listdir()
        checksums = open('checksums.csv', 'w')
        checksums_writer = csv.writer(checksums, delimiter=',')

        for file_name in file_list:
            # We will generate the fingerprints of only Python files for now
            if file_name.endswith('.py'):
                with open(file_name, 'r') as file:
                    plain_text = file.read()
                    hashed_text = hashlib.sha256(plain_text.encode()).hexdigest()
                    print(file_name, ',', hashed_text)
                    checksums_writer.writerow([file_name, hashed_text])

    def compare_finterprints(self) -> bool:
        """Compares the fingerprints (checksum) of all the Python files in the current diretory with what was generated before and shows if the results are ok or they don't match
        """
        mismatch_found = False
        file_list = os.listdir()
        checksums = open('checksums.csv', 'r')
        checksums_reader = csv.reader(checksums, delimiter=',')

        # Create a dictionary out of the CSV file of all the checksums so that we can easily compare the values
        mydict = {rows[0]: rows[1] for rows in checksums_reader}

        for file_name in file_list:
            if file_name.endswith('.py'):
                with open(file_name, 'r') as file:
                    plain_text = file.read()
                    hashed_text = hashlib.sha256(plain_text.encode()).hexdigest()
                    if (mydict[file_name] == hashed_text):
                        print(file_name, ': OK')
                    else:
                        print(file_name, ': Mismatch')
                        mismatch_found = True

        return mismatch_found

    def get_last_logins_not_current_user(self, authorised_user) -> bool:
        """Find out if the any of the logged in users are not same as the specified user

        Returns:
            _type_: _description_
        """
        unauthorised_user_found = False

        # Get a list of tuples containing all the current (logged in) users
        current_users = psutil.users()

        for user in current_users:
            if (user[0]) != authorised_user:
                print('Unauthorised user found: ', user[0])
                unauthorised_user_found = True
            else:
                print((user[0]), ' is an authorised user')

        return unauthorised_user_found


if __name__ == "__main__":
    response = Dfir()
    # response.generate_fingerprints()

    if (response.compare_finterprints()):
        print('---- Fingerprint mismatch found\n')
    else:
        print('---- No fingerprint mismatch found\n')

    if (response.get_last_logins_not_current_user('nishant')):
        print('Unauthorised user found\n')
    else:
        print('---- No unauthorised user found\n')
