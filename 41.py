n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total = total + i * i

print("Sum of squares:", total)