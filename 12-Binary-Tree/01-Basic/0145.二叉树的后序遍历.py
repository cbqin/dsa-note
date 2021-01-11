#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Medium (73.73%)
# Likes:    503
# Dislikes: 0
# Total Accepted:    177.6K
# Total Submissions: 240.5K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 后序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# 输出: [3,2,1]
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
#

# @lc code=start

from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     def dfs(root: TreeNode, res: List[int]) -> None:
    #         if not root:
    #             return
    #         dfs(root.left, res)
    #         dfs(root.right, res)
    #         res.append(root.val)

    #     res = []
    #     dfs(root, res)
    #     return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        pass

# @lc code=end
