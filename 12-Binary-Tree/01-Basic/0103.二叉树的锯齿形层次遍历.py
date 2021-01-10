#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (55.22%)
# Likes:    365
# Dislikes: 0
# Total Accepted:    109K
# Total Submissions: 191.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回锯齿形层序遍历如下：
#
#
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
#
#
#

# @lc code=start

from typing import List
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = deque([root])
        while q:
            size = len(q)
            temp = []
            for _ in range(size):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            temp = temp if len(ans) % 2 == 0 else temp[::-1]
            ans.append(temp)
        return ans
# @lc code=end
