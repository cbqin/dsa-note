#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
# https://leetcode-cn.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (39.43%)
# Likes:    119
# Dislikes: 0
# Total Accepted:    22.4K
# Total Submissions: 56.7K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
#
# 示例 1:
#
# 输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
#
#
#
#
# 注意:
#
#
# 1 <= k <= n <= 30,000。
# 所给数据范围 [-10,000，10,000]。
#
#
#

# @lc code=start


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        left = 0
        right = k-1
        temp_sum = sum(nums[left:k])
        max_average = temp_sum/k

        while right+1 < n:
            right += 1
            temp_sum += nums[right]
            temp_sum -= nums[left]
            left += 1

            max_average = max(max_average, temp_sum/k)

        return max_average

# @lc code=end
