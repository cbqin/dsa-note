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


def heapify(x):
    n = len(x)
    for i in reversed(range(n//2)):
        _siftup(x, i)


def _siftup(heap, pos):
    pass


def _siftdown(heap, startpos, pos):
    # 其实是 siftup ，是因为伴随着索引的减少，所以叫 siftdown。
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
