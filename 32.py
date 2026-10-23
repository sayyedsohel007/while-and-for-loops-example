attendance = float(input("Enter attendance percentage: "))
marks = int(input("Enter marks: "))

if attendance >= 75 and marks >= 40:
    print("Eligible for exam")
else:
    print("Not eligible for exam")