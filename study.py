plan = float(input("Enter planned study time: "))
time = float(input("Enter how many minutes you studied: "))

remaining_time = (plan - time)
extra_time = (time - plan)

if time == plan:
    print("Daily goal achieved!")

elif time > plan:
    print("You studied extra: ", extra_time, "minutes")

else:
    print(remaining_time)
    print("Keep going! You can achieve your goal.")
