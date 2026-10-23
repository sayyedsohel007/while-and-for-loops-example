text = input("Enter a string: ")
count = 0

for ch in text.lower():
    if ch.isalpha() and ch not in "aeiou":
        count = count + 1

print("Total consonants:", count)