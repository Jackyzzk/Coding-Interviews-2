# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7
限制：
0 <= 节点个数 <= 5000
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
    """
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def rebuild(p1, p2, p3, p4):
            if p2 < p1:
                return None
            root = TreeNode(preorder[p1])
            i = inorder.index(preorder[p1])
            # 在 inorder 中划分左右子树区间范围，得出区间长度后就可以在 preorder 中划分左右子树
            root.left = rebuild(p1 + 1, p1 + i - p3, p3, i - 1)
            root.right = rebuild(p1 + i - p3 + 1, p2, i + 1, p4)
            return root

        n = len(preorder)
        root = rebuild(0, n - 1, 0, n - 1)
        return root


def main():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    test = Solution()
    ret = test.buildTree(preorder, inorder)
    print(ret)


if __name__ == '__main__':
    main()
