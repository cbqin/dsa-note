#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (68.60%)
# Likes:    822
# Dislikes: 0
# Total Accepted:    143K
# Total Submissions: 207.8K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
#
# 返回如下的二叉树：
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#

# @lc code=start
from typing import List
# Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(preorder, preleft, preright, inorder, inleft, inright) -> TreeNode:
            if preleft > preright or inleft > inright:
                return None
            root_value = preorder[preleft]
            root = TreeNode(root_value)
            # index = inorder.index(root_value)
            index = indexs[root_value]
            root.left = build(preorder, preleft+1, index -
                              inleft+preleft, inorder, inleft, index-1)
            root.right = build(preorder, index-inleft+preleft+1,
                               preright, inorder, index+1, inright)
            return root

        length = len(preorder)
        indexs = {}
        for i, num in enumerate(inorder):
            indexs[num] = i
        return build(preorder, 0, length-1, inorder, 0, length-1)

# @lc code=end
