#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (51.27%)
# Likes:    1069
# Dislikes: 0
# Total Accepted:    119.3K
# Total Submissions: 232.6K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
#
#
#
# 实现 LRUCache 类：
#
#
# LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value)
# 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#
#
#
#
#
#
# 进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？
#
#
#
# 示例：
#
#
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#
#
#
#
# 提示：
#
#
# 1
# 0
# 0
# 最多调用 3 * 10^4 次 get 和 put
#
#
#

# @lc code=start


class DoubleLinkedList:

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.dummy_head = DoubleLinkedList()
        self.dummy_tail = DoubleLinkedList()
        self.dummy_head.next = self.dummy_tail
        self.dummy_head.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)
        else:
            node = DoubleLinkedList(key, value)
            self.addToHead(node)
            self.cache[key] = node

            if len(self.cache) > self.capacity:
                node = self.removeTail()
                self.cache.pop(node.key)

    def moveToHead(self, node: DoubleLinkedList) -> None:
        self.removeNode(node)
        self.addToHead(node)

    def removeNode(self, node: DoubleLinkedList) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        node.prev = None
        node.next = None

    def addToHead(self, node: DoubleLinkedList) -> None:
        head = self.dummy_head.next
        self.dummy_head.next = node
        node.prev = self.dummy_head
        node.next = head
        head.prev = node

    def removeTail(self) -> DoubleLinkedList:
        node = self.dummy_tail.prev
        self.removeNode(node)
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
