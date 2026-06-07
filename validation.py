import re
from datetime import datetime

def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    return bool(
        re.match(pattern, email)
    )

def validate_dob(dob):
    return dob <= datetime.today().date()

def validate_number(value):
    try:
        float(value)
        return True
    except:
        return False
