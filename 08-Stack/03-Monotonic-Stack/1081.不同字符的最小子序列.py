#
# @lc app=leetcode.cn id=1081 lang=python3
#
# [1081] 不同字符的最小子序列
#
# https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters/description/
#
# algorithms
# Medium (53.97%)
# Likes:    77
# Dislikes: 0
# Total Accepted:    8.9K
# Total Submissions: 15.6K
# Testcase Example:  '"bcabc"'
#
# 返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。
#
# 注意：该题与 316 https://leetcode.com/problems/remove-duplicate-letters/ 相同
#
#
#
# 示例 1：
#
#
# 输入：s = "bcabc"
# 输出："abc"
#
#
# 示例 2：
#
#
# 输入：s = "cbacdcbc"
# 输出："acdb"
#
#
#
# 提示：
#
#
# 1
# s 由小写英文字母组成
#
#
#

# @lc code=start


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        last_index = [-1]*26
        visited = [0]*26
        stack = list()
        for i, c in enumerate(s):
            last_index[ord(c)-ord('a')] = i

        for i, c in enumerate(s):
            if visited[ord(c)-ord('a')]:
                continue
            while stack and ord(c) < ord(stack[-1]) and last_index[ord(stack[-1])-ord('a')] > i:
                pop_c = stack.pop()
                visited[ord(pop_c)-ord('a')] = 0
            stack.append(c)
            visited[ord(c)-ord('a')] = 1

        res = ""
        while stack:
            res = stack.pop()+res

        return res

# @lc code=end
