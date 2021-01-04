#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
# https://leetcode-cn.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (49.35%)
# Likes:    326
# Dislikes: 0
# Total Accepted:    26.9K
# Total Submissions: 54.3K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
#
# 例如，
#
# [2,3,4] 的中位数是 3
#
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
#
# 设计一个支持以下两种操作的数据结构：
#
#
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
#
#
# 示例：
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
#
# 进阶:
#
#
# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
#
#
#

# @lc code=start

from heapq import heappop, heappush, heapreplace, heappushpop


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minh = []
        self.maxh = []

    def addNum(self, num: int) -> None:
        # if len(self.maxh) == len(self.minh):
        #     if len(self.minh) == 0 or num >= -self.maxh[0]:
        #         heappush(self.minh, num)
        #     else:
        #         pop = heapreplace(self.maxh, -num)
        #         heappush(self.minh, -pop)
        # else:
        #     if num > self.minh[0]:
        #         pop = heapreplace(self.minh, num)
        #         heappush(self.maxh, -pop)
        #     else:
        #         heappush(self.maxh, -num)
        if len(self.maxh) == len(self.minh):
            heappush(self.minh, -heappushpop(self.maxh, -num))
        else:
            heappush(self.maxh, -heappushpop(self.minh, num))

    def findMedian(self) -> float:
        if len(self.maxh) == len(self.minh):
            return (self.minh[0]-self.maxh[0])/2
        else:
            return self.minh[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
