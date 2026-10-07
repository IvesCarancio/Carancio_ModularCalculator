
#  This is the Function for addition
def add(num1, num2):
    return num1 + num2


# This is the Function for subtraction
def subtract(num1, num2):
    return num1 - num2


# This is the Function for multiplication
def multiply(num1, num2):
    return num1 * num2


#This is the Function for division
def divide(num1, num2):
    return num1 / num2


# This asks the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Asks the user to choose an operation
print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

# This Perform the selected operation
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
    print("Invalid choice.")
    exit()

# Displays the final answer
print(f"\nThe result of {operation} is: {result}")
