from typing import Optional


class TreeNode(object):
    def __init__(self,
                 key: int,
                 value: int,
                 left: Optional[TreeNode] = None,
                 right: Optional[TreeNode] = None
                 ) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def insert(self, key: int, value: int) -> None:
        self.root = self._insert(self.root, key, value)

    def _insert(self, node: TreeNode, key: int, value: int) -> TreeNode:
        if node is None:
            self.size += 1
            return TreeNode(key, value)

        if key == node.key:
            node.value = value
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        return node

    def search(self, key: int) -> int:
        return self._search(self.root, key)

    def _search(self, node: TreeNode, key: int) -> int:
        if node is None:
            return None

        if key == node.key:
            return node.value
        elif key < node.value:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def contain(self, key: int) -> bool:
        return self._contain(self.root, key)

    def _contain(self, node: TreeNode, key: int) -> bool:
        if node is None:
            return False

        if key == node.key:
            return True
        elif key < node.key:
            return self._contain(node.left, key)
        else:
            return self._contain(node.right, key)

    def remove(self, key: int) -> None:
        self.root = self._remove(self.root, key)

    def _remove(self, node: TreeNode, key: int) -> TreeNode:
        if node is None:
            return None

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                right = node.right
                node.right = None
                del node
                self.size -= 1
                return right

            if node.right is None:
                left = node.left
                node.left = None
                del node
                self.size -= 1
                return left

            successor = self.minimum(node.right)
            self.size += 1
            successor.right = self.removeMinimum(node.right)
            successor.left = node.left
            node.left = None
            node.right = None
            del node
            self.size -= 1
            return successor

    def minimum(self, node: TreeNode) -> TreeNode:
        if node.left is None:
            return node

        return self.minimum(node.left)

    def removeMinimum(self, node: TreeNode) -> TreeNode:
        if node.left is None:
            right = node.right
            node.right = None
            self.size -= 1
            return right

        node.left = self.removeMinimum(node.left)

        return node

    def removeMin(self, node: TreeNode) -> None:
        if self.root:
            self.root = self.removeMinimum(self.root)

    def floor(self, key: int) -> int:
        return self._floor(self.root, key)

    def _floor(self, node: TreeNode, key: int) -> int:
        if node is None:
            return None

        if key == node.key:
            return node.key
        if key < node.key:
            return self._floor(node.left, key)
        temp = self._floor(node.right, key)
        if temp:
            return temp
        return node.key

    def ceiling(self, key: int) -> int:
        return self._ceiling(self.root, key)

    def _ceiling(self, node: TreeNode, key: int) -> int:
        if node is None:
            return None

        if key == node.key:
            return node.key
        if key > node.key:
            return self._ceiling(node.right, key)
        temp = self._ceiling(node.left, key)
        if temp:
            return temp
        return node.key
