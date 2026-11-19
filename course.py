# Grocery Shop Billing System

name = input("Enter customer name: ")          # 1
phone = input("Enter phone number: ")          # 2
bill = input("Enter bill number: ")            # 3
date = input("Enter bill date: ")              # 4
p1 = input("Enter product 1 name: ")            # 5
q1 = int(input("Enter product 1 quantity: "))  # 6
price1 = float(input("Enter product 1 price: ")) # 7
p2 = input("Enter product 2 name: ")            # 8
q2 = int(input("Enter product 2 quantity: "))  # 9
price2 = float(input("Enter product 2 price: ")) # 10

total1 = q1 * price1
total2 = q2 * price2
total = total1 + total2

print("\n--- Grocery Shop Bill ---")
print("Customer Name:", name)
print("Phone Number:", phone)
print("Bill Number:", bill)
print("Date:", date)
print(p1, ":", total1)
print(p2, ":", total2)
print("Total Amount:", total)

# Save details to file
with open("grocery.txt", "a") as f:
    f.write(f"{name}, {phone}, {bill}, {date}, {p1}, {q1}, {price1}, {p2}, {q2}, {price2}, {total}\n")

print("Bill saved successfully!")