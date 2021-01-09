#
# @lc app=leetcode.cn id=721 lang=python3
#
# [721] 账户合并
#
# https://leetcode-cn.com/problems/accounts-merge/description/
#
# algorithms
# Medium (36.89%)
# Likes:    146
# Dislikes: 0
# Total Accepted:    7.3K
# Total Submissions: 19.7K
# Testcase Example:  '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
#
# 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称
# (name)，其余元素是 emails 表示该账户的邮箱地址。
#
#
# 现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
#
# 合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。账户本身可以以任意顺序返回。
#
#
#
# 示例 1：
#
#
# 输入：
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John",
# "johnnybravo@mail.com"], ["John", "johnsmith@mail.com",
# "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# 输出：
# [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
# ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# 解释：
# 第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。
# 第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
# 可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
# ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']]
# 也是正确的。
#
#
#
#
# 提示：
#
#
# accounts的长度将在[1，1000]的范围内。
# accounts[i]的长度将在[1，10]的范围内。
# accounts[i][j]的长度将在[1，30]的范围内。
#
#
#

# @lc code=start

from typing import List
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(10000)
        em_to_name = {}
        em_to_id = {}
        em_id = 0

        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = em_id
                    em_id += 1
                uf.union(em_to_id[emails[0]], em_to_id[email])

        merged_emails = defaultdict(list)
        for email, idd in em_to_id.items():
            merged_emails[uf.find(idd)].append(email)

        ans = []
        for emails in merged_emails.values():
            ans.append([em_to_name[emails[0]]]+sorted(emails))
        return ans


class UnionFind(object):
    def __init__(self, N: int):
        self.N = N
        self.count = N
        self.parents = [0]*N
        self.rank = [1]*N

        for i in range(N):
            self.parents[i] = i

    # 路径压缩：隔代压缩
    def find(self, x: int) -> int:
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    # 路径压缩：完全压缩
    # def find(self, x: int) -> int:
    #     if x != self.parents[x]:
    #         self.parents[x] = self.find(self.parents[x])
    #     return self.parents[x]

    # O(mα(n))
    def union(self, x: int, y: int) -> None:
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return

        if self.rank[rootx] == self.rank[rooty]:
            self.parents[rootx] = rooty
            self.rank[rooty] += 1
        elif self.rank[rootx] < self.rank[rooty]:
            self.parents[rootx] = rooty
        else:
            self.parents[rooty] = rootx

        self.count -= 1

    def getCount(self) -> int:
        return self.count


# @lc code=end
