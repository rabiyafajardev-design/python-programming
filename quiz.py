name = input("Enter name: ")
marks = float(input("Enter marks out of 10: "))
print("Name: ", name)
print("Marks ", marks)

if not(0 <= marks <= 10):
    print("Invalid marks! Enter marks between 0 and 10.")

elif 9 <= marks <= 10:
    print("Excellent performance! perfect score.")

elif 6 <= marks < 9:
    print("Congratulations! You passed.")

else:
    print("You need more practice. Try again!")