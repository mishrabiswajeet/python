num=input()
n=0
str= " "
for i in num:
    if num.index(i) == n:
        str+=i
    n +=1
print(str)
