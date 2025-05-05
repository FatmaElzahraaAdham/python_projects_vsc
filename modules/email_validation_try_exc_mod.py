import re

def validate_email(email):
    try:
        if not email or email[-1] == '.':
            raise ValueError("Email cannot end with a dot")
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValueError("Invalid email format")
        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False

while True:
    try:
        name = input("Enter your name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty")
        if name.isnumeric():
            raise ValueError("Name cannot be just numbers")
        break
    except ValueError as e:
        print(f"Invalid name: {e}")

while True:
    try:
        email = input("Enter your email: ").strip()
        if validate_email(email):
            break
    except Exception as e:
        print(f"An error occurred: {e}")

print(f"\nRegistration Successful!")
print(f"Name: {name}")
print(f"Email: {email}")