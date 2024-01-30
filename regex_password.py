'''
Python function to validate regex for  16 character alphanumeric password
with uppercase, lowercase, numbers, special characters
'''

import re
def validate_password(password):
    pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@$!%*?&#])[A-Za-z0-9@$#!%*?&]{16}$"
    result = re.search(pattern, password)
    if result:
        return "SUCCESS: Password combination is valid"
    else:
        return "ERROR: Password combination is not correct"

password = "hustle@ABCDE#202"
print(validate_password(password))

'''
Note:
(?=) is used for look ahead assertion, which asserts somewhere in input
provided condition is present
*. - wildcard used for all characters
re.search - search function as part of regex module with parameter of pattern and string
'''