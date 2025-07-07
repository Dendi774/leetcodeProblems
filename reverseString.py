




class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for i in range(len(s)-2, -1, -1):
            curr = s.pop(i)
            s.append(curr)
    
        return s


    def reverseString2(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        s = s[::-1]
    
        return s
    
    
tests = []

tests.append({
    "input": {
        "s": ["h","e","l","l","o"]
    },
    "output": ["o","l","l","e","h"]
})


tests.append({
    "input": {
        "s": ["H","a","n","n","a","h"]
    },
    "output": ["h","a","n","n","a","H"]
})


for test in tests:
    print(Solution().reverseString(**test["input"]))
    print(Solution().reverseString2(**test["input"]) == test["output"])