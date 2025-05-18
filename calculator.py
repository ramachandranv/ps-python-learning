run = True

def get_operator():
    print("Select the operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    op = input("Enter the option from 1-6 or 'q' to quit: ")
    if op == 'q':
        return None
    else:
        return int(op)

def get_operands():
    num1 = int(input("Enter the value for num1: "))
    num2 = int(input("Enter the value for num2: "))
    return num1, num2

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def mod(num1, num2):
    return num1 % num2

def power(num1, num2):
    return num1 ** num2

def calc(op, num1, num2):
    if op == 1:
       return add(num1, num2)
    elif op == 2:
       return sub(num1, num2)
    elif op == 3:
       return mul(num1, num2)
    elif op == 4:
       return div(num1, num2)
    elif op == 5:
       return mod(num1, num2)
    elif op == 6:
       return power(num1, num2)
        

def calculator():
    global run
    try:
        op = get_operator()
        if (op is None):
            run = False
            print("Thanks for using calculator!")
        elif op in range(1, 7):
            a, b = get_operands()
            result = calc(op, a, b)
            print("Result:", result)
        else:
            print("Enter the options from 1-6")
        
    except ValueError as ve:
        print("Enter a valid input", str(ve))
    except ZeroDivisionError as zde:
        print("Division by zero is not possible. Please enter a valid input", str(zde))

print("Welcome to the calculator!")
while(run):
    calculator()