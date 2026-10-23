age = int(input("Enter age: "))

if age < 5:
    print("Ticket is free")
elif age < 18:
    print("Ticket price: Rs. 50")
else:
    print("Ticket price: Rs. 100")