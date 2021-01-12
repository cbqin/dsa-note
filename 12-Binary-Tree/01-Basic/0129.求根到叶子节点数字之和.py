#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#
# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (66.30%)
# Likes:    301
# Dislikes: 0
# Total Accepted:    79.6K
# Total Submissions: 119.8K
# Testcase Example:  '[1,2,3]'
#
# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
#
# 例如，从根到叶子节点路径 1->2->3 代表数字 123。
#
# 计算从根到叶子节点生成的所有数字之和。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例 1:
#
# 输入: [1,2,3]
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25.
#
# 示例 2:
#
# 输入: [4,9,0,5,1]
# ⁠   4
# ⁠  / \
# ⁠ 9   0
# / \
# 5   1
# 输出: 1026
# 解释:
# 从根到叶子节点路径 4->9->5 代表数字 495.
# 从根到叶子节点路径 4->9->1 代表数字 491.
# 从根到叶子节点路径 4->0 代表数字 40.
# 因此，数字总和 = 495 + 491 + 40 = 1026.
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
    # def sumNumbers(self, root: TreeNode) -> int:
    #     def dfs(root: TreeNode, parent: int) -> int:
    #         if not root:
    #             return 0
    #         num = parent*10+root.val
    #         if not root.left and not root.right:
    #             return num
    #         return dfs(root.left, num)+dfs(root.right, num)
    #     return dfs(root, 0)

    def sumNumbers(self, root: TreeNode) -> int:
        def bfs(root: TreeNode) -> int:
            if not root:
                return 0
            q_node = deque([root])
            q_value = deque([root.val])
            res = 0
            while q_node:
                node = q_node.popleft()
                value = q_value.popleft()
                if not node.left and not node.right:
                    res += value
                    continue
                if node.left:
                    q_node.append(node.left)
                    q_value.append(value*10+node.left.val)
                if node.right:
                    q_node.append(node.right)
                    q_value.append(value*10+node.right.val)

            return res

        return bfs(root)

# @lc code=end
