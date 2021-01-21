#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (64.26%)
# Likes:    475
# Dislikes: 0
# Total Accepted:    127.3K
# Total Submissions: 198.4K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
#
#
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
#
#
# 示例 2:
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
#
#

# @lc code=start


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, begin, path, res):
            if target == 0:
                res.append(path[:])
                return

            for i in range(begin, len(candidates)):
                if target-candidates[i] < 0:
                    break

                if i > begin and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])

                dfs(candidates, target-candidates[i], i+1, path, res)
                path.pop()
        res = []
        candidates.sort()
        dfs(candidates, target, 0, [], res)
        return res
# @lc code=end
