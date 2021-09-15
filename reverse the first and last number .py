num = int(input("Enter the number :"))
a = []
for i in range(1,num+1):
    element = int(input("Enter the number of element ehich you wanted to add"))
    a.append(element)
temp = a[0]
a[0] = a[num-1]
a[num-1] = temp
print(a)
    
