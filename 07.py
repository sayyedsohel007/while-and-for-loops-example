# Calculate factorial of a number using for loop.
num=int(input("enter your number"))
factorial=1
for i in range (1,num+1):
    factorial=factorial*i
print("factorial of",num,"is",factorial)