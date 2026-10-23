age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))

if age >= 18 and age <= 65 and weight >= 50:
    print("Eligible based on these criteria")
else:
    print("Not eligible based on these criteria")