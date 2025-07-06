


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def findSum(self, head):
        
        if head == None:
            return 0
        return head.data + self.findSum(head.left) + self.findSum(head.right)
        
        
        