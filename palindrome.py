# Function to check palindrome
def is_palindrome(value):
    value = str(value)  # Convert to string
    if value == value[::-1]:
        return True
    else:
        return False

# Taking input from user
user_input = input("Enter a string or number: ")

# Checking result
if is_palindrome(user_input):
    print("It is a palindrome ✅")
else:
    print("Not a palindrome ❌")