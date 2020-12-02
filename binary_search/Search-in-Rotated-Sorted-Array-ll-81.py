from typing import List

"""
复杂度？
"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mi = (lo + hi) >> 1
            if target == nums[mi]:
                return True
            if nums[lo] == nums[mi]:
                lo = lo + 1
            elif nums[lo] < nums[mi]:
                if nums[lo] <= target < nums[mi]:
                    hi = mi - 1
                else:
                    lo = mi + 1
            else:
                if nums[mi] < target <= nums[hi]:
                    lo = mi + 1
                else:
                    hi = mi - 1
        return False


if __name__ == "__main__":
    pass
