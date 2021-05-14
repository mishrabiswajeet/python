class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num=3
        if n==1 or n==3:
             return (True)
        while(num<=n):
            num*=3
            if num==n:
                return (True)
                break
        else:
            return(False)
