#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/
#
# algorithms
# Easy (74.01%)
# Likes:    129
# Dislikes: 0
# Total Accepted:    61.3K
# Total Submissions: 82.8K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的前序遍历。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 返回其前序遍历: [1,3,5,6,2,4]。
#
#
#
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    # def preorder(self, root: 'Node') -> List[int]:
    #     def dfs(root, res):
    #         if not root:
    #             return
    #         res.append(root.val)
    #         for child in root.children:
    #             dfs(child, res)
    #     res = []
    #     dfs(root, res)
    #     return res

    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children[::-1]:
                if child:
                    stack.append(child)
        return res
# @lc code=end
