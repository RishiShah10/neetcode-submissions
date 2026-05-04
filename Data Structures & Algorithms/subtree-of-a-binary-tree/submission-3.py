# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        explore the values of a tree when we see the starting value of the subroot we enter a equal checking
        function
        """
        def checkIfEqual(root,subRoot):
            firstq = deque([root])
            secondq = deque([subRoot])
            while firstq or secondq:
                firstNode = firstq.popleft()
                secondNode = secondq.popleft()
                if firstNode == None and secondNode == None:
                    continue
                if firstNode == None or secondNode == None:
                    return False
                if firstNode.val != secondNode.val:
                    return False
                firstq.append(firstNode.left)
                firstq.append(firstNode.right)
                secondq.append(secondNode.left)
                secondq.append(secondNode.right)        
            return len(firstq) == len(secondq)
        q = deque([root])
        while q:
            current = q.popleft()
            if current == None:
                continue
            if current.val == subRoot.val:
                if checkIfEqual(current,subRoot):
                    return True
            q.append(current.left)
            q.append(current.right)
        return False

        