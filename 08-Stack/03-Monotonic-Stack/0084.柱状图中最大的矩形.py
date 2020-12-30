#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (42.01%)
# Likes:    1112
# Dislikes: 0
# Total Accepted:    111.5K
# Total Submissions: 263.1K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
#
#
# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
#
#
#
#
#
# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
#
#
#
# 示例:
#
# 输入: [2,1,5,6,2,3]
# 输出: 10
#
#

# @lc code=start


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        heights = [0]+heights+[0]
        n += 2
        area = 0
        stack = [0]
        for i in range(1, n):
            while heights[stack[-1]] > heights[i]:
                pop = stack.pop()
                height = heights[pop]
                width = i-stack[-1]-1
                area = max(area, height*width)
            stack.append(i)
        return area
# @lc code=end
