"Code to check that a User Name meet certain criterias before being accepted"
"""Criterias:
1. username must be at least 2 characters long.
2. It can begin with an alphabet or number but must end with a number

"""
import re
class Users:
    def UserID(self):
        box = []
        username = input("Please insert your Username in the right format: ")
        pattern = '[a-zA-Z0-9]+\d$'
        x = re.findall(pattern, username, re.IGNORECASE)
        box.append(username)

        if x == box:
            print("Username is valid")
        if x!=box:
            print("Username not valid, Try again")
            print("Your username must start with at least a string and end with a number")
usersname=Users()
print("Test 1: ")
usersname.UserID()
# Test 2
print("Test 2: ")
usersname.UserID()
print("Test 3: ")
usersname.UserID()
print("Test 4: ")
usersname.UserID()
