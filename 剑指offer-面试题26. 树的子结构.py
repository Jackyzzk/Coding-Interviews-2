# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。
给定的树 A:
     3
    / \
   4   5
  / \
 1   2
给定的树 B：
   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
输入：A = [1,2,3], B = [3,1]
输出：false
输入：A = [3,4,5,1,2], B = [4,1]
输出：true
0 <= 节点个数 <= 10000
链接：https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof
    """
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        def dfs(node1, node2):
            que = [(node1, node2)]
            while que:
                p1, p2 = que.pop()
                if p1 and p2:
                    if p1.val != p2.val:
                        return False
                    que.append((p1.right, p2.right))
                    que.append((p1.left, p2.left))
                elif p2:
                    return False
            return True

        que = [A]
        while que:
            node = que.pop()
            if node and B:
                if node.val == B.val and dfs(node, B):
                    return True
                que.append(node.right)
                que.append(node.left)
        return False


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
    nums1, nums2 = [1, 2, 3], [3, 1]
    # nums1, nums2 = [3, 4, 5, 1, 2], [4, 1]
    nums1, nums2 = [-1, 3, 2, 0], []
    test = Solution()
    ret = test.isSubStructure(create(nums1), create(nums2))
    print(ret)


if __name__ == '__main__':
    main()
