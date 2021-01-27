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


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(root, path, path_sum, res, sum):
            if not root:
                return

            path.append(root.val)
            path_sum += root.val
            if not root.left and not root.right:
                if path_sum == sum:
                    res.append(path[:])
            dfs(root.left, path, path_sum, res, sum)
            dfs(root.right, path, path_sum, res, sum)
            path.pop()
            path_sum -= root.val

        res = []
        dfs(root, [], 0, res, sum)
        return res


# @lc code=end
