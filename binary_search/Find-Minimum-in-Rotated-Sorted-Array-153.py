from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        left = nums[lo]
        if left < nums[hi]:
            return left
        while lo < hi:
            mi = (lo + hi) >> 1
            if left <= nums[mi]:  # <=:[2,1]
                lo = mi + 1
            else:
                hi = mi
        return nums[lo]


if __name__ == "__main__":
    pass
