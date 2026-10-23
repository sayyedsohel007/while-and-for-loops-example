num = int(input("Enter a number: "))
original = num
total = 0

while num > 0:
    digit = num % 10
    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    total = total + fact
    num = num // 10

if original >= 0 and total == original:
    print("Strong number")
else:
    print("Not a strong number")