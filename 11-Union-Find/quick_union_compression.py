

class UnionFind(object):
    def __init__(self, N: int):
        self.N = N
        self.count = N
        self.parents = [0]*N

        for i in range(N):
            self.parents[i] = i

    # O(logN)
    # 路径压缩：隔代压缩
    # def find(self, x: int) -> int:
    #     while x != self.parents[x]:
    #         self.parents[x] = self.parents[self.parents[x]]
    #         x = self.parents[x]
    #     return x

    # 路径压缩：完全压缩
    def find(self, x: int) -> int:
        while x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    # O(logN)
    def union(self, x: int, y: int) -> None:
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return

        self.parents[rootx] = rooty

        self.count -= 1

    def getCount(self) -> int:
        return self.count
