# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        que = deque([p])
        s = deque([q])

        while que:
            for i in range(len(que)):
                node = que.popleft()
                nodes = s.popleft()
                # checks if they are both NULL
                if node is None and nodes is None:
                    continue
                if node is None or nodes is None or node.val != nodes.val:
                    return False
                que.append(node.left)
                que.append(node.right)
                s.append(nodes.left)
                s.append(nodes.right)
        return True
