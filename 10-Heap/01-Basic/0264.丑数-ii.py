#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (54.65%)
# Likes:    448
# Dislikes: 0
# Total Accepted:    41.5K
# Total Submissions: 75.6K
# Testcase Example:  '10'
#
# 编写一个程序，找出第 n 个丑数。
#
# 丑数就是质因数只包含 2, 3, 5 的正整数。
#
# 示例:
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
#
# 说明:  
#
#
# 1 是丑数。
# n 不超过1690。
#
#
#

# @lc code=start
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = [1]
        res = 1
        for _ in range(n):
            res = heapq.heappop(h)

            while len(h) and h[0] == res:
                heapq.heappop(h)

            heapq.heappush(h, 2*res)
            heapq.heappush(h, 3*res)
            heapq.heappush(h, 5*res)

        return res
# @lc code=end
