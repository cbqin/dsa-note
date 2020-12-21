#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (39.72%)
# Likes:    1083
# Dislikes: 0
# Total Accepted:    196K
# Total Submissions: 493.4K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 给你一个整数数组 nums ，和一个整数 target 。
#
# 该整数数组原本是按升序排列，但输入时在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2]
# ）。
#
# 请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
#
# 示例 1：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#
#
# 示例 2：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
#
# 示例 3：
#
#
# 输入：nums = [1], target = 0
# 输出：-1
#
#
#
#
# 提示：
#
#
# 1
# -10^4
# nums 中的每个值都 独一无二
# nums 肯定会在某个点上旋转
# -10^4
#
#
#

# @lc code=start


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left+(right-left+1)//2
            if nums[mid] > nums[left]:
                if nums[left] <= target <= nums[mid-1]:
                    right = mid-1
                else:
                    left = mid
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid-1
        if nums[left] == target:
            return left
        return -1

# @lc code=end
