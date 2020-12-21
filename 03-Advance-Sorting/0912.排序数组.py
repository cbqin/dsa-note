#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
# https://leetcode-cn.com/problems/sort-an-array/description/
#
# algorithms
# Medium (59.58%)
# Likes:    190
# Dislikes: 0
# Total Accepted:    99.3K
# Total Submissions: 166.6K
# Testcase Example:  '[5,2,3,1]'
#
# 给你一个整数数组 nums，请你将该数组升序排列。
#
#
#
#
#
#
# 示例 1：
#
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
#
#
# 示例 2：
#
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000
#
#
#

# @lc code=start


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # return self.selectionSort(nums)
        # return self.bubbleSort(nums)
        # return self.insertionSort(nums)
        # return self.shellSort(nums)
        return self.quickSort(nums)

    def selectionSort(self, nums: List[int]) -> List[int]:
        """
        每一轮都选取「未排定的部分」的最小元素，然后将它 交换 到「未排定的部分」的第 1 个位置
        交换的次数最少:N-1
        运行时间与输入无关
        优化是堆排序
        """
        n = len(nums)
        for i in range(0, n-1):
            current_min = i
            for j in range(i, n):
                if nums[j] < nums[current_min]:
                    current_min = j
            nums[i], nums[current_min] = nums[current_min], nums[i]
        return nums

    def bubbleSort(self, nums: List[int]) -> List[int]:
        """
        每一轮都一次比较两个元素，如果他们的顺序错误就把他们交换过来
        交换次数：N^2
        """
        n = len(nums)
        for i in range(n):
            is_sorted = True
            for j in range(n-1-i):
                if nums[j] > nums[j+1]:  # 稳定
                    is_sorted = False
                    nums[j], nums[j+1] = nums[j+1], nums[j]
            if is_sorted:
                break
        return nums

    def insertionSort(self, nums: List[int]) -> List[int]:
        """
        将一个元素插入之前的有序数组中，使之成为更长的有序数组
        """
        # n = len(nums)
        # for i in range(1, n):
        #     for j in range(i, 0, -1):
        #         if nums[j-1] > nums[j]:
        #             nums[j-1], nums[j] = nums[j], nums[j-1]
        #         else:
        #             break
        # return nums

        # n = len(nums)
        # for i in range(1, n):
        #     temp = nums[i]
        #     j = i
        #     while j > 0 and nums[j-1] > temp:
        #         nums[j] = nums[j-1]
        #         j -= 1
        #     nums[j] = temp
        # return nums

        # 哨兵：将最小元素提前放到第一个位置
        # n = len(nums)
        # min_index = 0
        # for i in range(1, n):
        #     if nums[i] < nums[min_index]:
        #         min_index = i
        # nums[0], nums[min_index] = nums[min_index], nums[0]

        # for i in range(1, n):
        #     temp = nums[i]
        #     j = i
        #     while nums[j-1] > temp:
        #         nums[j] = nums[j-1]
        #         j -= 1
        #     nums[j] = temp
        # return nums

        # 折半插入排序
        n = len(nums)
        for i in range(1, n):
            temp = nums[i]
            j = i
            left = 0
            right = i
            while left < right:
                mid = left+(right-left)//2
                if nums[mid] > nums[i]:
                    right = mid
                else:
                    left = mid+1
            while j > left:
                nums[j] = nums[j-1]
                j -= 1
            nums[j] = temp
        return nums

    def shellSort(self, nums: List[int]) -> List[int]:
        """
        依间隔序列依次进行插入排序
        利用插入排序在接近有序情况下效率较高的优点
        目前Sedgewick增量序列目前最好
        """
        n = len(nums)
        gap = n//2
        while gap > 0:
            for i in range(gap, n):
                temp = nums[i]
                j = i
                while j-gap >= 0 and nums[j-gap] > temp:
                    nums[j] = nums[j-gap]
                    j -= gap
                nums[j] = temp
            gap //= 2
        return nums

    def quickSort(self, nums):
        def partition(nums, left, right):
            random_index = random.randint(left, right)
            nums[left], nums[random_index] = nums[random_index], nums[left]
            pivot = nums[left]
            lt = left
            gt = right+1
            i = left+1
            while i < gt:
                if nums[i] < pivot:
                    lt += 1
                    nums[i], nums[lt] = nums[lt], nums[i]
                    i += 1
                elif nums[i] == pivot:
                    i += 1
                else:
                    gt -= 1
                    nums[i], nums[gt] = nums[gt], nums[i]
            nums[left], nums[lt] = nums[lt], nums[left]

            return lt, gt

        def quickSortCore(nums, left, right):
            if left >= right:
                return
            lt, gt = partition(nums, left, right)
            quickSortCore(nums, left, lt-1)
            quickSortCore(nums, gt, right)

        n = len(nums)
        if n == 0:
            return
        quickSortCore(nums, 0, n-1)
        return nums


# @lc code=end
