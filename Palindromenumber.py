n=int(input("Enter the number"))
temp=n
rev_num=0
while n>                                                                                                             0:
    remainder=n%10
    rev_num=(rev_num*10)+remainder
    n=n//10
print(rev_num)

if temp==rev_num:
    print("Palindrome number")
else:
    print("Not a palindrome number")
