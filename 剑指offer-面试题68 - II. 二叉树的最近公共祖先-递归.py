# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
                3
            5       1
          6   2   0   8
             7 4
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。
注意：本题与主站 236 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
链接：https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof
    """
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):  # 返回结果为公共祖先或者 p、q 或者 None
            if not node:
                return None
            if node == p or node == q:
                return node  # 假如 q 在 p 的子节点，那么返回 p 是 q 的祖先没问题
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            if left:
                return left
            return right

        return dfs(root)


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
    # nums, p, q = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1
    nums, p, q = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4
    test = Solution()
    root, p, q = create(nums, p, q)
    ret = test.lowestCommonAncestor(root, p, q)
    print(ret)


if __name__ == '__main__':
    main()
