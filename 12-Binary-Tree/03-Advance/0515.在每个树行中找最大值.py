#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#
# https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (62.87%)
# Likes:    119
# Dislikes: 0
# Total Accepted:    23.4K
# Total Submissions: 36.9K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# 您需要在二叉树的每一行中找到最大的值。
#
# 示例：
#
#
# 输入:
#
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \
# ⁠     5   3   9
#
# 输出: [1, 3, 9]
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        def bfs(root):
            if not root:
                return
            queue = deque([root])
            res = []
            while queue:
                size = len(queue)
                maxval = float("-inf")
                for _ in range(size):
                    node = queue.popleft()
                    if node.val > maxval:
                        maxval = node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                res.append(maxval)
            return res
        return bfs(root)

# @lc code=end
