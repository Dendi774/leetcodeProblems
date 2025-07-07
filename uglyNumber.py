




class Solution:
    def isUgly(self, n: int) -> bool:
        pass
    
    
tests = []


tests.append({
    "input": {
        "n": 6
    },
    "output": True
})

tests.append({
    "input": {
        "n": 1
    },
    "output": True
})


tests.append({
    "input": {
        "n": 14
    },
    "output": False
})


tests.append({
    "input": {
        "n": 100231
    },
    "output": False
})


for test in tests:
    print(Solution().isUgly(**test["input"]) == test["output"])