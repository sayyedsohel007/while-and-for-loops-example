print("1. Pizza")
print("2. Burger")
print("3. Biryani")
print("4. Sandwich")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("You selected Pizza")
    case 2:
        print("You selected Burger")
    case 3:
        print("You selected Biryani")
    case 4:
        print("You selected Sandwich")
    case _:
        print("Invalid choice")