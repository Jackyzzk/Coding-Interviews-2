# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一棵二叉搜索树，请找出其中第k大的节点。
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
1 ≤ k ≤ 二叉搜索树元素个数
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof
    """
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        que, node = [], root
        while que or node:
            while node:
                que.append(node)
                node = node.right
            node = que.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.left


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
    nums, k = [3, 1, 4, None, 2], 1
    nums, k = [5, 3, 6, 2, 4, None, None, 1], 3
    test = Solution()
    ret = test.kthLargest(create(nums), k)
    print(ret)


if __name__ == '__main__':
    main()
