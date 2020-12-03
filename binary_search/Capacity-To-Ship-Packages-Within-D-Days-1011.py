from typing import List

"""
类似410，875
"""


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def check(mi):
            d = 1  # 剩余的重量算最后一天
            total = 0
            for weight in weights:
                if total + weight > mi:
                    total = weight
                    d += 1
                else:
                    total += weight
            return d <= D

        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mi = (lo + hi) >> 1
            if check(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo


if __name__ == "__main__":
    pass
