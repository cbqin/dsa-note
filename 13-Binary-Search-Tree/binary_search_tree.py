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
