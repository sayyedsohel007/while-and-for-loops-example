num = int(input("Enter a number: "))

for i in range(1, abs(num) + 1):
    if num != 0 and num % i == 0:
        print(i)