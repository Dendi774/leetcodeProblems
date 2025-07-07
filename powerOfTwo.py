import math




class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n > 0 and int(math.log2(n)) == math.log2(n):
            return True
        return False
    
    
    
tests = []


tests.append({
    "input": {
        "n": 1
    },
    "output": True
})


tests.append({
    "input": {
        "n": 16
    },
    "output": True
})


tests.append({
    "input": {
        "n": 3
    },
    "output": False
})


tests.append({
    "input": {
        "n": -16
    },
    "output": False
})


tests.append({
    "input": {
        "n": 32
    },
    "output": True
})


tests.append({
    "input": {
        "n": 8
    },
    "output": True
})


#print(Solution().isPowerOfTwo(**tests[len(tests)-1]["input"]))
for test in tests:
    print(Solution().isPowerOfTwo(**test["input"]) == test["output"])
