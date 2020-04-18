class Solution(object):
    """
写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。
首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，
作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
在任何情况下，若函数不能进行有效的转换时，请返回 0。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，
请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
输入: "42"
输出: 42
输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。因此无法执行有效的转换。
输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 因此返回 INT_MIN (−231) 。
注意：本题与主站 8 题相同：https://leetcode-cn.com/problems/string-to-integer-atoi/
链接：https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof
    """
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        def digit(s):
            if ord(s) in range(48, 58):
                return True
            return False

        def sign(s):
            if s == '-' or s == '+':
                return True
            return False

        def index(t):
            while t < n and str[t] == ' ':
                t += 1
            return t

        def convert(s):
            ret = 0
            for x in s:
                ret = ret * 10 + ord(x) - 48
            return ret

        if not str:
            return 0
        n = len(str)
        i = index(0)
        if i == n or not (digit(str[i]) or sign(str[i])):
            return 0
        mark = 1
        if sign(str[i]):
            if str[i] == '-':
                mark = -1
            i += 1

        j = i
        while j < n and digit(str[j]):
            j += 1
        ret = convert(str[i:j])
        if mark > 0:
            if ret > (1 << 31) - 1:
                return (1 << 31) - 1
            else:
                return ret
        else:
            if ret > 1 << 31:
                return -(1 << 31)
            else:
                return -ret


def main():
    s = '42'
    s = "   -42"
    s = "4193 with words"
    s = "words and 987"
    s = "-91283472332"
    s = "+1"
    s = " "
    s = "2147483648"  # 2147483647
    test = Solution()
    ret = test.strToInt(s)
    print(ret)


if __name__ == '__main__':
    main()
