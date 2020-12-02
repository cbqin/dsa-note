from typing import List

"""
选择右端点进行比较适是因为能保证最小值不会被丢弃。
可以通过讨论当 nums[hi] 为最小值是否唯一来讨论验证。
如果选择左端点，因为取中点时，mi = (lo + hi) >> 1，
mid 会偏向左侧，mid==left，导致最小值被丢弃。
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        if nums[lo] < nums[hi]:
            return nums[lo]
        while lo < hi:
            mi = (lo + hi) >> 1
            if nums[hi] == nums[mi]:
                hi -= 1
            elif nums[hi] < nums[mi]:
                lo = mi + 1
            else:
                hi = mi
        return nums[lo]


if __name__ == "__main__":
    pass
