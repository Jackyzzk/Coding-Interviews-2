"""
区分堆(heap)与栈(stack)：
    堆与二叉树有关，像一堆金字塔型泥沙；而栈像一个直立垃圾桶，一列下来。
堆(heap):
    又被为优先队列(priority queue)。尽管名为优先队列，但堆并不是队列。
性质：
    堆的实现通过构造二叉堆（binary heap），实为二叉树的一种。
    堆总是一棵完全树。即除了最底层，其他层的节点都被元素填满，且最底层尽可能地从左到右填入。
复杂度分析：
    insert: O(logN)
    del Max: O(logN)
    Max: O(1)
python内置方法创建堆：
    1.初始化为[]的空列表
    2.将新的值推入堆中，heapq.heappush(堆，项目)
    a.初始化普通的列表[]并存入元素
    b.通过函数heapify()将列表转换为堆，heapq.heapify(原列表)
弹出堆顶元素：
    heapq.heappop（堆）
    弹出并返回堆中的最小项，保持堆不变。如果堆是空的，则引发IndexError。
"""
import heapq


# 1
heap = []
test = [3, 1, 5, 7, 9, 2, 4, 6, 8, 10]
for i in test:
    heapq.heappush(heap, i)
print(heap)
print(heapq.heappop(heap))

# 2
heapq.heapify(test)
print(test)
print(heapq.nlargest(3, test))
# print(heapq.heappop(test))
# print(test)
