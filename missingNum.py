




class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(0, len(nums)+1):
            if i not in nums:
                return i

    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pass
        
    
    
tests = []

tests.append({
    "input": {
        "nums": [3,0,1]
    },
    "output": 2
})


tests.append({
    "input": {
        "nums": [0,1]
    },
    "output": 2
})

tests.append({
    "input": {
        "nums": [9,6,4,2,3,5,7,0,1]
    },
    "output": 8
})


for test in tests:
    print(Solution().missingNumber(**test["input"]) == test["output"])