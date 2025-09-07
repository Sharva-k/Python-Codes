n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
op=(input("Enter arimthetic operator('+' , '-' , '/' , '*'): "))
if "+" in op:
    print("Addition of given numbers is: ",n1+n2)
elif "-" in op:
    print("Subtraction of given numbers is: ",n1-n2)
elif "*" in op:
    print("Multiplication of given numbers is: ",n1*n2)
elif "/" in op:
    print("Division of given numbers is: ",n1/n2)