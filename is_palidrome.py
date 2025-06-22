


class Solution:
    def isPalindromeStrConversion(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        """ Converts the integer to string """
        if str(x)==str(x)[::-1]:
            return True
        return False


    def isPalindromeNoStrConversion(self, x):
        """
        :type x: int
        :rtype: bool
        """
    
        """ Algorithm: no string conversion """
        
        

        


print(Solution().isPalindromeStrConversion(x = 1234321))
        