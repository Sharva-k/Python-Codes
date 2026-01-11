def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def div(n1,n2):
    if n2!=0:
        return n1/n2
    else:
        return "Error cannot divide with 0"

operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : div,
}

should_accumulate = True
num1 = float(input("What is the first number: "))
while should_accumulate:
    
    for symbol in operations:
        print(symbol)
    op = input("Pick an operation: ")
    num2 = float(input("What is the second number: "))
    ans = operations[op](num1,num2)
    print(f"{num1} {op} {num2} = {ans}")

    choice = input(f"Type y to continue claculating with {ans} , or type n to exit: ")
    if choice == "y":
        num1 =ans
    else:
        should_accumulate = False
