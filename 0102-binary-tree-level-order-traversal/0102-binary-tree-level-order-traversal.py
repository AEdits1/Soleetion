# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        levelval = []
        q = deque([root,None])
        while q:
            cur = q.popleft()
            if cur is None:
                res.append(levelval)
                levelval = []
                if q:
                    q.append(None)
                else:
                    break
            else:
                levelval.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return res