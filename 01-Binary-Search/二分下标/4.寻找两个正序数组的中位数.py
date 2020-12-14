#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (39.21%)
# Likes:    3464
# Dislikes: 0
# Total Accepted:    297.6K
# Total Submissions: 758.9K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
#
# 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#
#
# 示例 2：
#
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#
#
# 示例 3：
#
# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
#
#
# 示例 4：
#
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
#
#
# 示例 5：
#
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
#
#
#
#
# 提示：
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#

# @lc code=start

# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        (nums1, nums2) = (nums1, nums2) if len(
            nums1) <= len(nums2) else (nums2, nums1)
        m = len(nums1)
        n = len(nums2)
        total_left = (m+n+1)//2
        left = 0
        right = m
        while left < right:
            i = left+(right-left)//2
            j = total_left-i
            if nums2[j-1] > nums1[i]:
                left = i+1
            else:
                right = i
        i = left
        j = total_left-i
        nums1LeftMax = float("-inf") if i == 0 else nums1[i-1]
        nums1RightMIn = float("inf") if i == m else nums1[i]
        nums2LeftMax = float("-inf") if j == 0 else nums2[j-1]
        nums2RightMIn = float("inf") if j == n else nums2[j]

        if (m+n) % 2 == 1:
            return max(nums1LeftMax, nums2LeftMax)
        else:
            return (max(nums1LeftMax, nums2LeftMax)+min(nums1RightMIn, nums2RightMIn))/2
# @lc code=end
