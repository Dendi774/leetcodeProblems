


class Solution:
    def quickSort(self, array, l=None, r=None):
        
        if l >= r:
            return
        p = self.partition(array, l, r)
        
        self.quickSort(array, l, p-1)
        self.quickSort(array, p+1, r)
        

    def partition(self, array, l, r):
        pivot = array[r]
        i = l - 1
        for j in array[:r-1]:
            if j < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        
        array[i+1], array[r] = array[r], array[i+1]
        return i+1



print(Solution().quickSort([5,4], 0, 1))