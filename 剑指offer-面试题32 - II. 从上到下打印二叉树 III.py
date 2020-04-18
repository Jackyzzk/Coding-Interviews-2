# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [20,9],
  [15,7]
]
节点总数 <= 1000
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
    """
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        que, ret = [root], []
        aux, rec = [], []
        level = 1  # 根为第1层
        while que:
            node = que.pop(0)
            if node.left:
                aux.append(node.left)
            if node.right:
                aux.append(node.right)
            rec.append(node.val)
            if not que:
                que, aux = aux, []  # 新生成一个[] 比用que快很多
                if level & 1:
                    ret.append(rec)
                else:
                    ret.append(rec[::-1])
                rec = []
                level ^= 1
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
    nums = [1, 2, 3, 4, None, None, 5]  # [[1],[3,2],[4,5]]
    test = Solution()
    ret = test.levelOrder(create(nums))
    print(ret)


if __name__ == '__main__':
    main()
