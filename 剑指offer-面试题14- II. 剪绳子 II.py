class Solution(object):
    """
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
输入: 2    输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
输入: 10    输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
2 <= n <= 1000
链接：https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof
    """
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        # (xy)⊙p=[(x⊙p)(y⊙p)]⊙p
        # (xy) % p = [(x % p)(y % p)] % p

        pre2, pre1, cur = 0, 0, 1
        for i in range(3, n + 1):
            pre2, pre1, cur = pre1, cur, max(pre2 * 3, pre1 * 2, cur,
                                             (i - 3) * 3, (i - 2) * 2, i - 1)
        return cur % 1000000007


def main():
    n = 120  # 953271190
    # n = 10
    test = Solution()
    ret = test.cuttingRope(n)
    print(ret)


if __name__ == '__main__':
    main()
