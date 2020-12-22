#
# @lc app=leetcode.cn id=978 lang=python3
#
# [978] 最长湍流子数组
#
# https://leetcode-cn.com/problems/longest-turbulent-subarray/description/
#
# algorithms
# Medium (42.30%)
# Likes:    69
# Dislikes: 0
# Total Accepted:    12.1K
# Total Submissions: 28.5K
# Testcase Example:  '[9,4,2,10,7,8,8,1,9]'
#
# 当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：
#
#
# 若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
# 或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
#
#
# 也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。
#
# 返回 A 的最大湍流子数组的长度。
#
#
#
# 示例 1：
#
# 输入：[9,4,2,10,7,8,8,1,9]
# 输出：5
# 解释：(A[1] > A[2] < A[3] > A[4] < A[5])
#
#
# 示例 2：
#
# 输入：[4,8,12,16]
# 输出：2
#
#
# 示例 3：
#
# 输入：[100]
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 40000
# 0 <= A[i] <= 10^9
#
#
#

# @lc code=start


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return n

        left = 0
        right = 1
        res = 1
        is_left = False

        while right < n:
            if arr[right] == arr[right-1]:
                left = right
                right += 1
            elif right-left == 1 or ((arr[right]-arr[right-1] < 0) != is_left):
                is_left = (arr[right]-arr[right-1] < 0)
                res = max(res, right-left+1)
                right += 1
            else:
                left = right-1

        return res

# @lc code=end
