status = input("Enter result status (pass/fail): ").lower()

match status:
    case "pass":
        print("Congratulations! You passed.")
    case "fail":
        print("Better luck next time.")
    case _:
        print("Invalid result status")