




class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        
        
        return len(max("".join(str(num) for num in nums).split("0")))
    

tests = []


tests.append({
    "input": {
        "nums": [1,1,0,1,1,1]
    },
    "output": 3
})

tests.append({
    "input": {
        "nums": [1,0,1,1,0,1]
    },
    "output": 2
})


tests.append({
    "input": {
        "nums": []
    },
    "output": 0
})

tests.append({
    "input": {
        "nums": [1]
    },
    "output": 1
})

tests.append({
    "input": {
        "nums": [0]
    },
    "output": 0
})

for test in tests:
    print(Solution().findMaxConsecutiveOnes(**test["input"]) == test["output"])