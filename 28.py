num = int(input("Enter a number: "))
original = num
total = 0
digits = len(str(abs(num)))

while num > 0:
    digit = num % 10
    total = total + digit ** digits
    num = num // 10

if original >= 0 and total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")