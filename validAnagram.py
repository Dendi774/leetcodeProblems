




class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return "".join(letter for letter in sorted(list(s))) == "".join(letter for letter in sorted(list(t)))
    
    
    def isAnagram2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        for letter in s:
            if s.count(letter) != t.count(letter):
                return False

        return True
    
tests = []


tests.append({
    "input": {
        "s": "anagram",
        "t": "nagaram"
    },
    "output": True
})


tests.append({
    "input": {
        "s": "rat",
        "t": "car"
    },
    "output": False
})


tests.append({
    "input": {
        "s": "a",
        "t": "ab"
    },
    "output": False
})


for test in tests:
    print(Solution().isAnagram2(**test["input"]) == test["output"])