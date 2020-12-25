#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (59.65%)
# Likes:    478
# Dislikes: 0
# Total Accepted:    74.8K
# Total Submissions: 125.5K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
#
# 示例 2:
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow.next
        right = None
        slow.next = None

        while curr:
            next = curr.next
            curr.next = right
            right = curr
            curr = next

        dummy = ListNode(-1)
        curr = dummy
        while right:
            curr.next = head
            head = head.next
            curr.next.next = right
            right = right.next
            curr = curr.next.next
        if head:
            curr.next = head

        return dummy.next

# @lc code=end
