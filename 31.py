num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive and even")
    else:
        print("Positive but odd")
else:
    print("Not a positive number")