class Solution(object):
    """
数字以0123456789101112131415…的格式序列化到一个字符序列中。
在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
请写一个函数，求任意第n位对应的数字。
输入：n = 3
输出：3
输入：n = 11
输出：0
0 <= n < 2^31
注意：本题与主站 400 题相同：https://leetcode-cn.com/problems/nth-digit/
链接：https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof
    """
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        a, b = 9, 1
        while n > a * b:
            n -= a * b
            a *= 10
            b += 1
        count, rest = n // b, n % b
        real = 10 ** (b - 1) + count if rest else 10 ** (b - 1) + count - 1
        if rest:
            while rest <= b:
                ret = real % 10
                real //= 10
                rest += 1
        else:
            ret = real % 10
        return ret


def main():
    n = 19
    n = 999999999  # 9
    test = Solution()
    ret = test.findNthDigit(n)
    print(ret)


if __name__ == '__main__':
    main()
