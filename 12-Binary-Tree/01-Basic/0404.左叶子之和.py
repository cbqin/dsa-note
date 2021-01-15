#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
# https://leetcode-cn.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (56.31%)
# Likes:    272
# Dislikes: 0
# Total Accepted:    66.6K
# Total Submissions: 118.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 计算给定二叉树的所有左叶子之和。
#
# 示例：
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
#
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


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(root, left):
            if not root:
                return
            if not root.left and not root.right:
                if left:
                    nonlocal s
                    s += root.val
            else:
                if root.left:
                    dfs(root.left, True)
                if root.right:
                    dfs(root.right, False)
        s = 0
        if root:
            dfs(root.left, True)
            dfs(root.right, False)
        return s
# @lc code=end
