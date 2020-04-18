class Solution(object):
    """
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
输入: 2   输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
输入: 10   输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
2 <= n <= 58
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
链接：https://leetcode-cn.com/problems/integer-break/
    """
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 尽可能的多分出 3 可以使得乘积最大
        # opt = [0] * (n + 1)
        # opt[2] = 1
        # for i in range(3, n + 1):
        #     opt[i] = max(opt[i - 3] * 3, opt[i - 2] * 2, opt[i - 1],
        #                  (i - 3) * 3, (i - 2) * 2, i - 1)
        # return opt[n]
        pre2, pre1, cur = 0, 0, 1
        for i in range(3, n + 1):
            pre2, pre1, cur = pre1, cur, max(pre2 * 3, pre1 * 2, cur,
                                             (i - 3) * 3, (i - 2) * 2, i - 1)
        return cur


def main():
    n = 10
    test = Solution()
    ret = test.cuttingRope(n)
    print(ret)


if __name__ == '__main__':
    main()
