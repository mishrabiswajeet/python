class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = str(bin(N))[2:]
        complement_str = ''
        for i in binary:
            if i == '0':
                complement_str += '1'
            else:
                complement_str += '0'
        complement_num = 0
        exp = len(complement_str)-1
        for i in complement_str:
            complement_num += pow(2,exp)*int(i)
            exp -= 1
        
        return complement_num
