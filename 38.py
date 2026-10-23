m1 = int(input("Enter marks in subject 1: "))
m2 = int(input("Enter marks in subject 2: "))
m3 = int(input("Enter marks in subject 3: "))

if m1 >= 40 and m2 >= 40 and m3 >= 40:
    print("Passed all subjects")
else:
    print("Failed in one or more subjects")