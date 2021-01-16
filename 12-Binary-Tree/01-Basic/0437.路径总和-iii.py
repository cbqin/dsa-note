#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# https://leetcode-cn.com/problems/path-sum-iii/description/
#
# algorithms
# Medium (56.41%)
# Likes:    711
# Dislikes: 0
# Total Accepted:    62.8K
# Total Submissions: 111K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# 给定一个二叉树，它的每个结点都存放着一个整数值。
#
# 找出路径和等于给定数值的路径总数。
#
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
#
# 示例：
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
#
# 返回 3。和等于 8 的路径有:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
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

from collections import deque, defaultdict


class Solution:
    def __init__(self):
        self.res = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:

        def bfs(root, sum, curr_sum, prefix_sum):
            if not root:
                return
            curr_sum += root.val
            self.res += prefix_sum[curr_sum-sum]
            prefix_sum[curr_sum] += 1
            bfs(root.left, sum, curr_sum, prefix_sum)
            bfs(root.right, sum, curr_sum, prefix_sum)
            prefix_sum[curr_sum] -= 1

        prefix_sum = defaultdict(int)
        # prefix_sum[0] = 1
        bfs(root, sum, 0, prefix_sum)
        return self.res

# @lc code=end
