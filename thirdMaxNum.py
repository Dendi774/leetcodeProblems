




class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        
        nums_set = set(nums)
        
        if len(set(nums_set)) < 3:
            return max(nums_set)
        
        for i in range(2):
            nums_set.remove(max(nums_set))
        
        return max(nums_set)
    
    

tests = []


tests.append({
    "input": {
        "nums": [3,2,1]
    },
    "output": 1
})


tests.append({
    "input": {
        "nums": [1,2]
    },
    "output": 2
})


tests.append({
    "input": {
        "nums": [2,2,3,1]
    },
    "output": 1
})


for test in tests:
    print(Solution().thirdMax(**test["input"]) == test["output"])