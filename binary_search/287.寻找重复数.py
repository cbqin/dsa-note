#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
# https://leetcode-cn.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (66.06%)
# Likes:    987
# Dislikes: 0
# Total Accepted:    109.2K
# Total Submissions: 165.2K
# Testcase Example:  '[1,3,4,2,2]'
#
# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和
# n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
#
# 示例 1:
#
# 输入: [1,3,4,2,2]
# 输出: 2
#
#
# 示例 2:
#
# 输入: [3,1,3,4,2]
# 输出: 3
#
#
# 说明：
#
#
# 不能更改原数组（假设数组是只读的）。
# 只能使用额外的 O(1) 的空间。
# 时间复杂度小于 O(n^2) 。
# 数组中只有一个重复的数字，但它可能不止重复出现一次。
#
#
#

# @lc code=start


# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         # binary search: O(nlogn)
#         lo, hi = 1, len(nums)-1
#         while lo < hi:
#             mi = (lo+hi) >> 1

#             cnt = 0
#             for num in nums:
#                 if num <= mi:
#                     cnt += 1

#             if cnt > mi:
#                 hi = mi
#             else:
#                 lo = mi+1
#         return lo

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # two pointers, fast, slow: O(n)
        fast = 0
        slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]
            if slow == finder:
                break
        return slow

# @lc code=end
