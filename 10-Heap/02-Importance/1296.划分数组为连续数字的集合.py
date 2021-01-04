#
# @lc app=leetcode.cn id=1296 lang=python3
#
# [1296] 划分数组为连续数字的集合
#
# https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers/description/
#
# algorithms
# Medium (44.11%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    5.8K
# Total Submissions: 13.2K
# Testcase Example:  '[1,2,3,3,4,4,5,6]\n4'
#
# 给你一个整数数组 nums 和一个正整数 k，请你判断是否可以把这个数组划分成一些由 k 个连续数字组成的集合。
# 如果可以，请返回 True；否则，返回 False。
#
#
#
# 注意：此题目与 846 重复：https://leetcode-cn.com/problems/hand-of-straights/
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3,3,4,4,5,6], k = 4
# 输出：true
# 解释：数组可以分成 [1,2,3,4] 和 [3,4,5,6]。
#
#
# 示例 2：
#
#
# 输入：nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# 输出：true
# 解释：数组可以分成 [1,2,3] , [2,3,4] , [3,4,5] 和 [9,10,11]。
#
#
# 示例 3：
#
#
# 输入：nums = [3,3,2,2,1,1], k = 3
# 输出：true
#
#
# 示例 4：
#
#
# 输入：nums = [1,2,3,4], k = 3
# 输出：false
# 解释：数组不能分成几个大小为 3 的子数组。
#
#
#
#
# 提示：
#
#
# 1
# 1
# 1
#
#
#

# @lc code=start
from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        s = Counter(nums)
        order_nums = sorted(s)
        for num in order_nums:
            occ = s[num]
            if occ > 0:
                for i in range(num+1, num+k):
                    if s[i] >= occ:
                        s[i] -= occ
                    else:
                        return False
        return True
# @lc code=end
