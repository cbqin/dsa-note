#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (70.83%)
# Likes:    435
# Dislikes: 0
# Total Accepted:    84.3K
# Total Submissions: 118.9K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
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
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(inorder, inleft, inright, postorder, postleft, postright):
            if inleft > inright or postleft > postright:
                return None
            root_val = postorder[postright]
            root = TreeNode(root_val)
            # index = inorder.index(root_val)
            index = indexs[root_val]
            root.left = build(inorder, inleft, index-1,
                              postorder, postleft, index-inleft+postleft-1)
            root.right = build(inorder, index+1, inright,
                               postorder, index-inleft+postleft, postright-1)
            return root
        indexs = {}
        for i, num in enumerate(inorder):
            indexs[num] = i
        length = len(inorder)
        return build(inorder, 0, length-1, postorder, 0, length-1)

# @lc code=end
