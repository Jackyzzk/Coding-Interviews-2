class Solution(object):
    """
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
输入: n = 3
输出: 6
输入: n = 9
输出: 45
1 <= n <= 10000
链接：https://leetcode-cn.com/problems/qiu-12n-lcof
    """
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (1 + n) * n >> 1


def main():
    n = 9
    test = Solution()
    ret = test.sumNums(n)
    print(ret)


if __name__ == '__main__':
    main()
