#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#
# https://leetcode-cn.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (76.52%)
# Likes:    415
# Dislikes: 0
# Total Accepted:    74.8K
# Total Submissions: 97.6K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# 给出一个完全二叉树，求出该树的节点个数。
#
# 说明：
#
#
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第
# h 层，则该层包含 1~ 2^h 个节点。
#
# 示例:
#
# 输入:
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \  /
# 4  5 6
#
# 输出: 6
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
    # def countNodes(self, root: TreeNode) -> int:
    #     def dfs(root: TreeNode) -> int:
    #         if not root:
    #             return 0
    #         if not root.left and not root.right:
    #             return 1
    #         return dfs(root.left)+dfs(root.right)+1
    #     return dfs(root)

    # def countNodes(self, root: TreeNode) -> int:
    #     def bfs(root: TreeNode) -> int:
    #         if not root:
    #             return 0
    #         queue = deque([root])
    #         count = 0
    #         while queue:
    #             node = queue.popleft()
    #             count += 1
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #         return count

    #     return bfs(root)

    def countNodes(self, root: TreeNode) -> int:
        def check(mid, root, h):
            bits = 1 << (h-1)
            node = root
            while node and bits > 0:
                if bits & mid:
                    node = node.right
                else:
                    node = node.left
                bits = bits >> 1
            return node is not None

        if not root:
            return 0
        h = 0
        node = root
        while node.left:
            h += 1
            node = node.left
        left = 1 << h
        right = (1 << (h+1))-1
        while left < right:
            mid = left+(right-left+1)//2
            if check(mid, root, h):
                left = mid
            else:
                right = mid-1
        return left
# @lc code=end
