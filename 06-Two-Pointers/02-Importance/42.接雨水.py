#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (53.47%)
# Likes:    1885
# Dislikes: 0
# Total Accepted:    176.6K
# Total Submissions: 329.4K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 示例 1：
#
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
#
# 示例 2：
#
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
#
#
# 提示：
#
#
# n == height.length
# 0
# 0
#
#
#

# @lc code=start


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        res = 0
        left_max = height[0]
        right_max = height[-1]
        left = 1
        right = n-2

        while left <= right:
            if left_max <= right_max:
                if height[left] < left_max:
                    res += left_max-height[left]
                left_max = max(left_max, height[left])
                left += 1
            else:
                if height[right] < right_max:
                    res += right_max-height[right]
                right_max = max(right_max, height[right])
                right -= 1
        return res
# @lc code=end
