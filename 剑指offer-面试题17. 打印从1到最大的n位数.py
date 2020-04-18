class Solution(object):
    """
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，
则打印出 1、2、3 一直到最大的 3 位数 999。
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
用返回一个整数列表来代替打印, n 为正整数
链接：https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof
    """
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # return [i for i in range(1, 10 ** n)]
        return range(1, 10 ** n)


def main():
    n = 1
    test = Solution()
    ret = test.printNumbers(n)
    print(ret)


if __name__ == '__main__':
    main()
