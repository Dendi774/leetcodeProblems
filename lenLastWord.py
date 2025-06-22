


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        return len(s.strip()[s.strip().rfind(" ")+1:])



print(Solution().lengthOfLastWord(s = "   fly me   to   the moon  "))