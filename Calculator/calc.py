def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def floor_division(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x // y

def power(x, y):
    return x ** y

print("Simple Calculator")

while True:
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Power")
    print("7. Exit")

    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4','5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            result = floor_division(num1, num2)
        elif choice == '6':
            print("Result:", power(num1, num2))
    elif choice == '7':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a valid choice (1/2/3/4/5/6/7).")
