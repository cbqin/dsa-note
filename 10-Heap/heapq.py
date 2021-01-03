"""Heap queue algorithm (a.k.a. priority queue).
Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for
all k, counting elements from 0.  For the sake of comparison,
non-existing elements are considered to be infinite.  The interesting
property of a heap is that a[0] is always its smallest element.
Usage:
heap = []            # creates an empty heap
heappush(heap, item) # pushes a new item on the heap
item = heappop(heap) # pops the smallest item from the heap
item = heap[0]       # smallest item on the heap without popping it
heapify(x)           # transforms list into a heap, in-place, in linear time
item = heapreplace(heap, item) # pops and returns smallest item, and adds
                               # new item; the heap size is unchanged
"""


def heappush(heap, item):
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)


def heappop(heap):
    lastelt = heap.pop()
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt


def heapreplace(heap, item):
    returnitem = heap[0]
    heap[0] = item
    _siftup(heap, 0)
    return returnitem


def heappushpop(heap, item):
    if heap and heap[0] < item:
        item, heap[0] = heap[0], item
        _siftup(heap, 0)
    return item


def heapify(x):
    n = len(x)
    for i in reversed(range(n//2)):
        _siftup(x, i)


def _siftup(heap, pos):
    # 其实是 siftdown ，是因为伴随着索引的增大，所以叫 siftdup。
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]

    # Bubble up the smaller child until hitting a leaf.
    # 使最小的子节点上浮，直到父节点到达叶子节点
    childpos = 2*pos+1  # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos+1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos

        # Move the smaller child up
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos+1

    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


def _siftdown(heap, startpos, pos):
    # 其实是 siftup ，是因为伴随着索引的减小，所以叫 siftdown。
    newitem = heap[pos]

    while pos < startpos:
        parentpos = (pos-1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break

    heap[pos] = newitem


def _siftup_max(heap, pos):
    pass


def _siftdown_max(heap, startpos, pos):
    pass
