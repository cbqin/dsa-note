#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#
# https://leetcode-cn.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Medium (43.55%)
# Likes:    424
# Dislikes: 0
# Total Accepted:    45.4K
# Total Submissions: 95.4K
# Testcase Example:  '"bcabc"'
#
# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
#
# 注意：该题与 1081
# https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters
# 相同
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
    def removeDuplicateLetters(self, s: str) -> str:
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
