#
# @lc app=leetcode.cn id=460 lang=python3
#
# [460] LFU 缓存
#
# https://leetcode-cn.com/problems/lfu-cache/description/
#
# algorithms
# Hard (42.81%)
# Likes:    308
# Dislikes: 0
# Total Accepted:    19.5K
# Total Submissions: 45.5K
# Testcase Example:  '["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]'
#
# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。
#
# 实现 LFUCache 类：
#
#
# LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
# int get(int key) - 如果键存在于缓存中，则获取键的值，否则返回 -1。
# void put(int key, int value) -
# 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除
# 最久未使用 的键。
#
#
# 注意「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。
#
#
#
# 进阶：
#
#
# 你是否可以在 O(1) 时间复杂度内执行两项操作？
#
#
#
#
# 示例：
#
#
# 输入：
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get",
# "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# 输出：
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
#
# 解释：
# LFUCache lFUCache = new LFUCache(2);
# lFUCache.put(1, 1);
# lFUCache.put(2, 2);
# lFUCache.get(1);      // 返回 1
# lFUCache.put(3, 3);   // 去除键 2
# lFUCache.get(2);      // 返回 -1（未找到）
# lFUCache.get(3);      // 返回 3
# lFUCache.put(4, 4);   // 去除键 1
# lFUCache.get(1);      // 返回 -1（未找到）
# lFUCache.get(3);      // 返回 3
# lFUCache.get(4);      // 返回 4
#
#
#
#
# 提示：
#
#
# 0
# 最多调用 10^5 次 get 和 put 方法
#
#
#

# @lc code=start


class DoubleLinkedListNode:

    def __init__(self, key, value, freq=0):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None

    def insert(self, next_node):
        next_node.prev = self
        next_node.next = self.next
        self.next.prev = next_node
        self.next = next_node


def createList():
    head = DoubleLinkedListNode(0, 0)
    tail = DoubleLinkedListNode(0, 0)
    head.next = tail
    tail.prev = head

    return (head, tail)


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.freq = collections.defaultdict(createList)
        self.size = 0
        self.min_freq = 0

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
            node.next.prev = node.prev
            head, tail = self.freq[node.freq]
            if node.prev is head and node.next is tail:
                self.freq.pop(node.freq)
        return node.key

    def increase(self, node):
        node.freq += 1
        self.delete(node)
        self.freq[node.freq][-1].prev.insert(node)
        if node.freq == 1:
            self.min_freq = 1
        elif node.freq-1 == self.min_freq:
            head, tail = self.freq[node.freq-1]
            if head.next is tail:
                self.min_freq = node.freq

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.increase(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            if key in self.cache:
                node = self.cache[key]
                node.value = value
            else:
                node = DoubleLinkedListNode(key, value)
                self.size += 1
                self.cache[key] = node

            if self.size > self.capacity:
                self.size -= 1
                deleted = self.delete(self.freq[self.min_freq][0].next)
                self.cache.pop(deleted)

            self.increase(node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
