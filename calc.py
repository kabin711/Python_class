a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = input("Enter operator (+,-,*,/): ")

def calc(a, b, c):
    if c == '+':
        result = a + b
    elif c == '-':
        result = a - b
    elif c == '*':
        result = a * b
    elif c == '/':
        if b != 0:
            result = a / b  
        else:
            return ("invalid input")      
    else:
        print("Error: Invalid operator")
        return None

    return result

result = calc(a, b, c)
if result is not None:
    print(f"The result of {a} {c} {b} is: {result}")
