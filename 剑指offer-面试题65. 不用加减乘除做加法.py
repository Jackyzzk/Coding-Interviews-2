class Solution(object):
    """
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
输入: a = 1, b = 1
输出: 2
a, b 均可能是负数或 0
结果不会溢出 32 位整数
链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof
    """
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 异或是不计进位的加法
        plus, carry = a & 0xffffffff, b & 0xffffffff  # 与上掩码可以找到负数的那个相加越界为0的数
        while carry:
            plus, carry = plus ^ carry, (plus & carry) << 1 & 0xffffffff
        return plus if plus < 0x80000000 else ~(plus ^ 0xffffffff)


def main():
    a, b = -1, -1
    test = Solution()
    ret = test.add(a, b)
    print(ret)


if __name__ == '__main__':
    main()
