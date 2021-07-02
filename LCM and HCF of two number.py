# LCM of two number #

import math
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c=math.lcm(a,b)
print(c)




# LCM of two number using function #


a = int(input("Enter the first value of a:"))
b = int(input("Enter the second value of b:"))
if a>b:
    maximum = a
else:
    maximum = b
while True:
    if maximum % a == 0 and maximum % b == 0:
        print("\n LCM of {0} and {1} = {2}".format(a,b,maximum))
        break
    maximum+=1



