




class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        prev_num = None
        
        
        for num in sorted(nums):
            if prev_num == num:
                return True
            prev_num = num
            
            
        return False
    
    
    
    
tests = []

tests.append({
    "input": {
        "nums": [1,2,3,1]
    },
    "output": True
})


tests.append({
    "input": {
        "nums": [1,2,3,4]
    },
    "output": False
})


tests.append({
    "input": {
        "nums": [1,1,1,3,3,4,3,2,4,2]
    },
    "output": True
})


for test in tests:
    print(Solution().containsDuplicate(**test["input"]) == test["output"])