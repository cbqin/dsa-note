#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode-cn.com/problems/powx-n/description/
#
# algorithms
# Medium (36.98%)
# Likes:    552
# Dislikes: 0
# Total Accepted:    142.4K
# Total Submissions: 384.9K
# Testcase Example:  '2.00000\n10'
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
#
# 示例 1:
#
# 输入: 2.00000, 10
# 输出: 1024.00000
#
#
# 示例 2:
#
# 输入: 2.10000, 3
# 输出: 9.26100
#
#
# 示例 3:
#
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2^-2 = 1/2^2 = 1/4 = 0.25
#
# 说明:
#
#
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
#
#
#

# @lc code=start


# 递归
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         def quickMul(n):
#             if n == 0:
#                 return 1.0
#             y = quickMul(n//2)
#             return y*y if n % 2 == 0 else x*y*y
#         return quickMul(n) if n >= 0 else 1.0/quickMul(-n)

# 迭代
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(n):
            res = 1.0
            weight = x

            while n:
                if n & 1:
                    res *= weight
                weight *= weight
                n >>= 1
            return res
        return quickMul(n) if n >= 0 else 1/quickMul(-n)

# @lc code=end
