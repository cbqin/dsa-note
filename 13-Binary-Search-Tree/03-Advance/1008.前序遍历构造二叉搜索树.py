#
# @lc app=leetcode.cn id=1008 lang=python3
#
# [1008] 前序遍历构造二叉搜索树
#
# https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
#
# algorithms
# Medium (72.52%)
# Likes:    123
# Dislikes: 0
# Total Accepted:    10.7K
# Total Submissions: 14.8K
# Testcase Example:  '[8,5,1,7,10,12]'
#
# 返回与给定前序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。
#
# (回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于 node.left 的任何后代，值总 < node.val，而 node.right
# 的任何后代，值总 > node.val。此外，前序遍历首先显示节点 node 的值，然后遍历 node.left，接着遍历 node.right。）
#
# 题目保证，对于给定的测试用例，总能找到满足要求的二叉搜索树。
#
#
#
# 示例：
#
# 输入：[8,5,1,7,10,12]
# 输出：[8,5,10,1,7,null,12]
#
#
#
#
#
# 提示：
#
#
# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 10^8
# preorder 中的值互不相同
#
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
    # def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
    #     def dfs(preorder, left, right):
    #         if left > right:
    #             return None
    #         root = TreeNode(preorder[left])
    #         if left == right:
    #             return root
    #         mid = left
    #         while mid+1 <= right and preorder[mid+1] < preorder[left]:
    #             mid += 1

    #         root.left = dfs(preorder, left+1, mid)
    #         root.right = dfs(preorder, mid+1, right)
    #         return root

    #     return dfs(preorder, 0, len(preorder)-1)

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def dfs(preorder, bound):
            if self.i == len(preorder) or preorder[self.i] > bound:
                return None

            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = dfs(preorder, root.val)
            root.right = dfs(preorder, bound)
            return root

        self.i = 0
        return dfs(preorder, float("inf"))

# @lc code=end
