#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (61.50%)
# Likes:    367
# Dislikes: 0
# Total Accepted:    63.1K
# Total Submissions: 102.3K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
#
#

# @lc code=start


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, begin, path, res):
            res.append(path[:])
            for i in range(begin, len(nums)):
                if i > begin and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(nums, i+1, path, res)
                path.pop()
        res = []
        nums.sort()
        dfs(nums, 0, [], res)
        return res
# @lc code=end
