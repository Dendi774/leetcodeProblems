




class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        test_string = ""
        
        if needle in haystack:
            for letter_index, letter in list(enumerate(haystack)):
                if letter == needle[0]:
                    for inner in haystack[letter_index:]:
                        test_string+=inner
                        if len(test_string)==len(needle) and test_string==needle:
                            return letter_index
                    test_string=""
            
        
        else:
            return -1
    

print(Solution().strStr(haystack = "sadbutsad", needle = "bu"))
