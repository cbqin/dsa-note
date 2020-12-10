#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
# https://leetcode-cn.com/problems/binary-search/description/
#
# algorithms
# Easy (55.46%)
# Likes:    178
# Dislikes: 0
# Total Accepted:    81.5K
# Total Submissions: 146.7K
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的
# target，如果目标值存在返回下标，否则返回 -1。
#
#
# 示例 1:
#
# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
#
#
# 示例 2:
#
# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1
#
#
#
#
# 提示：
#
#
# 你可以假设 nums 中的所有元素是不重复的。
# n 将在 [1, 10000]之间。
# nums 的每个元素都将在 [-9999, 9999]之间。
#
#
#

# @lc code=start


class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     if not nums:
    #         return -1
    #     left = 0
    #     right = len(nums)-1
    #     while left < right:
    #         mid = left+(right-left)//2
    #         if nums[mid] < target:
    #             left = mid+1
    #         else:
    #             right = mid
    #     if nums[left] == target:
    #         return left
    #     return -1
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left+(right-left+1)//2
            if target < nums[mid]:
                right = mid-1
            else:
                left = mid
        if nums[left] == target:
            return left
        return -1
# @lc code=end
