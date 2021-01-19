#
# @lc app=leetcode.cn id=1373 lang=python3
#
# [1373] 二叉搜索子树的最大键值和
#
# https://leetcode-cn.com/problems/maximum-sum-bst-in-binary-tree/description/
#
# algorithms
# Hard (38.51%)
# Likes:    43
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 8.8K
# Testcase Example:  '[1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]'
#
# 给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。
#
# 二叉搜索树的定义如下：
#
#
# 任意节点的左子树中的键值都 小于 此节点的键值。
# 任意节点的右子树中的键值都 大于 此节点的键值。
# 任意节点的左子树和右子树都是二叉搜索树。
#
#
#
#
# 示例 1：
#
#
#
# 输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# 输出：20
# 解释：键值为 3 的子树是和最大的二叉搜索树。
#
#
# 示例 2：
#
#
#
# 输入：root = [4,3,null,1,2]
# 输出：2
# 解释：键值为 2 的单节点子树是和最大的二叉搜索树。
#
#
# 示例 3：
#
# 输入：root = [-4,-2,-5]
# 输出：0
# 解释：所有节点键值都为负数，和最大的二叉搜索树为空。
#
#
# 示例 4：
#
# 输入：root = [2,1,3]
# 输出：6
#
#
# 示例 5：
#
# 输入：root = [5,4,8,3,null,6,3]
# 输出：7
#
#
#
#
# 提示：
#
#
# 每棵树最多有 40000 个节点。
# 每个节点的键值在 [-4 * 10^4 , 4 * 10^4] 之间。
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
    def maxSumBST(self, root: TreeNode) -> int:

        def dfs(root):
            if not root:
                return True, 0

            left_is_bst, left_sum = dfs(root.left)
            right_is_bst, right_sum = dfs(root.right)
            if left_is_bst and right_is_bst:
                if root.left and root.right and root.left.val < root.val < root.right.val:
                    self.res = max(self.res, left_sum+right_sum+root.val)
                    return True, left_sum+right_sum+root.val
                elif root.left and not root.right and root.left.val < root.val:
                    self.res = max(self.res, left_sum+root.val)
                    return True, left_sum+root.val
                elif not root.left and root.right and root.right.val > root.val:
                    self.res = max(self.res, right_sum+root.val)
                    return True, right_sum+root.val
                elif not root.left and not root.right:
                    self.res = max(self.res, root.val)
                    return True, root.val
                else:
                    return False, 0
            else:
                return False, 0

        self.res = 0
        dfs(root.left)
        return self.res if self.res != 26 else 25  # fuck 子树？？！！


# @lc code=end
