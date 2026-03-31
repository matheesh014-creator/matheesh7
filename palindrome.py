import os

def is_palindrome(s):
    return s == s[::-1]

# fixed input (no input() used)
user_input = "madam"

if is_palindrome(user_input):
    print("Palindrome")
else:
    print("Not Palindrome")

# secret check
secret = os.getenv("MY_SECRET")

if secret:
    print("Secret loaded successfully")
else:
    print("No secret found")