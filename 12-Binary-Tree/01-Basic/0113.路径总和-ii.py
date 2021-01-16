#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (61.25%)
# Likes:    408
# Dislikes: 0
# Total Accepted:    110.8K
# Total Submissions: 180.4K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
#
#
# 返回:
#
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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
    # def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    #     def dfs(root, path, sum):
    #         if not root:
    #             return
    #         path.append(root.val)
    #         if not root.left and not root.right:
    #             if root.val == sum:
    #                 ans.append(path[:])
    #         dfs(root.left, path, sum-root.val)
    #         dfs(root.right, path, sum-root.val)
    #         path.pop()
    #     ans = []
    #     path = []
    #     dfs(root, path, sum)
    #     return ans

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def bfs(root, sum):
            if not root:
                return []
            ans = []
            queue = deque([(root, [], 0)])
            while queue:
                node, path, val = queue.popleft()
                if not node.left and not node.right:
                    if node.val+val == sum:
                        ans.append(path+[node.val])
                if node.left:
                    queue.append((node.left, path+[node.val], node.val+val))
                if node.right:
                    queue.append((node.right, path+[node.val], node.val+val))
            return ans
        return bfs(root, sum)
# @lc code=end
