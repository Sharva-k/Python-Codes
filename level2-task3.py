import re
def strong (password):
    strength=0
    msg=[]
    if len(password)>=8:
        strength+=1
    else:
        msg.append("Password must contain 8 or more than 8 characters!")
    
    if re.search(r"[a-z]",password):
        strength+=1
    else:
        msg.append("Password must contain small case letters!")
    
    if re.search(r"[A-Z]",password):
        strength+=1
    else:
        msg.append("Password must contain upper case letters!")

    if re.search(r"\d",password):
        strength+=1
    else:
        msg.append("Password must contain digits!")

    if re.search(r"[!@#$%^&*-_(),.?><;':{}]",password):
        strength+=1
    else:
        msg.append("Password must contain special characters!")
    if strength == 5:
        return "Strong password!"
    elif 3 <= strength < 5:
        return "Moderate password. Suggestions:\n" + "\n".join(msg)
    else:
        return "Weak password. Improve it by:\n" + "\n".join(msg)



userpassword=input("Enter you password to check strength: ")
print(strong(userpassword))