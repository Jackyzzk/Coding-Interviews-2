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
    """
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        nums = [i for i in range(n)]
        pre, count = 0, n - 1
        for i in range(count):
            nums.pop((pre + m - 1) % n)
            pre = (pre + m - 1) % n
            n -= 1
        return nums[0]


def main():
    n, m = 5, 3
    n, m = 10, 17
    test = Solution()
    ret = test.lastRemaining(n, m)
    print(ret)


if __name__ == '__main__':
    main()
