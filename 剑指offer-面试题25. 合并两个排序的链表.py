# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
0 <= 链表长度 <= 1000
链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
    """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        aux = p1 = ListNode(0)
        p1.next, p2 = l1, l2
        while p1.next and p2:
            if p1.next.val < p2.val:
                p1 = p1.next
            else:
                p1.next, p2.next, p1, p2 = p2, p1.next, p2, p2.next
        if p2:
            p1.next = p2
        return aux.next


def create(nums):
    aux = p = ListNode(0)
    for x in nums:
        p.next = ListNode(x)
        p = p.next
    return aux.next


def main():
    nums1, nums2 = [1, 2, 4], [1, 3, 4]
    # nums1, nums2 = [1, 2, 4], [5, 6, 7]
    # nums1, nums2 = [5, 6, 7], [1, 3, 4]
    test = Solution()
    ret = test.mergeTwoLists(create(nums1), create(nums2))
    print(ret)


if __name__ == '__main__':
    main()
