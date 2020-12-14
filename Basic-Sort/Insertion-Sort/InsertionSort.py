from typing import List


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
