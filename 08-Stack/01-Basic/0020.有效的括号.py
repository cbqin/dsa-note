#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (39.96%)
# Likes:    1178
# Dislikes: 0
# Total Accepted:    153.8K
# Total Submissions: 384K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
#
#
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
#
#
# 示例 3:
#
# 输入: "(]"
# 输出: false
#
#
# 示例 4:
#
# 输入: "([)]"
# 输出: false
#
#
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
#
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = list()
        m = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c in m:
                stack.append(c)
            else:
                if stack and m[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return True if not stack else False


# @lc code=end
