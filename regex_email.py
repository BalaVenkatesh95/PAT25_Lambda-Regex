'''
Python function to validate regex for email id
'''
import re
def validate_email_address(email_id):
    pattern = "^[a-z0-9.]+@[a-z0-9]+.+[a-z]{2,6}$"
    result = re.search(pattern, email_id)
    if result:
        return "SUCCESS : Email ID is valid"
    else:
        return "ERROR : Invalid Email ID"
email_id = "bvsh@gmail.com"
print(validate_email_address(email_id))

'''
Note:
re.search - search function as part of regex module with parameter of pattern and string
'''