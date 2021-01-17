#
# @lc app=leetcode.cn id=1302 lang=python3
#
# [1302] 层数最深叶子节点的和
#
# https://leetcode-cn.com/problems/deepest-leaves-sum/description/
#
# algorithms
# Medium (80.95%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    13.2K
# Total Submissions: 16.3K
# Testcase Example:  '[1,2,3,4,5,null,6,7,null,null,null,null,8]'
#
# 给你一棵二叉树，请你返回层数最深的叶子节点的和。
#
#
#
# 示例：
#
#
#
# 输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# 输出：15
#
#
#
#
# 提示：
#
#
# 树中节点数目在 1 到 10^4 之间。
# 每个节点的值在 1 到 100 之间。
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def bfs(root):
            if not root:
                return 0
            queue = deque([root])
            res = []
            while queue:
                size = len(queue)
                s = 0
                for _ in range(size):
                    node = queue.popleft()
                    s += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                res.append(s)
            return res[-1]
        return bfs(root)
# @lc code=end
