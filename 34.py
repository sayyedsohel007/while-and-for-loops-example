text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome string")
else:
    print("Not a palindrome string")