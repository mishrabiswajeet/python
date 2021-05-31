
def nextPrime(num):
    while True:
        num+=1
        for i in range(2,num):
            if num%i==0:
                break
        else:
            return num
def PrimeProducer(n):
    num=1
    count=1
    while count<=n:
        num=nextPrime(num)
        yield num
        count+=1
N=int(input("Enter the prime number which you want to print"))
L=[x for x in PrimeProducer(N)]
print(L)
