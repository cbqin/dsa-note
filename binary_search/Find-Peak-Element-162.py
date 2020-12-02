from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mi = (lo + hi) >> 1
            if nums[mi] < nums[mi+1]:
                lo = mi + 1
            else:
                hi = mi
        return lo


if __name__ == "__main__":
    pass
