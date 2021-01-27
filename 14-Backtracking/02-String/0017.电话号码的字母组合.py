#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (55.57%)
# Likes:    1093
# Dislikes: 0
# Total Accepted:    214.4K
# Total Submissions: 384.9K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
#
#

# @lc code=start


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(digits, digits_map, index, path, res):
            if len(path) == len(digits):
                res.append(path)
                return

            next_digit = digits_map[int(digits[index])-2]
            for c in next_digit:
                dfs(digits, digits_map, index+1, path+c, res)

        if not digits:
            return []
        digits_map = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        dfs(digits, digits_map, 0, "", res)
        return res

# @lc code=end
