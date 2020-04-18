class Solution(object):
    """
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
输入：n = 2   输出：1
输入：n = 5   输出：5
0 <= n <= 100
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
    """
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        opt = [0] * (n + 2)  # 加 2 可以保证 n 为 0 的情况不用特殊处理
        opt[1] = 1
        for i in range(2, n + 1):
            opt[i] = opt[i - 1] + opt[i - 2]
        return opt[n] % 1000000007


def main():
    n = 1
    n = 45  # 134903163
    test = Solution()
    ret = test.fib(n)
    print(ret)


if __name__ == '__main__':
    main()
