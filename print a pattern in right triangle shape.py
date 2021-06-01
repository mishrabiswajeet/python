num=int(input("Enter the number of rows:"))
for i in range(num):
    var=i+1
    dec = num-1
    for j in range(i+1):
        print(var,end=" ")
        var = var+dec
        dec = dec-1
    print()
