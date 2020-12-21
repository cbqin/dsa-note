#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# https://leetcode-cn.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (59.09%)
# Likes:    883
# Dislikes: 0
# Total Accepted:    98K
# Total Submissions: 165.9K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
#
#
#
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#
#
# 示例:
#
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49
#
#

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # n = len(height)
        # max_water = 0
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         water = (j-i)*min(height[i], height[j])
        #         max_water = max(max_water, water)
        # return max_water

        left = 0
        right = len(height)-1
        answer = 0
        while left < right:
            area = (right-left)*min(height[left], height[right])
            answer = max(answer, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return answer

# @lc code=end
