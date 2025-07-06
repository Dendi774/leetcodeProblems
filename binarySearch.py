



class Solution(object):
    def binarySearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        low = 0
        high = len(nums)-1
        
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid

        return -1    
    
tests = []

tests.append({
    "input": {
        "nums": [-1,0,3,5,9,12],
        "target": 9
    },
    "output": 4
})


tests.append({
    "input": {
        "nums": [-1,0,3,5,9,12],
        "target": 2
    },
    "output": -1
})



for test in tests:
    print(Solution().binarySearch(**test["input"]) == test["output"])