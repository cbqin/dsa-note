#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# https://leetcode-cn.com/problems/path-sum/description/
#
# algorithms
# Easy (51.50%)
# Likes:    494
# Dislikes: 0
# Total Accepted:    164.3K
# Total Submissions: 318.4K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，
#
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \      \
# ⁠       7    2      1
#
#
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
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
    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # def dfs(root: TreeNode, sum: int) -> bool:
        #     if not root:
        #         return False
        #     if not root.left and not root.right:
        #         return root.val == sum

        #     left = self.hasPathSum(root.left, sum-root.val)
        #     right = self.hasPathSum(root.right, sum-root.val)
        #     return left or right

        # return dfs(root, sum)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def bfs(root: TreeNode, sum: int) -> bool:
            if not root:
                return False
            q_node = deque([root])
            q_sum = deque([root.val])
            while q_node:
                node = q_node.popleft()
                value = q_sum.popleft()
                if not node.left and not node.right:
                    if value == sum:
                        return True
                    continue
                if node.left:
                    q_node.append(node.left)
                    q_sum.append(value+node.left.val)
                if node.right:
                    q_node.append(node.right)
                    q_sum.append(value+node.right.val)
            return False
        return bfs(root, sum)

# @lc code=end
