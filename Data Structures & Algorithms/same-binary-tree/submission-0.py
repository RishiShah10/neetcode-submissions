# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pq = deque([p])
        qq = deque([q])

        while pq and qq:
            pcurrent = pq.popleft()
            qcurrent = qq.popleft()

            if not pcurrent and not qcurrent:
                continue

            if not pcurrent or not qcurrent:
                return False

            if pcurrent.val != qcurrent.val:
                return False

            pq.append(pcurrent.left)
            pq.append(pcurrent.right)
            qq.append(qcurrent.left)
            qq.append(qcurrent.right)

        return len(pq) == len(qq)