# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回：
[3,9,20,15,7]
节点总数 <= 1000
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
    """
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        que, ret = [root], []
        while que:
            node = que.pop(0)
            ret.append(node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return ret


def create(nums):
    root = TreeNode(nums.pop(0))
    que = [root]
    while que:
        node = que.pop(0)
        left = nums.pop(0) if nums else None
        right = nums.pop(0) if nums else None
        node.left = TreeNode(left) if left else None
        node.right = TreeNode(right) if right else None
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
    return root


def main():
    nums = [3, 9, 20, None, None, 15, 7]
    test = Solution()
    ret = test.levelOrder(create(nums))
    print(ret)


if __name__ == '__main__':
    main()
