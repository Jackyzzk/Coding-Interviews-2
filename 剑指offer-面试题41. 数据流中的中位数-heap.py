import heapq


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
        # 构造最大堆和最小堆，让数组中的大数放在最小堆，小的数放在最大堆，这样每个堆的顶点都接近中位数
        self.n1, self.n2 = 0, 0
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # heapq.heappush(self.min_heap, num)
        # x = heapq.heappop(self.min_heap)
        # heapq.heappush(self.max_heap, -x)
        # self.n2 += 1
        # if self.n1 < self.n2:
        #     x = -heapq.heappop(self.max_heap)
        #     self.n2 -= 1
        #     heapq.heappush(self.min_heap, x)
        #     self.n1 += 1

        heapq.heappush(self.max_heap, -num)
        x = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, x)
        self.n1 += 1
        if self.n2 < self.n1:
            x = heapq.heappop(self.min_heap)
            self.n1 -= 1
            heapq.heappush(self.max_heap, -x)
            self.n2 += 1

    def findMedian(self):
        """
        :rtype: float
        """
        n = self.n1 + self.n2
        # if n & 1:
        #     return self.min_heap[0] * 1.0
        # else:
        #     return (self.min_heap[0] - self.max_heap[0]) / 2.0

        if n & 1:
            return self.max_heap[0] * -1.0
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2.0


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
