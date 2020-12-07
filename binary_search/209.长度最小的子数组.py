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
    # def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    #     # two pointers: O(n)
    #     if not nums:
    #         return 0
    #     back, front = 0, 0
    #     total, min_seq_len = 0, len(nums)+1
    #     while front < len(nums):
    #         total += nums[front]
    #         while total >= s:
    #             min_seq_len = min(min_seq_len, front-back+1)
    #             total -= nums[back]
    #             back += 1
    #         front += 1
    #     return 0 if min_seq_len == len(nums)+1 else min_seq_len

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # binary search: O(nlogn)
        def binary_search(arr, e, lo, hi):
            while lo < hi:
                mi = (lo+hi) >> 1
                if e < arr[mi]:
                    hi = mi
                else:
                    lo = mi+1
            return lo-1

        if not nums:
            return 0
        n = len(nums)
        ans = n+1
        sums = [0]
        for i in range(n):
            sums.append(sums[-1]+nums[i])

        for i in range(1, n+1):
            target = s+sums[i-1]
            # bound = bisect.bisect_left(sums, target)
            bound = binary_search(sums, target-1, 0, len(sums))+1
            if bound != len(sums):  # why
                ans = min(ans, bound-i+1)
        return ans if ans != n+1 else 0

# @lc code=end
