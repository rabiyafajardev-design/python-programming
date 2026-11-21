name = input("Enter your name: ")
units = int(input("Enter electricity units consumed: "))

if units <= 0:
    print("Invalid units entered.")

else:
    if units <= 100:
        rate = 5

    elif units <= 300:
        rate = 8

    else:
        rate = 10

electricity_cost = (units * rate)
bill = (electricity_cost + 50)

print("Name: ", name)
print("Units consumed: ", units)
print("Rate per unit: Rs. ", rate)
print("Electricity bill: Rs.", bill)
