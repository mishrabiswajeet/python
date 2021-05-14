class Solution:
    def isPalindrome(self, x: int) -> bool:
        string=str(x)
        if string[::-1]==str(x):
             return (True)
        else:
             return (False)   
