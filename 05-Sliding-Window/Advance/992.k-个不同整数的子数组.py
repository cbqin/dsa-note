#
# @lc app=leetcode.cn id=992 lang=python3
#
# [992] K 个不同整数的子数组
#
# https://leetcode-cn.com/problems/subarrays-with-k-different-integers/description/
#
# algorithms
# Hard (32.15%)
# Likes:    134
# Dislikes: 0
# Total Accepted:    5.9K
# Total Submissions: 18.3K
# Testcase Example:  '[1,2,1,2,3]\n2'
#
# 给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。
#
# （例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）
#
# 返回 A 中好子数组的数目。
#
#
#
# 示例 1：
#
# 输入：A = [1,2,1,2,3], K = 2
# 输出：7
# 解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2],
# [1,2,1,2].
#
#
# 示例 2：
#
# 输入：A = [1,2,1,3,4], K = 3
# 输出：3
# 解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 20000
# 1 <= A[i] <= A.length
# 1 <= K <= A.length
#
#
#

# @lc code=start


class Window:
    def __init__(self):
        self.counter = collections.Counter()
        self.unique = 0

    def add(self, x):
        self.counter[x] += 1
        if self.counter[x] == 1:
            self.unique += 1

    def remove(self, x):
        self.counter[x] -= 1
        if self.counter[x] == 0:
            self.unique -= 1


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        window1 = Window()
        window2 = Window()

        ans = 0
        left1 = 0
        left2 = 0

        for x in A:
            window1.add(x)
            window2.add(x)

            while window1.unique > K:
                window1.remove(A[left1])
                left1 += 1

            while window2.unique >= K:
                window2.remove(A[left2])
                left2 += 1

            ans += left2-left1
        return ans


# @lc code=end
