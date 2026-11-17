name = input("Enter your name: ")
marks = float(input("Enter marks out of 100: "))
attendance = int(input("Enter your attendance percentage: "))
print("Name: ", name)
print("Marks: ", marks)
print("Attendance percentage ", attendance)

if marks >= 80 and attendance >= 75:
    print("Congratulations! You are eligible for a scholarship.")

else:
    print("Sorry! You do not meet the scholarship requirements.")