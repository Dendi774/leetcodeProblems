




class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        subStr_index = 1
        curr_subStr = ""
        
        while len(s[:subStr_index]) <= len(s)//2:
            while len(curr_subStr) < len(s):
                curr_subStr += s[:subStr_index]
            
            if curr_subStr == s:
                return True
            
            curr_subStr = ""
            subStr_index += 1
        
        return False
    
tests = []

tests.append({
    "input": {
        "s": "abab"
    },
    "output": True
})


tests.append({
    "input": {
        "s": "aba"
    },
    "output": False
})


tests.append({
    "input": {
        "s": "abcabcabcabc"
    },
    "output": True
})

tests.append({
    "input": {
        "s": "bb"
    },
    "output": True
})


for test in tests:
    print(Solution().repeatedSubstringPattern(**test["input"]) == test["output"])