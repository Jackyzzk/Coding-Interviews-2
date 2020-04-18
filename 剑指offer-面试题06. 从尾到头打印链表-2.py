# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
输入：head = [1,3,2]
输出：[2,3,1]
限制：
0 <= 链表长度 <= 10000
链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
    """
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        rec = []
        while head:
            rec.append(head.val)
            head = head.next
        return rec[::-1]


def create(nums):
    aux = p = ListNode(-1)
    for x in nums:
        p.next = ListNode(x)
        p = p.next
    return aux.next


def main():
    head = [1, 3, 2]
    test = Solution()
    ret = test.reversePrint(create(head))
    print(ret)


if __name__ == '__main__':
    main()
