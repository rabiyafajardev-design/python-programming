marks = float(input("Enter marks out of 100: "))
attendance = int(input("Enter attendance percentage: "))

if 0 <= marks > 100 or 0 <= attendance > 100:
    print("Invalid input!")

elif marks >= 80 and attendance >= 75:
    print("Congratulations! you qualify for scholarship.")

else:
    print("You do not qualify for scholarship.")