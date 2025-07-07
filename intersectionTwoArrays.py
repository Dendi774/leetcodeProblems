




class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        nums1 = set(nums1)
        nums2 = set(nums2)

        for i in (nums1 if len(nums1) < len(nums2) else nums2):
            if i in (nums2 if len(nums1) < len(nums2) else nums1) and i not in ans:
                ans.append(i)
        return ans
    

tests = []


tests.append({
    "input": {
        "nums1": [1,2,2,1],
        "nums2": [2,2]
    },
    "output":[2]
})


tests.append({
    "input": {
        "nums1": [4,9,5],
        "nums2": [9,4,9,8,4]
    },
    "output":[4,9]
})


for test in tests:
    print(Solution().intersection(**test["input"]) == test["output"])