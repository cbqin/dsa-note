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
        stack = list()
        res = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                bottom = height[stack.pop()]
                if not stack:
                    break
                heigh = min(height[stack[-1]], h)-bottom
                width = i-stack[-1]-1
                res += heigh*width
            stack.append(i)
        return res
# @lc code=end
