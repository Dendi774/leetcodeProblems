




class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math
        
        return True if math.sqrt(num).is_integer() else False
    
    
tests = []


tests.append({
    "input": {
        "num": 16
    },
    "output": True
})


tests.append({
    "input": {
        "num": 14
    },
    "output": False
})


tests.append({
    "input": {
        "num": 0
    },
    "output": True
})


tests.append({
    "input": {
        "num": 1
    },
    "output": True
})


tests.append({
    "input": {
        "num": 9
    },
    "output": True
})


tests.append({
    "input": {
        "num": 9
    },
    "output": True
})


tests.append({
    "input": {
        "num": 256
    },
    "output": True
})

tests.append({
    "input": {
        "num": 113
    },
    "output": False
})

for test in tests:
    print(Solution().isPerfectSquare(**test["input"]) == test["output"])