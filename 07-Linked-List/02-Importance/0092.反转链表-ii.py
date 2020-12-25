#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (51.83%)
# Likes:    607
# Dislikes: 0
# Total Accepted:    91.6K
# Total Submissions: 176.5K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
#
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        for _ in range(m-1):
            pre = pre.next

        cur = pre.next
        tail = cur
        temp_pre = None
        next = None
        for _ in range(n-m+1):
            next = cur.next
            cur.next = temp_pre
            temp_pre = cur
            cur = next
        pre.next = temp_pre
        tail.next = next

        return dummy.next

# @lc code=end
