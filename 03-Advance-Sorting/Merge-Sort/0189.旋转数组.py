#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
# https://leetcode-cn.com/problems/rotate-array/description/
#
# algorithms
# Medium (43.72%)
# Likes:    750
# Dislikes: 0
# Total Accepted:    184.1K
# Total Submissions: 421.1K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
#
# 示例 2:
#
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#
# 说明:
#
#
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。
#
#
#

# @lc code=start


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.rotate4(nums, k)

    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for _ in range(k):
            temp = nums[-1]
            for j in range(n-1, 1, -1):
                nums[j] = nums[j-1]
            nums[0] = temp

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp = [0]*n
        for i in range(n):
            temp[(i+k) % n] = nums[i]
        nums[:] = temp[:]

    def rotate3(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        n = len(nums)
        k %= n
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)

    def rotate4(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        count = 0
        start = 0
        while count < n:
            current = start
            prev = nums[start]
            while True:
                next_ = (current+k) % n
                temp = nums[next_]
                nums[next_] = prev
                prev = temp
                count += 1
                current = next_
                if current == start:
                    break
            start += 1

# @lc code=end
