"""
Python function to validate regex for  bangladesh mobile number
1.) It comprise of 11 digits
2.) The first two digit is always 01,followed by next 3 digit as operator number(054) and
last 6 digits
"""
import re
def validate_ban_mobile_number(mobile_number):
    pattern = "^[0]{1}[1]{1}[054]{3}[0-9]{6}$"
    result = re.search(pattern, mobile_number)
    if result:
        return "SUCCESS : Valid Bangladesh Number"
    else:
        return "ERROR : Invalid Mobile Number"


mobile_number = "01054456789"

print(validate_ban_mobile_number(mobile_number))
