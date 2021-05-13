class Solution:
    def reverse(self, x: int) -> int:
        check=False
        if x<0:
            check= True
        string=str(abs(x))
        if check and int(string[::-1])<2147483647:
            return (-1*int(string[::-1]))
        elif int(string[::-1])<2147483648:
            return (int(string[::-1]))
        return 0    
