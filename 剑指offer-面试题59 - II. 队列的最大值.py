class MaxQueue(object):
    """
请定义一个队列并实现函数 max_value 得到队列里的最大值，
要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1
输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
    """
    def __init__(self):
        self.que = []
        self.rec = [float('-inf')]

    def max_value(self):
        """
        :rtype: int
        """
        return self.rec[0] if self.que else -1

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.que.append(value)
        if value > self.rec[0]:
            self.rec = [value]
        else:
            while value > self.rec[-1]:  # 维护单调栈
                self.rec.pop()
            self.rec.append(value)

    def pop_front(self):
        """
        :rtype: int
        """
        if self.que:
            if self.que[0] == self.rec[0]:
                self.rec.pop(0)
                if not self.rec:
                    self.rec.append(float('-inf'))
            return self.que.pop(0)
        else:
            return -1


def main():
    input1 = ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"], [[],[1],[2],[],[],[]]
    input2 = ["MaxQueue","pop_front","max_value"], [[],[],[]]
    input3 = ["MaxQueue","pop_front","pop_front","pop_front","pop_front","pop_front",
              "push_back","max_value","push_back","max_value"], [[],[],[],[],[],[],[15],[],[9],[]]
    input4 = ["MaxQueue","max_value","pop_front","max_value","push_back","max_value","pop_front","max_value",
              "pop_front","push_back","pop_front","pop_front","pop_front","push_back","pop_front","max_value",
              "pop_front","max_value","push_back","push_back","max_value","push_back","max_value","max_value",
              "max_value","push_back","pop_front","max_value","push_back","max_value","max_value","max_value",
              "pop_front","push_back","push_back","push_back","push_back","pop_front","pop_front","max_value",
              "pop_front","pop_front","max_value","push_back","push_back","pop_front","push_back","push_back",
              "push_back","push_back","pop_front","max_value","push_back","max_value","max_value","pop_front",
              "max_value","max_value","max_value","push_back","pop_front","push_back","pop_front","max_value",
              "max_value","max_value","push_back","pop_front","push_back","push_back","push_back","pop_front",
              "max_value","pop_front","max_value","max_value","max_value","pop_front","push_back","pop_front",
              "push_back","push_back","pop_front","push_back","pop_front","push_back","pop_front","pop_front",
              "push_back","pop_front","pop_front","pop_front","push_back","push_back","max_value","push_back",
              "pop_front","push_back","push_back","pop_front"], \
             [[],[],[],[],[46],[],[],[],[],[868],[],[],[],[525],[],[],[],[],[123],[646],[],[229],[],[],[],[871],
              [],[],[285],[],[],[],[],[45],[140],[837],[545],[],[],[],[],[],[],[561],[237],[],[633],[98],[806],
              [717],[],[],[186],[],[],[],[],[],[],[268],[],[29],[],[],[],[],[866],[],[239],[3],[850],[],[],[],[],
              [],[],[],[310],[],[674],[770],[],[525],[],[425],[],[],[720],[],[],[],[373],[411],[],[831],[],[765],[701],[]]
    input5 = ["MaxQueue","max_value","pop_front","max_value","push_back","max_value","pop_front","max_value","pop_front",
              "push_back","pop_front","pop_front","pop_front","push_back","pop_front","max_value","pop_front","max_value",
              "push_back","push_back","max_value","push_back","max_value","max_value","max_value","push_back","pop_front",
              "max_value","push_back","max_value","max_value","max_value","pop_front","push_back","push_back","push_back",
              "push_back","pop_front","pop_front","max_value","pop_front","pop_front","max_value","push_back","push_back",
              "pop_front","push_back","push_back","push_back","push_back","pop_front","max_value","push_back","max_value",
              "max_value","pop_front","max_value","max_value","max_value","push_back","pop_front","push_back","pop_front",
              "max_value","max_value","max_value","push_back","pop_front","push_back","push_back","push_back","pop_front",
              "max_value","pop_front","max_value","max_value","max_value","pop_front","push_back","pop_front","push_back",
              "push_back","pop_front","push_back","pop_front","push_back","pop_front","pop_front","push_back","pop_front",
              "pop_front","pop_front","push_back","push_back","max_value","push_back","pop_front","push_back","push_back",
              "pop_front"], \
             [[],[],[],[],[46],[],[],[],[],[868],[],[],[],[525],[],[],[],[],[123],[646],[],[229],[],[],[],[871],[],[],[285],
              [],[],[],[],[45],[140],[837],[545],[],[],[],[],[],[],[561],[237],[],[633],[98],[806],[717],[],[],[186],[],[],
              [],[],[],[],[268],[],[29],[],[],[],[],[866],[],[239],[3],[850],[],[],[],[],[],[],[],[310],[],[674],[770],[],
              [525],[],[425],[],[],[720],[],[],[],[373],[411],[],[831],[],[765],[701],[]]
    test, ret = MaxQueue(), [None]

    def run(init):
        for i, x in enumerate(init[0]):
            if x == 'push_back':
                test.push_back(init[1][i][0])
                ret.append(None)
            elif x == 'max_value':
                ret.append(test.max_value())
            elif x == 'pop_front':
                ret.append(test.pop_front())
        print(ret)

    run(input5)  # [null,null,null,2,1,2], [null,-1,-1], [null,-1,-1,-1,-1,-1,null,15,null,15]


if __name__ == '__main__':
    main()

# [null,-1,-1,-1,null,46,46,-1,-1,null,868,-1,-1,null,525,-1,-1,-1,null,null,646,null,646,646,646,null,123,871,
# null,871,871,871,646,null,null,null,null,229,871,837,285,45,837,null,null,140,null,null,null,null,837,806,null,
# 806,806,545,806,806,806,null,561,null,237,806,806,806,null,633,null,null,null,98,866,806,866,866,866,717,null,
# 186,null,null,268,null,29,null,866,239,null,3,850,310,null,null,770,null,674,null,null,770]