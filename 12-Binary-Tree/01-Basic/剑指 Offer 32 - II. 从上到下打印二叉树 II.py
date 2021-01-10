# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

#  

# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：

# [
#   [3],
#   [9,20],
#   [15,7]
# ]


from typing import List
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            size = len(q)
            temp = []
            for _ in range(size):
                pop = q.popleft()
                temp.append(pop.val)
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
            ans.append(temp)
        return ans
