"""
在这个版本的二分查找中，返回的是不大于目标值的最后一个位置。
这种返回模式可以处理很多问题。

二分搜索有4个基本变种：
1. 查找第一个与 target 相等的元素
   查找 target-1 即可，返回的是第一个与 target 相等的元素左侧的位置 index ，
   需要判断 index+1 位置的值的情况
2. 查找最后一个与 target 相等的元素
   正符合本版本语义
3. 查找第一个大于等于 target 的元素
   与 1 相同
4. 查找最后一个小于等于 target 的元素
   与 2 相同

题型主要分为三种：
1. 有序
2. 基本有序：33，81，153，154，162，852
3. 最大值最小化问题，求在最小满足条件的情况下的最大值：410，875，1011，1283
"""


def binary_search(arr, e, lo, hi):
    while lo < hi:
        mi = (lo+hi) >> 1
        if e < arr[mi]:
            hi = mi
        else:
            lo = mi+1
    return lo-1


def binary_search_first_equal(arr, e, lo, hi):
    """
    查找第一个与 target 相等的元素
    如果存在，返回下标
    如果不存在，返回 -1
    """
    while lo < hi:
        mi = (lo+hi) >> 1
        if e < arr[mi]:
            hi = mi
        else:
            lo = mi+1
    if lo == len(arr):
        return -1
    if arr[lo] == e+1:  # 注意与 e+1 比较
        return lo
    else:
        return -1


def binary_search_first_large_equal(arr, e, lo, hi):
    """
    查找第一个大于等于 target 的元素
    如果存在，返回下标
    如果不存在，返回 -1
    """
    while lo < hi:
        mi = (lo+hi) >> 1
        if e < arr[mi]:
            hi = mi
        else:
            lo = mi+1
    if lo == len(arr):
        return -1
    return lo  # 此时就不需要判断相不相等，因为 lo-1 位置是不大于 e-1 的最后位置，lo 位置就是大于等于 e 的第一个位置


def binary_search_last_equal(arr, e, lo, hi):
    """
    查找最后一个与 target 相等的元素
    如果存在，返回下标
    如果不存在，返回 -1
    """
    while lo < hi:
        mi = (lo+hi) >> 1
        if e < arr[mi]:
            hi = mi
        else:
            lo = mi+1
    return lo-1 if arr[lo-1] == e else -1


def binary_search_last_large_equal(arr, e, lo, hi):
    """
    查找最后一个小于等于 target 的元素
    如果存在，返回下标
    如果不存在，返回 -1
    """
    while lo < hi:
        mi = (lo+hi) >> 1
        if e < arr[mi]:
            hi = mi
        else:
            lo = mi+1
    if lo-1 == -1:
        return -1
    return lo-1


if __name__ == "__main__":
    arr = [1, 2, 4, 4, 4, 4, 5, 6, 7]
    es = [1, 0, 9, 7, 3, 4]
    for e in es:
        index = binary_search(arr, e, 0, len(arr))
        print(index)
