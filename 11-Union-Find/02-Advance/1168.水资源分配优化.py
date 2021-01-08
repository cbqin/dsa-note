# 村里面一共有 n 栋房子。我们希望通过建造水井和铺设管道来为所有房子供水。

# 对于每个房子 i，我们有两种可选的供水方案：

# 一种是直接在房子内建造水井，成本为 wells[i]；
# 另一种是从另一口井铺设管道引水，数组 pipes 给出了在房子间铺设管道的成本，其中每个 pipes[i] = [house1, house2, cost] 代表用管道将 house1 和 house2 连接在一起的成本。当然，连接是双向的。
# 请你帮忙计算为所有房子都供水的最低总成本。


from typing import List
from heapq import heapify, heappop


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        queue = []
        for i, well in enumerate(wells):
            queue.append((well, 0, i+1))
        for pipe in pipes:
            queue.append((pipe[2], pipe[0], pipe[1]))
        heapify(queue)

        uf = UnionFind(n+1)

        res = 0
        while uf.getCount() > 1:
            pop = heappop(queue)
            print(uf.getCount())
            print(pop)
            print(uf.find(pop[1]))
            print(uf.find(pop[2]))
            print()
            if uf.find(pop[1]) == uf.find(pop[2]):
                continue
            uf.union(pop[1], pop[2])
            res += pop[0]
        return res


class UnionFind(object):
    def __init__(self, N: int):
        self.N = N
        self.count = N
        self.parents = [0]*N
        self.rank = [1]*N

        for i in range(N):
            self.parents[i] = i

    # 路径压缩：隔代压缩
    def find(self, x: int) -> int:
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    # 路径压缩：完全压缩
    # def find(self, x: int) -> int:
    #     if x != self.parents[x]:
    #         self.parents[x] = self.find(self.parents[x])
    #     return self.parents[x]

    # O(mα(n))
    def union(self, x: int, y: int) -> None:
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return

        if self.rank[rootx] == self.rank[rooty]:
            self.parents[rootx] = rooty
            self.rank[rooty] += 1
        elif self.rank[rootx] < self.rank[rooty]:
            self.parents[rootx] = rooty
        else:
            self.parents[rooty] = rootx

        self.count -= 1

    def getCount(self) -> int:
        return self.count


if __name__ == "__main__":
    s = Solution()
    r = s.minCostToSupplyWater(3, [1, 2, 2], [[1, 2, 1], [2, 3, 1]])
    print(r)
