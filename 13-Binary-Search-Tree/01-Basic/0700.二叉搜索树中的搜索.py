#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#
# https://leetcode-cn.com/problems/search-in-a-binary-search-tree/description/
#
# algorithms
# Easy (74.85%)
# Likes:    106
# Dislikes: 0
# Total Accepted:    46K
# Total Submissions: 61.3K
# Testcase Example:  '[4,2,7,1,3]\n2'
#
# 给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
#
# 例如，
#
#
# 给定二叉搜索树:
#
# ⁠       4
# ⁠      / \
# ⁠     2   7
# ⁠    / \
# ⁠   1   3
#
# 和值: 2
#
#
# 你应该返回如下子树:
#
#
# ⁠     2
# ⁠    / \
# ⁠   1   3
#
#
# 在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    #     def dfs(root, val):
    #         if root is None:
    #             return None
    #         if val < root.val:
    #             return dfs(root.left, val)
    #         elif val > root.val:
    #             return dfs(root.right, val)
    #         else:
    #             return root
    #     return dfs(root, val)

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return root

# @lc code=end
