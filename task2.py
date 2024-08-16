# Example email list 
email_list = [
    'jdoe@hr.company.com',
    'asmith@it.company.com',
    'mjones@fin.company.com',
    'bwhite@mkt.company.com',
    'kgreen@ops.company.com',
    'invalid@xyz.company.com'
]
import re

def validate_email(email):
    pattern = r'^[a-z]\w*@(?:hr|it|fin|mkt|ops)\.company\.com$'
    if re.match(pattern, email):
        print(f"Email '{email}' is valid.")
        return True
    else:
        print(f"Email '{email}' is invalid.")
        return False

def get_department(email):
    if validate_email(email):
        department = email.split('@')[1].split('.')[0]
        return department
    return None

def categorize_emails(email_list):
    categories = {'hr': [], 'it': [], 'fin': [], 'mkt': [], 'ops': []}
    for email in email_list:
        if validate_email(email):
            department = get_department(email)
            if department:
                categories[department].append(email)
    return categories

# Test the categorize_emails function
categorized_emails = categorize_emails(email_list)
print(categorized_emails)