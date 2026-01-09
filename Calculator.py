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

num1 = float(input("What is the first number: "))
for symbol in operations:
    print(symbol)
op = input("Pick an operation: ")
num2 = float(input("What is the second number: "))
ans = operations[op](num1,num2)
print(f"{num1} {op} {num2} = {ans}")