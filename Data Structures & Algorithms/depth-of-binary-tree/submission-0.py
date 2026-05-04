# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        do a bfs from root keep a counter on rounds
        return counter
        """
        level = 0
        if root == None:
            return 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                top = q.popleft()
                if top.left != None:
                    q.append(top.left)
                if top.right != None:
                    q.append(top.right)
            level += 1
        return level
        