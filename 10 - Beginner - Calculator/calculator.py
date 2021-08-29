def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {"+": add, "-": sub, "*": mul, "/": div}

num1 = int(input("Type the first number: "))
num2 = int(input("Type the second number: "))
operation = input(f"Type the operation {' '.join(x for x in operations.keys())}: ")

function = operations[operation]
result = function(num1, num2)

print(f"{num1} {operation} {num2} = {result}")

