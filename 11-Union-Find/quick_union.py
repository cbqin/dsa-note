

class UnionFind(object):
    def __init__(self, N: int):
        self.N = N
        self.count = N
        self.parents = [0]*N

        for i in range(N):
            self.parents[i] = i

    # O(lonN)
    def find(self, x: int) -> int:
        while x != self.parents[x]:
            x = self.parents[x]

        return x

    # O(lonN)
    def union(self, x: int, y: int) -> None:
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return

        self.parents[rootx] = rooty

        self.count -= 1

    def getCount(self) -> int:
        return self.count
