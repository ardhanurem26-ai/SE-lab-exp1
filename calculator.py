# ==========================================
#        SIMPLE PYTHON CALCULATOR
# ==========================================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def calculator():
    while True:
        print("\n================================")
        print("       PYTHON CALCULATOR")
        print("================================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        print("================================")

        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("\nCalculator Exited Successfully!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("\nInvalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("\nError: Please enter valid numbers.")
            continue

        if choice == "1":
            result = add(num1, num2)
            operation = "+"

        elif choice == "2":
            result = subtract(num1, num2)
            operation = "-"

        elif choice == "3":
            result = multiply(num1, num2)
            operation = "*"

        elif choice == "4":
            result = divide(num1, num2)
            operation = "/"

        print("\n--------------------------------")
        print(f"{num1} {operation} {num2} = {result}")
        print("--------------------------------")


# Start the calculator
calculator()
