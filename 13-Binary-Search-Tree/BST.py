from typing import Optional


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class NoSuchElementError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class IllegalArgumentError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


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

    def _deleteMin(self, node: Node)->Node:
        if node.left is None:
            return node.right
        node.left = self._deleteMin(node.left)
        node.size = 1+self._size(node.left)+self._size(node.right)
        return node

    def deleteMin(self)->None:
        if self.isEmpty():
            raise NoSuchElementError("Delete Min.", "BST is empty.")
        self.root = self._deleteMin(self.root)

    def _deleteMax(self, node: Node)->Node:
        if node.right is None:
            return node.left
        node.right = self._deleteMax(node.right)
        node.size = 1+self._size(node.left)+self._size(node.right)
        return node

    def deleteMax(self)->None:
        if self.isEmpty():
            raise NoSuchElementError("Delete Max.", "BST is empty.")
        self.root.self._deleteMax(self.root)

    def _delete(self, node: Node, key: int)->Node:
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            temp = node
            node = self._min(temp.right)
            node.right = self._deleteMin(temp.right)
            node.left = temp.left
        node.size = 1+self._size(node.left)+self._size(node.right)
        return node

    def delete(self, key: int)->None:
        if self.isEmpty():
            raise NoSuchElementError("Delete.", "BST is empty.")
        self.root = self._delete(self.root, key)

    def _min(self, node: Node)->None:
        if node.left is None:
            return node
        return self._min(node.left)

    def min(self)->Node:
        if self.isEmpty():
            raise NoSuchElementError("Min.", "BST is empty.")
        return self._min(self.root).key

    def _max(self, node: Node)->None:
        if node.right is None:
            return node
        return self._max(node.right)

    def max(self)->Node:
        if self.isEmpty():
            raise NoSuchElementError("Max", "BST is empty.")
        return self._max(self.root).key

    def _floor(self, node: Node, key: int)->Node:
        if node is None:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self._floor(node.left, key)
        temp = self._floor(node.right, key)
        if temp is not None:
            return temp
        return node

    def floor(self, key: int)->int:
        if self.isEmpty():
            raise NoSuchElementError("Floor", "BST is empty.")
        node = self._floor(self.root, key)
        if node is None:
            raise NoSuchElementError("Floor", "Key is too small")
        else:
            return node.key

    def _ceiling(self, node: Node, key: int)->Node:
        if node is None:
            return None
        if key == node.key:
            return node
        elif key > node.key:
            return self._ceiling(node.right, key)
        temp = self._ceiling(node.left, key)
        if temp is not None:
            return temp
        return node

    def ceiling(self, key: int)->int:
        if self.isEmpty():
            raise NoSuchElementError("Floor", "BST is empty.")
        node = self._ceiling(self.root, key)
        if node is None:
            raise NoSuchElementError("Ceiling", "Key is too large")
        else:
            return node.key

    def _select(self, node: Node, rank: int)->int:
        if node is None:
            return None
        left_size = self._size(node.left)
        if left_size > rank:
            return self._select(node.left, rank)
        elif left_size < rank:
            return self._select(node, rank-left_size-1)
        else:
            return node.key

    def select(self, rank: int)->int:
        if rank < 0 or rank >= self.size():
            raise IllegalArgumentError("Select", "Illegal argument.")
        return self._select(self.root, rank)

    def _rank(self, node: Node, key: int)->int:
        if node is None:
            return 0
        if key < node.key:
            return self._rank(node.left, key)
        elif key > node.key:
            return 1+self._size(node.left)+self._rank(node.right, key)
        else:
            return self._size(node.left)

    def rank(self, key: int)->int:
        return self._rank(self.root, key)
