#
# @lc app=leetcode.cn id=945 lang=python3
#
# [945] 使数组唯一的最小增量
#
# https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/description/
#
# algorithms
# Medium (48.35%)
# Likes:    158
# Dislikes: 0
# Total Accepted:    32.2K
# Total Submissions: 66.5K
# Testcase Example:  '[1,2,2]'
#
# 给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
#
# 返回使 A 中的每个值都是唯一的最少操作次数。
#
# 示例 1:
#
# 输入：[1,2,2]
# 输出：1
# 解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
#
# 示例 2:
#
# 输入：[3,2,1,2,1,7]
# 输出：6
# 解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
# 可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
#
#
# 提示：
#
#
# 0 <= A.length <= 40000
# 0 <= A[i] < 40000
#
#
#

# @lc code=start


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        ans = 0
        taken = 0
        count = [0]*80000
        for num in A:
            count[num] += 1

        for num in range(80000):
            if count[num] >= 2:
                taken += count[num]-1
                ans -= (count[num]-1)*num
            elif taken > 0 and count[num] == 0:
                taken -= 1
                ans += num
        return ans

# @lc code=end
