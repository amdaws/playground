def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

def calculator():
    print("Welcome to the Calculator App!")
    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
        print("The result is:", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("The result is:", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("The result is:", result)
    elif choice == '4':
        result = divide(num1, num2)
        print("The result is:", result)
    else:
        print("Invalid choice")

calculator()