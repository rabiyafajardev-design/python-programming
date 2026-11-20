integer = int(input("Enter a number: "))
if integer > 0:
    print("Positive number.")
elif integer < 0:
    print("Negative number.")
else:
    print("Zero.")

if integer % 2 == 0:
    print("Even number.")
else:
    print("Odd number.")
