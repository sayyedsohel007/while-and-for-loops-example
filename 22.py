num = abs(int(input("Enter a number: ")))
total = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        total = total + digit

    num = num // 10

print("Sum of even digits:", total)