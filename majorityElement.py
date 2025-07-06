




class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums_set = set(nums)
        
        for num in nums_set:
            if nums.count(num) > len(nums) // 2:
                return num
    
    
tests = []

tests.append({
    "input": {
        "nums": [3,2,3]
    },
    "output": 3
})


tests.append({
    "input": {
        "nums": [2,2,1,1,1,2,2]
    },
    "output": 2
})


for test in tests:
    print(Solution().majorityElement(**test["input"]) == test["output"])