# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，
本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，
从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。
给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.
链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
    """
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p1 = p2 = head
        count = 0
        while p1:
            if count < k:
                p1 = p1.next
                count += 1
            else:
                p1 = p1.next
                p2 = p2.next
        return p2


def create(nums):
    aux = p = ListNode(0)
    for x in nums:
        p.next = ListNode(x)
        p = p.next
    return aux.next


def main():
    nums, k = [1, 2, 3, 4, 5], 2
    test = Solution()
    ret = test.getKthFromEnd(create(nums), k)
    print(ret)


if __name__ == '__main__':
    main()
