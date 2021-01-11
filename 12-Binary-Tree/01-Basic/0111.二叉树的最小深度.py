#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (45.70%)
# Likes:    426
# Dislikes: 0
# Total Accepted:    171K
# Total Submissions: 370.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明：叶子节点是指没有子节点的节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
#
#
# 示例 2：
#
#
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
#
#
#
#
# 提示：
#
#
# 树中节点数的范围在 [0, 10^5] 内
# -1000
#
#
#

# @lc code=start

from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def minDepth(self, root: TreeNode) -> int:
    #     def dfs(root: TreeNode) -> int:
    #         if not root:
    #             return 0
    #         left_min = dfs(root.left)
    #         right_min = dfs(root.right)
    #         return left_min+right_min+1 if left_min == 0 or right_min == 0 else min(left_min, right_min)+1

    #     return dfs(root)

    def minDepth(self, root: TreeNode) -> int:
        def bfs(root: TreeNode) -> int:
            if not root:
                return 0

            queue = deque([(root, 1)])
            while queue:
                node, depth = queue.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append((node.left, depth+1))
                if node.right:
                    queue.append((node.right, depth+1))

        return bfs(root)

# @lc code=end
