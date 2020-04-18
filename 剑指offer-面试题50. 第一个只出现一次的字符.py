class Solution(object):
    """
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。
s = "abaccdeff"   返回 "b"
s = ""            返回 " "
0 <= s 的长度 <= 50000
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
    """
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        rec = {}
        for x in s:
            if x not in rec:
                rec[x] = True
            else:
                rec[x] = False
        for x in s:
            if rec[x]:
                return x
        return ' '


def main():
    s = "abaccdeff"
    # s = ''  # ' '
    test = Solution()
    ret = test.firstUniqChar(s)
    print(ret)


if __name__ == '__main__':
    main()
