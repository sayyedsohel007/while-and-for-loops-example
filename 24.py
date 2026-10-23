text = input("Enter a string: ")
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count = count + 1

print("Total vowels:", count)