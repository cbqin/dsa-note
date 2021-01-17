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
        self._insert(self.root, key, value)

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
        pass
