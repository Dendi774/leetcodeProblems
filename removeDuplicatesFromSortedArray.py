



class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k = 0
        num_unique_elems = 0
        
        while True:
            for num in nums:
                if nums.index(num)<len(nums)-1 and num==nums[nums.index(num)+1]:
                    print(num)
                    k+=1
                    nums.remove(num)
                    break
                elif nums.index(num)>=len(nums)-1:
                    num_unique_elems=len(nums)
                    for duplicate in range(k):
                        nums.append("_")
                    return num_unique_elems, nums
                
                    
print(Solution().removeDuplicates(nums = [-1,0,0,0,0,3,3]))