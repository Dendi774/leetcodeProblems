




class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        position = 0
        
        while position+1 < len(nums):
            
            if nums[position] == nums[position+1]:
                nums.pop(position)
                nums.pop(position)
                continue
            
            elif nums[position] < nums[position+1]:
                return nums[position]
        
        return nums[position]
            
        
tests = []


tests.append({
    "input": {
        "nums": [2,2,1]
    },
    "output": 1
})


tests.append({
    "input": {
        "nums": [4,1,2,1,2]
    },
    "output": 4
})


tests.append({
    "input": {
        "nums": [1]
    },
    "output": 1
})


for test in tests:
    print(Solution().singleNumber(**test["input"]) == test["output"])