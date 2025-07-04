

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        merged_linkedList = self.array_to_linkedList(sorted(self.linkedList_to_array(list1) + self.linkedList_to_array(list2)))
        
        return self.linkedList_to_array(merged_linkedList)

    
    def linkedList_to_array(self, node):
        if node is None:
            return []
        return [node.val] + self.linkedList_to_array(node.next)
    
    
    def array_to_linkedList(self, array, counter=0):
        
        if counter == len(array):
            return
        else:
            node = ListNode(array[counter])
            node.next = self.array_to_linkedList(array, counter+1)
        
        return node
    
    

tests = []


tests.append({
    "input": {
        "list1": Solution().array_to_linkedList([1, 2, 4]),
        "list2":  Solution().array_to_linkedList([1, 3, 4])
    },
    "output": [1,1,2,3,4,4]
})


tests.append({
    "input": {
        "list1":  Solution().array_to_linkedList([]),
        "list2":  Solution().array_to_linkedList([])
    },
    "output": []
})


tests.append({
    "input": {
        "list1": Solution().array_to_linkedList([]),
        "list2":  Solution().array_to_linkedList([0])
    },
    "output": [0]
})


for test in tests:
    print(Solution().mergeTwoLists(**test["input"]))
    print(Solution().mergeTwoLists(**test["input"]) == test["output"])