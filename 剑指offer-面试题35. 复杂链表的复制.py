# Definition for a Node.
class Node(object):
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    """
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next
指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。节点数目不超过 1000 。
注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-pointer/
链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
    """
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        rec, p = [], head
        seq, count = {None: None}, 0
        while p:
            seq[p] = count
            count += 1
            p = p.next
        p = head
        while p:
            rec.append([p.val, seq[p.random]])
            p = p.next

        def create(nums):
            aux = p = Node(0)
            rec = []
            for x in nums:
                p.next = Node(x[0])
                p = p.next
                rec.append(p)
            for i, x in enumerate(nums):
                if x[1] is not None:
                    rec[i].random = rec[x[1]]
            return aux.next

        return create(rec)


def create(nums):
    aux = p = Node(0)
    rec = []
    for x in nums:
        p.next = Node(x[0])
        p = p.next
        rec.append(p)
    for i, x in enumerate(nums):
        if x[1] is not None:
            rec[i].random = rec[x[1]]
    return aux.next


def main():
    nums = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    nums = [[1, 1], [2, 1]]
    nums = [[3, None], [3, 0], [3, None]]
    # nums = []
    test = Solution()
    ret = test.copyRandomList(create(nums))
    print(ret)


if __name__ == '__main__':
    main()
