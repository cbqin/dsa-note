#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (76.06%)
# Likes:    470
# Dislikes: 0
# Total Accepted:    127.5K
# Total Submissions: 167.2K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
#

# @lc code=start


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(n, k, begin, path, res):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(begin, n+1):
                path.append(i)
                dfs(n, k, i+1, path, res)
                path.pop()
        res = []
        dfs(n, k, 1, [], res)
        return res
# @lc code=end
