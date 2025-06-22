


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        """ Removes all occurences of val in a list of integers """
        
        num_of_val = 0
        
        while val in nums:
            num_of_val+=1
            nums.remove(val)
            nums.append("_")
            
        return len(nums)-num_of_val, nums
    
    

print(Solution().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))