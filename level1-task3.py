email=input("Enter your email: ")
def check_email(mail):
    if email.count("@" and ".")!=1:
        return False
    name,domain = email.split("@")
    if name and domain and "." in domain:
        return True
    else:
        return False
output=check_email(email)
print(f"Your email value is {output}")