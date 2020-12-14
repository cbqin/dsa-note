from typing import List


class Solution:
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
