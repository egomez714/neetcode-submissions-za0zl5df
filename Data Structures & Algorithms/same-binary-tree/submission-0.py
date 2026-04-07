# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
        fQ = deque([p])
        sQ = deque([q])
        while fQ:
            for i in range(len(fQ)):
                node = fQ.popleft()
                nodeTwo = sQ.popleft()
                if node is None and nodeTwo is None:
                    continue
                if nodeTwo is None or node is None or node.val != nodeTwo.val:
                    return False
                fQ.append(node.left)
                fQ.append(node.right)
                sQ.append(nodeTwo.left)
                sQ.append(nodeTwo.right)
        return True
                    