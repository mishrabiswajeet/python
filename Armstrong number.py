num=int(input("Enter the number:"))
sum = 0
temp = num
while num>0:
    remainder = num % 10
    sum +=remainder**3
    num//=10
if sum == temp:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
