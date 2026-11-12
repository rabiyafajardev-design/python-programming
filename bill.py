name = input("Enter your name: ")
movie_name = input("Enter your movie name: ")
a = float(input("Enter the price of one ticket: "))
b = int(input("Enter number of tickets you want: "))
c = float(input("Enter total cost of snacks: "))

ticket_cost = a*b
total_bill = ticket_cost + c

print("name: ", name)
print("movie name: ", movie_name)
print("ticket cost: " , ticket_cost)
print("snack cost: ", c )
print("final bill: ", total_bill)