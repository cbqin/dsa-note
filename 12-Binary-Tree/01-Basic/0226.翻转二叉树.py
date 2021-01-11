#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#
# https://leetcode-cn.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (77.66%)
# Likes:    728
# Dislikes: 0
# Total Accepted:    177.3K
# Total Submissions: 227.9K
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# 翻转一棵二叉树。
#
# 示例：
#
# 输入：
#
# ⁠    4
# ⁠  /   \
# ⁠ 2     7
# ⁠/ \   / \
# 1   3 6   9
#
# 输出：
#
# ⁠    4
# ⁠  /   \
# ⁠ 7     2
# ⁠/ \   / \
# 9   6 3   1
#
# 备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：
#
# 谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
#
#

# @lc code=start

from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if not root:
    #         return root
    #     left = self.invertTree(root.left)
    #     right = self.invertTree(root.right)
    #     root.left = right
    #     root.right = left
    #     return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

# @lc code=end
