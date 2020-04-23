class MedianFinder(object):
    """
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
那么中位数就是所有数值排序之后中间两个数的平均值。
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5
设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
最多会对 addNum、findMedia进行 50000 次调用。
注意：本题与主站 295 题相同：https://leetcode-cn.com/problems/find-median-from-data-stream/
链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.n = 0
        self.que = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        p1, p2 = 0, self.n - 1
        while p1 < p2:
            t = (p1 + p2) >> 1
            if self.que[t] > num:
                p2 = t
            else:
                p1 = t + 1
        if self.n > 0 and self.que[p1] < num:
            self.que.insert(p1 + 1, num)
        else:
            self.que.insert(p1, num)
        self.n += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.n & 1:
            return self.que[self.n >> 1] * 1.0
        else:
            return (self.que[self.n >> 1] + self.que[(self.n >> 1) - 1]) / 2.0


def main():
    input1 = ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"], [[],[1],[2],[],[3],[]]
    input2 = ["MedianFinder","addNum","findMedian","addNum","findMedian"], [[],[2],[],[3],[]]
    test, ret = MedianFinder(), [None]

    def run(init):
        for i, x in enumerate(init[0]):
            if x == 'addNum':
                test.addNum(init[1][i][0])
                ret.append(None)
            elif x == 'findMedian':
                ret.append(test.findMedian())
        print(ret)

    run(input2)  # [null,null,null,1.50000,null,2.00000]  [null,null,2.00000,null,2.50000]


if __name__ == '__main__':
    main()
