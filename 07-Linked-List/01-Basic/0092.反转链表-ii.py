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
    # def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    #     curr_node = head
    #     index = 1
    #     last_node = None
    #     while index < m:
    #         last_node = curr_node
    #         curr_node = curr_node.next
    #         index += 1
    #     pre_node = None
    #     new_tail = curr_node
    #     while index <= n:
    #         next_node = curr_node.next
    #         curr_node.next = pre_node
    #         pre_node = curr_node
    #         curr_node = next_node
    #         index += 1
    #     new_tail.next = curr_node
    #     if last_node:
    #         last_node.next = pre_node
    #         return head
    #     else:
    #         return pre_node

    successor = None

    def reverseN(self, head: ListNode, n: int) -> ListNode:
        if n == 1:
            self.successor = head.next
            return head

        next_node = head.next
        last_node = self.reverseN(next_node, n-1)
        next_node.next = head
        head.next = self.successor
        return last_node

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.reverseN(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head


# @lc code=end
