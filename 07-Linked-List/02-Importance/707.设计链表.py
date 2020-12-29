#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#
# https://leetcode-cn.com/problems/design-linked-list/description/
#
# algorithms
# Medium (29.31%)
# Likes:    191
# Dislikes: 0
# Total Accepted:    33.9K
# Total Submissions: 114.9K
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n[[],[1],[3],[1,2],[1],[1],[1]]'
#
# 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next
# 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。
#
# 在链表类中实现这些功能：
#
#
# get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
# addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
# addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
# addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index
# 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
# deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
#
#
#
#
# 示例：
#
# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
# linkedList.get(1);            //返回2
# linkedList.deleteAtIndex(1);  //现在链表是1-> 3
# linkedList.get(1);            //返回3
#
#
#
#
# 提示：
#
#
# 所有val值都在 [1, 1000] 之内。
# 操作次数将在  [1, 1000] 之内。
# 请不要使用内置的 LinkedList 库。
#
#
#

# @lc code=start


class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy = LinkedListNode(-1)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        p = self.dummy.next
        while p and index:
            p = p.next
            index -= 1
        if p:
            return p.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = LinkedListNode(val)
        node.next = self.dummy.next
        self.dummy.next = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        p = self.dummy
        while p.next:
            p = p.next
        node = LinkedListNode(val)
        p.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            self.addAtHead(val)
            return
        node = LinkedListNode(val)
        p = self.dummy
        while p and index:
            p = p.next
            index -= 1
        if p:
            node.next = p.next
            p.next = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        p = self.dummy
        while p and index:
            p = p.next
            index -= 1
        if p and p.next:
            node = p.next
            p.next = node.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
