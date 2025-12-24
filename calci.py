def calculator():
    print("🧮 Welcome to Python Calculator!")
    print("Supported operations: +, -, *, /, %, **, //\n")

    while True:
        # Input numbers with validation
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.\n")
            continue

        # Input operation
        op = input("Enter operation (+, -, *, /, %, **, //): ").strip()

        # Perform calculation
        try:
            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                result = a / b
            elif op == '%':
                result = a % b
            elif op == '**':
                result = a ** b
            elif op == '//':
                result = a // b
            else:
                print("Invalid operation!\n")
                continue
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed!\n")
            continue

        print(f"Result: {a} {op} {b} = {result}\n")

        # Check if user wants to continue
        cont = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if cont != 'y':
            print("Thank you for using Python Calculator! Goodbye! 👋")
            break

if __name__ == "__main__":
    calculator()
