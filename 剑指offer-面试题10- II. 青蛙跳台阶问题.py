class Solution(object):
    """
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
输入：n = 2   输出：2
输入：n = 7   输出：21
0 <= n <= 100
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
    """
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        # opt = [1] * (n + 1)
        # for i in range(2, n + 1):
        #     opt[i] = opt[i - 1] + opt[i - 2]
        # return opt[n] % 1000000007
        pre, cur = 1, 1
        for i in range(2, n + 1):
            pre, cur = cur, (pre + cur) % 1000000007
        return cur


def main():
    n = 7
    test = Solution()
    ret = test.numWays(n)
    print(ret)


if __name__ == '__main__':
    main()
