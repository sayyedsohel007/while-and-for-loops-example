num = abs(int(input("Enter a number: ")))
smallest = 9

while num > 0:
    digit = num % 10

    if digit < smallest:
        smallest = digit

    num = num // 10

print("Smallest digit:", smallest)