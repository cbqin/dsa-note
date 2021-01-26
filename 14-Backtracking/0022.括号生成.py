#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (76.55%)
# Likes:    1533
# Dislikes: 0
# Total Accepted:    220.6K
# Total Submissions: 287.5K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例 1：
#
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：["()"]
#
#
#
#
# 提示：
#
#
# 1
#
#
#

# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, path, res):
            if left == 0 and right == 0:
                res.append(path)
                return

            if left > 0:
                dfs(left-1, right, path+"(", res)

            if left < right:
                dfs(left, right-1, path+")", res)

        res = []
        dfs(n, n, "", res)
        return res
# @lc code=end
