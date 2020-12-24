#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# https://leetcode-cn.com/problems/partition-list/description/
#
# algorithms
# Medium (60.29%)
# Likes:    287
# Dislikes: 0
# Total Accepted:    62.4K
# Total Submissions: 103.4K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
#
#
# 示例:
#
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        pre = dummy
        cur = head
        while cur and cur.val < x:
            pre = cur
            cur = cur.next

        ge_node = cur

        pre2 = None
        while cur:
            if cur.val >= x:
                pre2 = cur
                cur = cur.next
            else:
                next = cur.next
                pre.next = cur
                cur.next = ge_node
                pre2.next = next
                cur = next
                pre = pre.next
        return dummy.next

# @lc code=end
