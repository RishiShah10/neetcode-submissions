# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        q = deque([root])
        while q:
            top = q.popleft()
            temp = top.left
            top.left,top.right = top.right,temp
            if top.left != None:
                q.append(top.left)
            if top.right != None:
                q.append(top.right)
        return root

        