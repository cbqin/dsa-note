#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#
# https://leetcode-cn.com/problems/permutation-sequence/description/
#
# algorithms
# Hard (51.72%)
# Likes:    458
# Dislikes: 0
# Total Accepted:    71.1K
# Total Submissions: 137.2K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
#
#
# 给定 n 和 k，返回第 k 个排列。
#
#
#
# 示例 1：
#
#
# 输入：n = 3, k = 3
# 输出："213"
#
#
# 示例 2：
#
#
# 输入：n = 4, k = 9
# 输出："2314"
#
#
# 示例 3：
#
#
# 输入：n = 3, k = 1
# 输出："123"
#
#
#
#
# 提示：
#
#
# 1
# 1
#
#
#

# @lc code=start


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(n, k, index, path):
            if index == n:
                return
            cnt = factorial[n - 1 - index]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if cnt < k:
                    k -= cnt
                    continue
                path.append(i)
                used[i] = True
                dfs(n, k, index + 1, path)
                # 注意：这里要加 return，后面的数没有必要遍历去尝试了
                return

        if n == 0:
            return ""

        used = [False for _ in range(n + 1)]
        path = []
        factorial = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i

        dfs(n, k, 0, path)
        return ''.join([str(num) for num in path])

# @lc code=end
