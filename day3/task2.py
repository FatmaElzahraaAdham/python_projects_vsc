def email_validation(email):
    #res = False
    if "@" in email:
        x = email.split("@")
        if len(x) == 2 and "." in x[1]:  
            domain_parts = x[1].split(".")
            if len(domain_parts) >= 2 and domain_parts[0] and domain_parts[-1]:
                return True
            else:
                return False
            
    else: 
        print("enter a valid email")


email = input("Enter your email: ")


print(f"Your email is {email_validation(email)}.")