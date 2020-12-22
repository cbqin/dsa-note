#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (58.59%)
# Likes:    1345
# Dislikes: 0
# Total Accepted:    520.7K
# Total Submissions: 888.4K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
#
#
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
#
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
#
#
# 进阶:
#
# 你能不将整数转为字符串来解决这个问题吗？
#
#

# @lc code=start


class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     s = str(x)
    #     n = len(s)
    #     left = 0
    #     right = n-1
    #     while left < right:
    #         if s[left] == s[right]:
    #             left += 1
    #             right -= 1
    #         else:
    #             return False
    #     return True

    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        origin = x
        while x > 0:
            reverse = reverse*10+x % 10
            x //= 10
        return origin == reverse

# @lc code=end
