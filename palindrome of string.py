string=input()
str=string.casefold()
if list(str) == list(str[::-1]):
    print("palindrome")
else:
    print("Not a palindrome number")
