# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点
（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。节点总数 <= 10000
注意：本题与主站 104 题相同：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof
    """
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return max(left, right) + 1

        return dfs(root)


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
    ret = test.maxDepth(create(nums))
    print(ret)


if __name__ == '__main__':
    main()
