

class UnionFind(object):
    def __init__(self, N: int):
        self.N = N
        self.count = N
        self._id = [0]*N

        for i in range(N):
            self._id[i] = i

    # O(1)
    def find(self, x: int) -> int:
        return self._id[x]

    # O(N)
    def union(self, x: int, y: int) -> None:
        xid = self.find(x)
        yid = self.find(y)

        if xid == yid:
            return

        for i in range(self.N):
            if self._id[i] == xid:
                self._id[i] = yid

        self.count -= 1

    def getCount(self) -> int:
        return self.count
