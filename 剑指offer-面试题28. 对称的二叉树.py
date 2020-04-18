# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
请实现一个函数，用来判断一棵二叉树是不是对称的。
如果一棵二叉树和它的镜像一样，那么它是对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3
输入：root = [1,2,2,3,4,4,3]
输出：true
输入：root = [1,2,2,null,3,null,3]
输出：false
0 <= 节点个数 <= 1000
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
    """
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def judge(n1, n2):
            if n1 and n2:
                if n1.val == n2.val:
                    return judge(n1.left, n2.right) and judge(n1.right, n2.left)
            elif not (n1 or n2):
                return True

        return True if not root or judge(root.left, root.right) else False


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
    nums = [1, 2, 2, 3, 4, 4, 3]
    # nums = [1, 2, 2, None, 3, None, 3]
    test = Solution()
    ret = test.isSymmetric(create(nums))
    print(ret)


if __name__ == '__main__':
    main()
