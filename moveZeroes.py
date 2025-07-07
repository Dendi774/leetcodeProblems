




class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)
        return nums
    


    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
        
        return nums
        

    

tests = []

tests.append({
    "input": {
        "nums": [0,1,0,3,12]
    },
    "output": [1,3,12,0,0]
})


tests.append({
    "input": {
        "nums": [0]
    },
    "output": [0]
})


for test in tests:
    print(Solution().moveZeroes(**test["input"]) == test["output"])