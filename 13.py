num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if original >= 0 and original == rev:
    print("Palindrome")
else:
    print("Not palindrome")