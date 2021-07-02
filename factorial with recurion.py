def recur_fact(n):
    if n == 1:
        return n
    else:
        return n*recur_fact(n-1)
num = int(input("Enter the number:"))
if num < 0:
    print("Sorry factorial is not for negative number")
elif num == 0:
    print("fact of ",num,"is",1)
else:
    print("The factorial of",num,"is",recur_fact(num))
