class Solution(object):
    """
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。
求出这个圆圈里剩下的最后一个数字。例如，0、1、2、3、4这5个数字组成一个圆圈，
从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
输入: n = 5, m = 3
输出: 3
输入: n = 10, m = 17
输出: 2
1 <= n <= 10^5
1 <= m <= 10^6
链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof
约瑟夫问题，这个问题描述是
N个人围成一圈，第一个人从1开始报数，报M的将被杀掉，下一个人接着从1开始报。如此反复，最后剩下一个，求最后的胜利者。
最重要的点：
只关心最终活着那个人的序号变化
我们定义f(n,m)表示最后剩下那个人的索引号
f(n,m) = [f(n-1, m) + m] % n
很显然最后一步 f(1,m) = 0
https://blog.csdn.net/u011500062/article/details/72855826
    """
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # 已知 opt[n] - m = opt[n - 1] 不考虑越界的时候
        opt = 0
        for i in range(2, n + 1):  # i 代表队列长度
            opt = (opt + m) % i
        return opt


def main():
    n, m = 5, 3
    n, m = 10, 17
    test = Solution()
    ret = test.lastRemaining(n, m)
    print(ret)


if __name__ == '__main__':
    main()
