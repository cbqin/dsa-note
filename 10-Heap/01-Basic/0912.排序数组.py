#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
# https://leetcode-cn.com/problems/sort-an-array/description/
#
# algorithms
# Medium (59.58%)
# Likes:    190
# Dislikes: 0
# Total Accepted:    99.3K
# Total Submissions: 166.6K
# Testcase Example:  '[5,2,3,1]'
#
# 给你一个整数数组 nums，请你将该数组升序排列。
#
#
#
#
#
#
# 示例 1：
#
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
#
#
# 示例 2：
#
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000
#
#
#

# @lc code=start


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        h = []
        for num in nums:
            heapq.heappush(h, num)
        return [heappop(h) for _ in range(len(h))]
# @lc code=end
