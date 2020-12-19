from typing import List

"""
1 <= A.length <= 10000
0 <= A[i] <= 100000
"""


class BucketSort:
    def bucketSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums

        step = 1000
        buckets = 100000//step

        temp = [[0]*n for _ in range(buckets)]
        next = [0]*(buckets)

        for num in nums:
            bucket_index = num//step
            temp[bucket_index][next[bucket_index]] = num
            next[bucket_index] += 1

        for i in range(buckets):
            self.insertionSort(temp[i], next[i])

        res = []
        for i in range(buckets):
            cur_len = next[i]
            for j in range(cur_len):
                res.append(temp[i][j])

        return res

    def insertionSort(self, nums: List[int], end_index: int) -> None:
        for i in range(1, end_index):
            temp = nums[i]
            j = i
            while j > 0 and nums[j-1] > temp:
                nums[j] = nums[j-1]
                j -= 1
            nums[j] = temp


if __name__ == "__main__":
    nums = [2, 5, 3, 0, 2, 3, 0, 3]
    bs = BucketSort()
    nums = bs.bucketSort(nums)
    print(nums)
