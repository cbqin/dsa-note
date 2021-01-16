#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#
# https://leetcode-cn.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (54.98%)
# Likes:    211
# Dislikes: 0
# Total Accepted:    16.4K
# Total Submissions: 29.6K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
#
# 两棵树重复是指它们具有相同的结构以及相同的结点值。
#
# 示例 1：
#
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
#
#
# 下面是两个重复的子树：
#
# ⁠     2
# ⁠    /
# ⁠   4
#
#
# 和
#
# ⁠   4
#
#
# 因此，你需要以列表的形式返回上述重复子树的根结点。
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import Counter


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        count = Counter()
        ans = []

        def dfs(root):
            if not root:
                return "#"
            serial = "{},{},{}".format(
                root.val, dfs(root.left), dfs(root.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(root)
            return serial

        dfs(root)
        return ans
# @lc code=end
