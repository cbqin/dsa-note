# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

#  

# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回：

# [3,9,20,15,7]


from typing import List
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        ans = list()
        if not root:
            return ans

        q = deque([root])
        while q:
            node = q.popleft()
            ans.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans
