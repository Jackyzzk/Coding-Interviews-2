class Solution(object):
    """
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
输入：s = "We are happy."
输出："We%20are%20happy."
限制：
0 <= s 的长度 <= 10000
链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
    """
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        rec = s.split(' ')
        return '%20'.join(rec)


def main():
    s = "We are happy."
    test = Solution()
    ret = test.replaceSpace(s)
    print(ret)


if __name__ == '__main__':
    main()
