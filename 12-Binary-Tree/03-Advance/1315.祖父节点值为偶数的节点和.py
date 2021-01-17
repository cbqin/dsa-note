#
# @lc app=leetcode.cn id=1315 lang=python3
#
# [1315] 祖父节点值为偶数的节点和
#
# https://leetcode-cn.com/problems/sum-of-nodes-with-even-valued-grandparent/description/
#
# algorithms
# Medium (80.93%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    9.3K
# Total Submissions: 11.5K
# Testcase Example:  '[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]'
#
# 给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：
#
#
# 该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）
#
#
# 如果不存在祖父节点值为偶数的节点，那么返回 0 。
#
#
#
# 示例：
#
#
#
# 输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# 输出：18
# 解释：图中红色节点的祖父节点的值为偶数，蓝色节点为这些红色节点的祖父节点。
#
#
#
#
# 提示：
#
#
# 树中节点的数目在 1 到 10^4 之间。
# 每个节点的值在 1 到 100 之间。
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def bfs(root):
            if not root:
                return 0
            queue = deque([(root, None, None)])
            res = 0
            while queue:
                size = len(queue)
                for _ in range(size):
                    node, parent, grandparent = queue.popleft()
                    if grandparent and grandparent.val % 2 == 0:
                        res += node.val
                    if node.left:
                        queue.append((node.left, node, parent))
                    if node.right:
                        queue.append((node.right, node, parent))
            return res

        return bfs(root)

# @lc code=end
