from typing import List

"""
「使……最大值尽可能小」是二分搜索题目常见的问法。
此题中，最大值的取值范围为 [max(nums), sum(nums)],
相当于查找这个有序数组中符合条件的最小值，典型的二分查找。
条件怎么确定？
对于此范围内每一个最大值的取值，可以依据此值划分原数组，情况有二：
1. 如果划分的数组数量大于 m ，则说明此最大值太小了：lo = mi + 1
2. 如果划分的数组数量不大于 m ，则说明此最大值满足情况，至于是不是最小不能确定，
   需要收缩右边界，继续查找：hi = mi
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(mi):
            total, cnt = 0, 1  # cnt = 1，因为本来nums就在算作一个子数组
            for num in nums:
                if total + num > mi:
                    total = num
                    cnt += 1
                else:
                    total += num
            return cnt <= m

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mi = (lo + hi) >> 1
            if check(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo


if __name__ == "__main__":
    pass
