class Solution(object):
    """
实现函数double Power(double base, int exponent)，求base的exponent次方。
不得使用库函数，同时不需要考虑大数问题。
输入: 2.00000, 10     输出: 1024.00000
输入: 2.10000, 3      输出: 9.26100
输入: 2.00000, -2     输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof
    """
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x, n = 1 / x, -n
        ret = 1
        while n:
            if n & 1:
                ret *= x  # 先让 x 两两相乘，缩小循环次数，n 为奇数时会剩下一个 x
            x *= x
            n >>= 1
        return ret


def main():
    # x, n = 2.00000, 10
    x, n = 0.00001, 2147483647
    test = Solution()
    ret = test.myPow(x, n)
    print(ret)


if __name__ == '__main__':
    main()
