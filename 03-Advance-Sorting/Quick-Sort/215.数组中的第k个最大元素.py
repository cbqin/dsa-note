#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (64.53%)
# Likes:    827
# Dislikes: 0
# Total Accepted:    234.4K
# Total Submissions: 363.3K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#
#
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
#
# 说明:
#
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
#
#

# @lc code=start


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, left, right):
            random_index = random.randint(left, right)
            nums[left], nums[random_index] = nums[random_index], nums[left]
            pivot = nums[left]
            le = left+1
            ge = right
            while True:
                while le <= ge and nums[le] < pivot:
                    le += 1
                while le <= ge and nums[ge] > pivot:
                    ge -= 1
                if le > ge:
                    break
                nums[le], nums[ge] = nums[ge], nums[le]
                le += 1
                ge -= 1
            nums[left], nums[ge] = nums[ge], nums[left]

            return ge

        n = len(nums)
        left = 0
        right = n-1

        target = n-k
        while True:
            p = partition(nums, left, right)
            if p == target:
                return nums[p]
            elif p < target:
                left = p+1
            else:
                right = p-1

# @lc code=end
