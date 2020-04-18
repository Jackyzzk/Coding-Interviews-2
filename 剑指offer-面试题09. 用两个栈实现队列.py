class CQueue(object):
    """
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
    """
    def __init__(self):
        self.que1, self.que2 = [], []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.que1.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        # 注意题目要求用两个栈而不是一个
        if self.que2:
            return self.que2.pop()
        if not self.que1:
            return -1
        while self.que1:
            self.que2.append(self.que1.pop())
        return self.que2.pop()


def main():
    input1 = ["CQueue","appendTail","deleteHead","deleteHead"], [[],[3],[],[]]
    input2 = ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"], [[],[],[5],[2],[],[]]
    test, ret = CQueue(), [None]

    def run(init):
        for i, x in enumerate(init[0]):
            if x == 'appendTail':
                test.appendTail(init[1][i][0])
                ret.append(None)
            elif x == 'deleteHead':
                ret.append(test.deleteHead())
        print(ret)

    run(input1)  # [null,null,3,-1], [null,-1,null,null,5,2]


if __name__ == '__main__':
    main()
