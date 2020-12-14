from typing import List


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
