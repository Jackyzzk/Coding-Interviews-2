# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
返回删除后的链表的头节点。
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
题目保证链表中节点的值互不相同
若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点
链接：https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof
    """
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        aux = p = ListNode(0)
        p.next = head
        while p.next.val != val:
            p = p.next
        p.next = p.next.next
        return aux.next


def create(nums):
    aux = p = ListNode(0)
    for x in nums:
        p.next = ListNode(x)
        p = p.next
    return aux.next


def main():
    nums, val = [4, 5, 1, 9], 5
    nums, val = [4, 5, 1, 9], 9
    test = Solution()
    ret = test.deleteNode(create(nums), val)
    print(ret)


if __name__ == '__main__':
    main()
