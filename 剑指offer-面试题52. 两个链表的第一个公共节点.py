# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
输入两个链表，找出它们的第一个公共节点。

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。

如果两个链表没有交点，返回 null.在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
本题与主站 160 题相同：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
链接：https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof
    """
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 设 headA 为 1 -> 2 -> 3 -> None
        # 设 headB 为 4 -> 5 -> None
        # 两个相连可得 1 -> 2 -> 3 -> None -> 4 -> 5 -> None
        # 无论如何他们都可以在最后的 None 把循环停止下来
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1


def main():
    intersectVal, listA, listB, skipA, skipB = 8, [4, 1, 8, 4, 5], [5, 0, 1, 8, 4, 5], 2, 3  # 8
    # intersectVal, listA, listB, skipA, skipB = 2, [0, 9, 1, 2, 4], [3, 2, 4], 3, 1  # 2
    # intersectVal, listA, listB, skipA, skipB = 0, [2, 6, 4], [1, 5], 3, 2  # None

    def create():
        cut = None
        aux1 = p = ListNode(-1)
        for i, x in enumerate(listA):
            p.next = ListNode(x)
            p = p.next
            if i == skipA and x == intersectVal:
                cut = p
        aux2 = p = ListNode(-1)
        for i, x in enumerate(listB):
            if i == skipB and x == intersectVal:
                p.next = cut
                break
            p.next = ListNode(x)
            p = p.next
        return aux1.next, aux2.next

    test = Solution()
    head1, head2 = create()
    ret = test.getIntersectionNode(head1, head2)
    print(ret)


if __name__ == '__main__':
    main()
