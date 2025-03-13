def calculator():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ")
        
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            if b == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = a / b
        else:
            print("Invalid operation. Please enter one of +, -, *, or /.")
            return
        
        print(f"The result is: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()