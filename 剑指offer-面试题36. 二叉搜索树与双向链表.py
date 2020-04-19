# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    """
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
要求不能创建任何新的节点，只能调整树中节点指针的指向。
为了让您更好地理解问题，以下面的二叉搜索树为例：
            4
        2       5
      1   3
我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。
对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。
下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。
   head --|
          V
     ||=> 1 <==> 2 <==> 3 <==> 4 <==> 5 <=||
     ||===================================||

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，
树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。
注意：本题与主站 426 题相同：
https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
注意：此题对比原题有改动。
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof
    """
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def traversal(node):
            que, p = [], node
            while que or p:
                while p:
                    que.append(p)
                    p = p.left
                p = que.pop()
                rec.append(p)
                p = p.right

        if not root:
            return None
        rec = []
        traversal(root)
        n = len(rec)
        for i in range(n):
            rec[i].left = rec[i - 1]
            if i + 1 == n:
                rec[i].right = rec[0]
            else:
                rec[i].right = rec[i + 1]
        return rec[0]


def create(nums):
    if not nums:
        return None
    root = Node(nums.pop(0))
    que = [root]
    while que:
        node = que.pop(0)
        left = nums.pop(0) if nums else None
        right = nums.pop(0) if nums else None
        node.left = Node(left) if left is not None else None
        node.right = Node(right) if right is not None else None
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
    return root


def main():
    nums = [4, 2, 5, 1, 3]
    test = Solution()
    ret = test.treeToDoublyList(create(nums))
    print(ret)


if __name__ == '__main__':
    main()
