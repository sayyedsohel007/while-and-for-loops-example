while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Program ended")
        break

    if choice >= 1 and choice <= 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == 1:
            print("Sum:", a + b)
        elif choice == 2:
            print("Difference:", a - b)
        else:
            print("Product:", a * b)
    else:
        print("Invalid choice")