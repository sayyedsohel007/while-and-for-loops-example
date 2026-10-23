num = abs(int(input("Enter a number: ")))
product = 1

if num == 0:
    product = 0
else:
    while num > 0:
        digit = num % 10
        product = product * digit
        num = num // 10

print("Product of digits:", product)