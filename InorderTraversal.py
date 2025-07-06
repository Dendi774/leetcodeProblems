

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def inorderIterative(self, node):
        """ Traverses a binary tree iteratively """
        
        if node == None:
            return []
        return self.inorderIterative(node.left) + [node.data] + self.inorderIterative(node.right)
            

    def parse_tuple(self, data):
        """ helper function that converts a tuple with the structure (left_subtree, key, right_subtree) into binary tree """
        
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = self.parse_tuple(data[0])
            node.right = self.parse_tuple(data[2])
            
        elif data is None:
            node = None
        
        else:
            node = TreeNode(data)
            
        return node


    def tree_to_tuple(self, node):
        """ converts a binary tree back to a tuple with the structure (left_subtree, key, right_subtree) """
        
        if node is not None and (node.left is not None or node.right is not None):
            tree_tuple = (self.tree_to_tuple(node.left), node.key, self.tree_to_tuple(node.right))
        elif node is not None and (node.left is None and node.right is None):
            return node.key
        else:
            return node
        return tree_tuple




tree_tuple = ((1,3,None), 2, ((None,3,4), 5, (6,7,8)))
tree = Solution().parse_tuple(tree_tuple)

print(Solution().inorderIterative(tree))

    


