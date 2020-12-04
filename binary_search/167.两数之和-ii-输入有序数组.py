#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
# https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (56.94%)
# Likes:    439
# Dislikes: 0
# Total Accepted:    173K
# Total Submissions: 303.7K
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
#
# 说明:
#
#
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
#
#
# 示例:
#
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
#
#

# @lc code=start


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        two pointers: log(n)
        """
        # lo, hi = 0, len(numbers)-1
        # while lo < hi:
        #     s = numbers[lo]+numbers[hi]
        #     if s == target:
        #         return [lo+1, hi+1]
        #     elif s < target:
        #         lo += 1
        #     else:
        #         hi -= 1
        # return [-1, -1]

        """
        binary search: nlog(n)
        """
        hi = len(numbers)-1
        for i, number in enumerate(numbers):
            lo = i+1
            while lo <= hi:
                mi = (lo+hi) >> 1
                if target-number == numbers[mi]:
                    return [i+1, mi+1]
                elif target-number < numbers[mi]:
                    hi = mi-1
                else:
                    lo = mi+1
        return [-1, -1]

# @lc code=end
