num = int(input("Enter the number :"))
temp = num
if num>1:
    for i in range(2,num):
        if num % i == 0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")
    
    
  ## Prime number for the certian interval:


lower = int(input("Enter lower range:"))
upper = int(input("Enter upper range:"))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)

    
    
   





