name = input("Enter your name: ")

# Validate name
while not name.strip() or name.isnumeric():
    print("Please enter a non-empty, non-numeric name.")
    name = input("Enter your name: ")

email = input("Enter your email: ")
res = False  


if "@" in email:
    x = email.split("@")
    if len(x) == 2 and "." in x[1]:  
        domain_parts = x[1].split(".")
        if len(domain_parts) >= 2 and domain_parts[0] and domain_parts[-1]:
            res = True

print(f"Your name is {name} and your email is {res}.")