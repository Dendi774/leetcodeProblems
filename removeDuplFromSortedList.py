




# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        return self.array_to_linkedList(sorted(list(set(self.linkedList_to_array(head)))))

    
    
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
        "head": Solution().array_to_linkedList([1, 1, 2])
    },
    "output": [1,2]
})


tests.append({
    "input": {
        "head": Solution().array_to_linkedList([1,1,2,3,3])
    },
    "output": [1,2,3]
})



for test in tests:
    print(Solution().deleteDuplicates(**test["input"]) == test["output"])