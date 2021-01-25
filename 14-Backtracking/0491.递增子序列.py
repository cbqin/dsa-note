#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#
# https://leetcode-cn.com/problems/increasing-subsequences/description/
#
# algorithms
# Medium (55.97%)
# Likes:    243
# Dislikes: 0
# Total Accepted:    32K
# Total Submissions: 57.1K
# Testcase Example:  '[4,6,7,7]'
#
# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
#
# 示例:
#
#
# 输入: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7],
# [4,7,7]]
#
# 说明:
#
#
# 给定数组的长度不会超过15。
# 数组中的整数范围是 [-100,100]。
# 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
#
#
#

# @lc code=start


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, begin, path, res, length):
            if len(path) > 1:
                res.append(path[:])

            seen = set()
            for i in range(begin, length):
                if nums[i] in seen:
                    continue
                if not path or nums[i] >= path[-1]:
                    path.append(nums[i])
                    dfs(nums, i+1, path, res, length)
                    path.pop()
                    seen.add(nums[i])

        res = []
        dfs(nums, 0, [], res, len(nums))
        return res

# @lc code=end
