# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
节点总数 <= 10000
注意：本题与主站 113 题相同：https://leetcode-cn.com/problems/path-sum-ii/
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
    """
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(node):
            rec.append(node.val)
            self.rest -= node.val
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            if not (node.left or node.right) and self.rest == 0:
                ret.append(rec[:])
            self.rest += node.val
            rec.pop()

        if not root:
            return []
        ret, rec = [], []
        self.rest = sum
        dfs(root)
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
    nums, sum = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22
    nums, sum = [1, -2, -3, 1, 3, -2, None, -1], -1
    test = Solution()
    ret = test.pathSum(create(nums), sum)
    print(ret)


if __name__ == '__main__':
    main()
