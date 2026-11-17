a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Choose an operation: ")
print("Addition (+)")
print("Subtraction (-)")
print("Multiplication (*)")
print("Division (/)")

operator = input("Enter your choice: ")

if operator == "+":
    print("Result: ", a + b)

elif operator == "-":
    print("Result: ", a -b)

elif operator == "*":
    print("Result: ", a * b)

elif operator == "/":
    if b != 0:
        print("Result: ", a / b)

    else:
            print("Error! cannot be divide by zero.")

else:
    print("Invalid operator.")
