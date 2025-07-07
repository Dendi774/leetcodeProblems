




class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        ans = []
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        
        for i in (nums1_set if len(nums1_set) < len(nums2_set) else nums2_set):
            if i in (nums2 if len(nums1) < len(nums2) else nums1) and i not in ans:
                for j in range(nums1.count(i) if nums1.count(i) < nums2.count(i) else nums2.count(i)):
                    ans.append(i)

        return ans
    


tests = []

tests.append({
    "input": {
        "nums1": [1,2,2,1],
        "nums2": [2,2]
    },
    "output": [2,2]
})


tests.append({
    "input": {
        "nums1": [4,9,5],
        "nums2": [9,4,9,8,4]
    },
    "output": [4,9]
})


for test in tests:
    print(Solution().intersect(**test["input"]) == test["output"])