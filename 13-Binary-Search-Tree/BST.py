from typing import Optional


class Node(object):
    def __init__(self,
                 key: int,
                 val: int,
                 size: int,
                 left: Optional[Node] = None,
                 right: Optional[Node] = None)->None:
        self.key = key
        self.val = val
        self.size = size
        self.left = left
        self.right = right


class BST(object):

    def __init__(self):
        self.root = None

    def _size(self, node: Node)->int:
        if node is None:
            return 0
        return node.size

    def size(self)->int:
        return self._size(self.root)

    def isEmpty(self)->bool:
        return self.size() == 0

    def _get(self, node: Node, key: int)->int:
        if node is None:
            return None
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    def get(self, key):
        return self._get(self.root, key)

    def contains(self, key):
        return self.get(key) is not None

    def _put(self, node: Node, key: int, val: int)->Node:
        if node is None:
            return Node(key, val, 1)
        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1+self._size(node.left)+self._size*node.right
        return node

    def put(self, key: int, val: int)->None:
        self.root = self._put(self.root, key, val)
