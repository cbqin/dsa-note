#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#
# https://leetcode-cn.com/problems/letter-case-permutation/description/
#
# algorithms
# Medium (66.11%)
# Likes:    244
# Dislikes: 0
# Total Accepted:    29K
# Total Submissions: 43.6K
# Testcase Example:  '"a1b2"'
#
# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
#
#
#
# 示例：
# 输入：S = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
#
# 输入：S = "3z4"
# 输出：["3z4", "3Z4"]
#
# 输入：S = "12345"
# 输出：["12345"]
#
#
#
#
# 提示：
#
#
# S 的长度不超过12。
# S 仅由数字和字母组成。
#
#
#

# @lc code=start


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def dfs(s, begin, path, res):
            if begin == len(s):
                res.append(path)
                return

            c = s[begin]
            dfs(s, begin+1, path+c, res)
            if c.isalpha():
                c = c.swapcase()
                dfs(s, begin+1, path+c, res)
        res = []
        dfs(S, 0, "", res)
        return res

# @lc code=end
