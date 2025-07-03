



class Solution:
    def isValidPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # copy of the original string, which will be the converted string
        s_copy = ""
        
        
        for letter in s:
            if letter.isalnum():
                s_copy += letter
    
        if s_copy.lower() == s_copy[::-1].lower():
            return True
        return False



tests = []


tests.append({
    "input": {
        "s": "A man, a plan, a canal: Panama"
    },
    "output": True
})


tests.append({
    "input": {
        "s": "race a car"
    },
    "output": False
})


tests.append({
    "input": {
        "s": " "
    },
    "output": True
})


for test in tests:
    print(Solution().isValidPalindrome(**test["input"]) == test["output"])