"""
Name : HimakarRaju Gunda
Date : 03-07-2024
Trainer Name : Saynam

Description of program :
Regular Expressions:
Write a function `extract_emails(text)` that takes a string and
returns a list of all email addresses found in the string using regular expressions.

    Example Input:
    ```python
    import re
    def extract_emails(text):
        # Your code here
    text = "Please contact us at support@example.com or sales@example.com."
    print(extract_emails(text))  # Output: ['support@example.com', 'sales@example.com']
    ```
"""
import re

# Regular expression pattern to match email addresses
mailID_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

text = "Contact us at support@example.com or call +1-800-123-4567. For sales, email sales@example.com."

# Find all email addresses in the text
ids = re.findall(mailID_pattern, text)
print(ids)
