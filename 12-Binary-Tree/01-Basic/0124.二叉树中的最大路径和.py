#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (43.21%)
# Likes:    845
# Dislikes: 0
# Total Accepted:    91.8K
# Total Submissions: 212.3K
# Testcase Example:  '[1,2,3]'
#
# 给你一个二叉树的根节点 root ，返回其最大路径和。
#
# 本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径 至少包含一个 节点，且不一定经过根节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3]
# 输出：6
#
#
# 示例 2：
#
#
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
#
#
#
#
# 提示：
#
#
# 树中节点数目范围是 [1, 3 * 10^4]
# -1000
#
#
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_path_sum = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(root: TreeNode) -> int:
            if not root:
                return 0
            left = max(maxGain(root.left), 0)
            right = max(maxGain(root.right), 0)
            self.max_path_sum = max(left+right+root.val, self.max_path_sum)
            return root.val+max(left, right)
        maxGain(root)
        return self.max_path_sum
# @lc code=end
