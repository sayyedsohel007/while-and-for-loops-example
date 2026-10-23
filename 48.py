print("1. English")
print("2. Hindi")
print("3. Marathi")

choice = int(input("Select language: "))

match choice:
    case 1:
        print("You selected English")
    case 2:
        print("You selected Hindi")
    case 3:
        print("You selected Marathi")
    case _:
        print("Invalid choice")