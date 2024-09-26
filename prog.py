# Program to sum two numbers

# Function to sum two numbers
def sum_two_numbers(num1, num2):
    return num1 + num2

# Input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Calculating the sum
result = sum_two_numbers(number1, number2)

# Displaying the result
print("The sum of", number1, "and", number2, "is:", result)
