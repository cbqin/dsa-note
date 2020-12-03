from typing import List
import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(mi):
            total = 0
            for num in nums:
                total += math.ceil(num/mi)
            return total <= threshold

        lo, hi = 1, max(nums)
        while lo < hi:
            mi = (lo + hi) >> 1
            if check(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo


if __name__ == "__main__":
    pass
