from typing import List

"""
最小速度取值范围：[1, max(piles)]
对于其中的每一个值去判断用的小时数是否大于 H
如果大于，则速度过慢：lo = mi + 1
否则，速度过快：hi = mi
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def check(k):
            h = 0
            for pile in piles:
                h += pile // k
                h = h if pile % k == 0 else h + 1
            return h <= H

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) >> 1
            if check(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo


if __name__ == "__main__":
    pass
