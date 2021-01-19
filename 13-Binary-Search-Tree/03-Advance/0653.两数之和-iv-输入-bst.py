#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#
# https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (57.22%)
# Likes:    212
# Dislikes: 0
# Total Accepted:    26.2K
# Total Submissions: 45.5K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
#
# 案例 1:
#
#
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Target = 9
#
# 输出: True
#
#
#
#
# 案例 2:
#
#
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Target = 28
#
# 输出: False
#
#
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
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def dfs(root, res):
            if not root:
                return
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)

        def twopointer(res, k):
            n = len(res)
            left = 0
            right = n-1
            while left < right:
                if res[left]+res[right] > k:
                    right -= 1
                elif res[left]+res[right] < k:
                    left += 1
                else:
                    return True
            return False

        res = []
        dfs(root, res)
        return twopointer(res, k)

# @lc code=end
