price = float(input("Enter the price of an item: "))
items = int(input("Enter the number of items you want to buy: "))
original_bill = (price * items)

if original_bill >= 1000:
    discount = (original_bill * 10 / 100)
else:
    discount = 0
final_bill = (original_bill - discount)

print("Original bill: ", final_bill)
print("Discount: ", discount)
print("Final bill: ", final_bill)