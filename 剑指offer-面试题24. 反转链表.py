# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
0 <= 节点个数 <= 5000
链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
    """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, cur = None, head
        while cur:
            cur.next, cur, pre = pre, cur.next, cur
        return pre


def create(nums):
    aux = p = ListNode(0)
    for x in nums:
        p.next = ListNode(x)
        p = p.next
    return aux.next


def main():
    nums = [1, 2, 3, 4, 5]
    test = Solution()
    ret = test.reverseList(create(nums))
    print(ret)


if __name__ == '__main__':
    main()
