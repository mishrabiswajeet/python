#Fibnocci without recursion#

num =  int(input("How many times :"))
a , b = 0 , 1
count = 0
if num <=0:
    print("Enter the positive number :")
elif num == 1:
    print(a)
else:
    print("Fibnocci Series:")
    while count<num:
        print(a)
        sum = a + b
        a = b
        b = sum
        count+=1

        
        
#Fibnocci with recursion#

def recur_fibo(n):
    if n<=1:
        return n
    else:
        return recur_fibo(n-1)+recur_fibo(n-2)

num = int(input("Enter the number:"))

if num<0:
    print("Enter the positive number")
else:
    print("Fibnocci number :")
    for i in range(num):
        print(recur_fibo(i))


