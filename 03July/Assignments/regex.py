"""
Name : HimakarRaju Gunda
Date : 03-07-2024
Trainer Name : Saynam

Description of program :
find the emails in the text

text = "Contact us at support@example.com or call +1-800-123-4567. For sales, email sales@example.com."
expected op - ['support@example.com', 'sales@example.com']
"""
import re

# Regular expression pattern to match email addresses
mailID_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

text = "Contact us at support@example.com or call +1-800-123-4567. For sales, email sales@example.com."

# Find all email addresses in the text
ids = re.findall(mailID_pattern, text)
print(ids)
