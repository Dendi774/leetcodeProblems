



class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        digits = [int(digit) for digit in str(int("".join(str(digit) for digit in digits))+1)]
        
        return digits
        
        

print(Solution().plusOne(digits = [1]))