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
        return "Error!"

def main():
    print("Select operation:")
    print("+. Add")
    print("-. Subtract")
    print("*. Multiply")
    print("/. Divide")

    choice = input("Enter choice (+ or - or * or /): ")
    if choice in ['+', '-', '*', '/']:
        try:
            value_1 = float(input("Enter first number: "))
            value_2 = float(input("Enter first number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return

        if choice == '+':
            print(f"{value_1} + {value_2} = {add(value_1, value_2)}")

        elif choice == '-':
            print(f"{value_1} - {value_2} = {subtract(value_1, value_2)}")

        elif choice == '*':
            print(f"{value_1} * {value_2} = {multiply(value_1, value_2)}")

        elif choice == '/':
            print(f"{value_1} / {value_2} = {divide(value_1, value_2)}")

    else:
        print("Invalid input. Please enter your choice from the given operations")

if __name__ == "__main__":
    main()
