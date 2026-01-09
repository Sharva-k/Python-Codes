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

print(operations["*"](4,8))