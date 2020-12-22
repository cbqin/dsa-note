#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.83%)
# Likes:    645
# Dislikes: 0
# Total Accepted:    174.3K
# Total Submissions: 380.1K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
#
#
# 示例：
#
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#
#
#
#
# 提示：
#
#
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
#
#
#

# @lc code=start


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = []
        if n < 3:
            return res

        nums.sort()
        min_diff = float("inf")

        for i in range(n-2):
            t = target-nums[i]
            left = i+1
            right = n-1
            while left < right:
                two_sum = nums[left]+nums[right]
                if two_sum > t:
                    diff = two_sum-t
                    if diff < min_diff:
                        min_diff = diff
                        res.append(nums[i]+two_sum)
                    right -= 1

                elif nums[left]+nums[right] < t:
                    diff = t-two_sum
                    if diff < min_diff:
                        min_diff = diff
                        res.append(nums[i]+two_sum)
                    left += 1
                else:
                    return target
        return res[-1]

# @lc code=end
