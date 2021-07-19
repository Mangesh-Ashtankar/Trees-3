# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        stack = []
        if root:
            stack.append((root.val, root, [root.val]))
        else:
            return []
        
        paths = []
            
        while len(stack):
            currentSum, currentNode, currentPath = stack.pop()
            
            
            children = [currentNode.left, currentNode.right]
            
            if not any(children):
                if currentSum == sum:
                    paths.append(currentPath)
            
            for c in children:
                if c:
                    stack.append((currentSum+c.val, c, currentPath+[c.val]))
                    
        return paths
