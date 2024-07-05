def palindrome(text):
    if text == text[::-1]:                  # Check if the string is a palindrome
        return f"The string {text} is a palindrome\n"
    else:
        return f"The string {text} is not a palindrome\n"


print(palindrome("cat"))
print(palindrome("tot"))
