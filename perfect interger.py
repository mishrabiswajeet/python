num = int(input("Enter the number:"))
sum = 0
temp = num
for i in range(1,num):
    if num % i == 0:
        sum = sum + i
if sum == temp:
    print(sum,"Perfect Number")
else:
    print(sum,"Not a perfect Number")
