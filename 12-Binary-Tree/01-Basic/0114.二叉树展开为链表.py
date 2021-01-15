#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (71.55%)
# Likes:    684
# Dislikes: 0
# Total Accepted:    104.1K
# Total Submissions: 145.3K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# 给定一个二叉树，原地将它展开为一个单链表。
#
#
#
# 例如，给定二叉树
#
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
#
# 将其展开为：
#
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
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
    # def flatten(self, root: TreeNode) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     if not root:
    #         return
    #     stack = [root]
    #     prev = None
    #     while stack:
    #         node = stack.pop()
    #         if node.right:
    #             stack.append(node.right)
    #         if node.left:
    #             stack.append(node.left)
    #         if prev:
    #             prev.right = node
    #             prev.left = None
    #         prev = node
    #     return root

    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        curr = root
        prev = None
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            else:
                curr = curr.right
        return root

# @lc code=end
