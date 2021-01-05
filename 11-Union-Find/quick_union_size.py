

class UnionFind(object):
    def __init__(self, N: int):
        self.N = N
        self.count = N
        self.parents = [0]*N
        self.size = [1]*N

        for i in range(N):
            self.parents[i] = i

    # O(logN)
    def find(self, x: int) -> int:
        while x != self.parents[x]:
            x = self.parents[x]

        return x

    # O(logN)
    def union(self, x: int, y: int) -> None:
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return

        if self.size[rootx] >= self.size[rooty]:
            self.parents[rooty] = rootx
            self.size[rootx] += self.size[rooty]
        else:
            self.parents[rootx] = rooty
            self.size[rooty] += self.size[rootx]

        self.count -= 1

    def getCount(self) -> int:
        return self.count
