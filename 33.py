age = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))

if age >= 21 and salary >= 25000:
    print("Eligible to apply for loan")
else:
    print("Not eligible based on these criteria")