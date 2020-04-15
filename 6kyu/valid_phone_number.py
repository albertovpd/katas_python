# valid phone number

import re
def validPhoneNumber(phoneNumber):
    if re.fullmatch('\(\d{3}\)\s\d{3}\-\d{4}', phoneNumber):
        return True
    else:
        return False