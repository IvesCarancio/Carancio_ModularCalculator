def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2



def multiply(num1, num2):
    return num1 * num2



def divide(num1, num2):
    return num1 / num2



num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user to choose an operation
print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")


if choice == "1":
    result = add(num1, num2)
    operation = "addition"

elif choice == "2":
    result = subtract(num1, num2)
    operation = "subtraction"

elif choice == "3":
    result = multiply(num1, num2)
    operation = "multiplication"

elif choice == "4":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        exit()
    result = divide(num1, num2)
    operation = "division"

else:
    print("This is invalid.")
    exit()

# Display the final answer
print(f"The result of {operation} is: {result}")
