#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (44.60%)
# Likes:    507
# Dislikes: 0
# Total Accepted:    101.2K
# Total Submissions: 226.8K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续
# 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
#
#
#
# 示例：
#
# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
#
#
#
#
# 进阶：
#
#
# 如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
#
#
#

# @lc code=start


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        start = 0
        min_len = n+1
        temp_sum = 0

        while right < n:
            temp_sum += nums[right]
            right += 1

            while temp_sum >= s:
                if right-left < min_len:
                    start = left
                    min_len = right-left
                temp_sum -= nums[left]
                left += 1
        return 0 if min_len == n+1 else min_len


# @lc code=end
