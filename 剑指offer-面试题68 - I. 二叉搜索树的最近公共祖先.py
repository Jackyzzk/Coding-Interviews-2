# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先
表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
            6
        2       8
      0   4   7   9
         3 5
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。
注意：本题与主站 235 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof
    """
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            p, q = q, p
        while root:
            if q.val < root.val:
                root = root.left
            elif p.val > root.val:
                root = root.right
            else:  # if p.val <= root.val <= q.val:
                return root


def create(nums, p, q):
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
            if node.left.val == p:
                p = node.left
            elif node.left.val == q:
                q = node.left
        if node.right:
            que.append(node.right)
            if node.right.val == p:
                p = node.right
            elif node.right.val == q:
                q = node.right
    return root, p, q


def main():
    nums, p, q = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8
    nums, p, q = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4
    test = Solution()
    root, p, q = create(nums, p, q)
    ret = test.lowestCommonAncestor(root, p, q)
    print(ret)


if __name__ == '__main__':
    main()
