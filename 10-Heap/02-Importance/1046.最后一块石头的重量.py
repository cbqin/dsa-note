#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#
# https://leetcode-cn.com/problems/last-stone-weight/description/
#
# algorithms
# Easy (61.49%)
# Likes:    137
# Dislikes: 0
# Total Accepted:    52.1K
# Total Submissions: 78.9K
# Testcase Example:  '[2,7,4,1,8,1]'
#
# 有一堆石头，每块石头的重量都是正整数。
#
# 每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
#
#
# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
#
#
# 最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。
#
#
#
# 示例：
#
# 输入：[2,7,4,1,8,1]
# 输出：1
# 解释：
# 先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
# 再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
# 接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
# 最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
#
#
#
# 提示：
#
#
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
#
#
#

# @lc code=start
from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-stone for stone in stones]
        heapify(h)

        if len(h) == 1:
            return -h[0]

        while h:
            x = heappop(h)
            if not h:
                return -x
            y = heappop(h)

            if x != y:
                heappush(h, x-y)

        if h:
            return -h[0]
        else:
            return 0


# @lc code=end
