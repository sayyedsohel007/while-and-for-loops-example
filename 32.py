base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1

for i in range(exp):
    result = result * base

print("Answer:", result)