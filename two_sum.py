



class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        next_index = 1
        
        for i in nums:
            for j in nums[next_index:]:
                if i+j==target:
                    return [nums.index(i), nums.index(j, next_index)]
            
            next_index += 1
    
    

print(Solution().twoSum(nums = [3,3], target = 6))