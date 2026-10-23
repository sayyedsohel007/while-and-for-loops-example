password = input("Enter password: ")

if len(password) >= 8:
    if password.isalnum():
        print("Valid password")
    else:
        print("Password must contain only letters and numbers")
else:
    print("Password must have at least 8 characters")