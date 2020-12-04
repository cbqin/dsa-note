#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (38.98%)
# Likes:    551
# Dislikes: 0
# Total Accepted:    231.5K
# Total Submissions: 593.8K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
#
#
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
# 由于返回类型是整数，小数部分将被舍去。
#
#
#

# @lc code=start

# math


# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x == 0:
#             return 0
#         res = int(math.exp(0.5*math.log(x)))
#         return res+1 if (res+1)**2 <= x else res


# class Solution:
#     def mySqrt(self, x: int) -> int:
#         lo, hi = 0, x
#         ans = -1
#         while lo <= hi:
#             mi = (lo+hi) >> 1
#             if mi**2 <= x:
#                 ans = mi
#                 lo = mi+1
#             else:
#                 hi = mi-1
#         return ans


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        c, x0 = float(x), float(x)
        while True:
            xi = 0.5*(x0+c/x0)
            if abs(xi-x0) < 1e-7:
                break
            x0 = xi
        return int(x0)
# @lc code=end
