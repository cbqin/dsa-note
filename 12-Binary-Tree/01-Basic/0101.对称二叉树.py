#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (53.26%)
# Likes:    1192
# Dislikes: 0
# Total Accepted:    250.7K
# Total Submissions: 469.8K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
#
#
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
#
#
#
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
#
#
# 进阶：
#
# 你可以运用递归和迭代两种方法解决这个问题吗？
#
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     def dfs(p: TreeNode, q: TreeNode) -> bool:
    #         if not p and not q:
    #             return True
    #         elif not p or not q:
    #             return False
    #         elif p.val != q.val:
    #             return False
    #         else:
    #             return dfs(p.left, q.right) and dfs(p.right, q.left)

    #     if not root:
    #         return True
    #     return dfs(root.left, root.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        pass


# @lc code=end
