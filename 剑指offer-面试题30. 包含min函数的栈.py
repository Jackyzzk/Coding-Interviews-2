class MinStack(object):
    """
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
各函数的调用总次数不超过 20000 次
链接：https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.que = []
        self.rec = [float('inf')]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.que.append(x)
        if x <= self.rec[-1]:
            self.rec.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.que.pop() == self.rec[-1]:
            self.rec.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.que[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.rec[-1]


def main():
    input1 = ["MinStack","push","push","push","min","pop","top","min"], [[],[-2],[0],[-3],[],[],[],[]]
    input2 = ["MinStack","push","push","push","min","pop","min"], [[],[0],[1],[0],[],[],[]]
    test, ret = MinStack(), [None]

    def run(init):
        for i, x in enumerate(init[0]):
            if x == 'push':
                test.push(init[1][i][0])
                ret.append(None)
            elif x == 'min':
                ret.append(test.min())
            elif x == 'pop':
                test.pop()
                ret.append(None)
            elif x == 'top':
                ret.append(test.top())
        print(ret)

    run(input2)  # [null,null,null,null,-3,null,0,-2]  [null,null,null,null,0,null,0]


if __name__ == '__main__':
    main()

