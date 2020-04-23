import re


class Solution(object):
    """
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"及"-1E-16"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof
    """
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        match = re.match(r'^[+-]?(\d*)\.?(\d*)([Ee][+-]?\d+)?$', s)
        if match:
            if match.group(1) or match.group(2):
                return True
        return False


def main():
    s = '-1E-16'
    # s = '+100'
    # s = '3.1416'
    # s = "12e+5.4"
    # s = "1a3.14"
    # s = '0'
    # s = '1 '
    # s = '.1'  # True
    # s = '.'
    # s = "3."  # True
    # s = "6+1"  # False
    test = Solution()
    ret = test.isNumber(s)
    print(ret)


if __name__ == '__main__':
    main()
