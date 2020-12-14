from typing import List


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
