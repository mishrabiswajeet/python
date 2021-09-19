def sumofnumber(arr,value):
    s = set()
    for i in arr:
        if (value-i) in s:
            print((value-i) , i)
        else:
            s.add(i)
            
arr = list(map(int,input().split()))
value = int(input())
sumofnumber(arr,value)
