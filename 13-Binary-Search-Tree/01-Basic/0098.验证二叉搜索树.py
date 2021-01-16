#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (32.93%)
# Likes:    890
# Dislikes: 0
# Total Accepted:    210.6K
# Total Submissions: 633.5K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
#
# 示例 1:
#
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
#
#
# 示例 2:
#
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
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


class Solution:
    # def isValidBST(self, root: TreeNode) -> bool:
    #     def dfs(root, lower, upper):
    #         if not root:
    #             return True
    #         if lower < root.val < upper:
    #             return dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper)
    #         else:
    #             return False
    #     return dfs(root, float("-inf"), float("inf"))

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        prev = float("-inf")

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True

# @lc code=end
