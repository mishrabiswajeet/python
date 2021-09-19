class Solution:
    def convertToBase7(self, num: int) -> str:
        rem=0
        output=[]
        check = False     #check = True num=7
        if num < 0: #num = -7
            check = True
            num = num*(-1)  
        elif num==0:
            return str(num)
        while num!=0:
            rem=num%7
            num=num//7
            output.append(str(rem))

        output.reverse()
        output=''.join(output)
        if check:
            return '-'+str(output)
        return str(output)
