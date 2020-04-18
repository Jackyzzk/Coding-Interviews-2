# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
请实现两个函数，分别用来序列化和反序列化二叉树。
你可以将以下二叉树：
    1
   / \
  2   3
     / \
    4   5
序列化为 "[1,2,3,null,null,4,5]"
注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof
    """
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def bfs(node):
            que = [node]
            while que:
                node = que.pop(0)
                if node:
                    ret.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
                else:
                    ret.append(None)

        ret = []
        bfs(root)
        while ret and ret[-1] is None:
            ret.pop()
        # return str(ret).replace('None', 'null')
        return str(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def rebuild(nums):
            if not nums:
                return None
            root = TreeNode(nums.pop(0))
            que = [root]
            while que:
                node = que.pop(0)
                left = nums.pop(0) if nums else None
                right = nums.pop(0) if nums else None
                node.left = TreeNode(left) if left is not None else None
                node.right = TreeNode(right) if right is not None else None
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            return root

        return rebuild(eval(data))


def create(nums):
    if not nums:
        return None
    root = TreeNode(nums.pop(0))
    que = [root]
    while que:
        node = que.pop(0)
        left = nums.pop(0) if nums else None
        right = nums.pop(0) if nums else None
        node.left = TreeNode(left) if left is not None else None
        node.right = TreeNode(right) if right is not None else None
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
    return root


def main():
    nums = [1, 2, 3, None, None, 4, 5]
    nums = []
    nums = [-1, 0, 1]
    codec = Codec()
    ret = codec.deserialize(codec.serialize(create(nums)))
    return ret


if __name__ == '__main__':
    main()
