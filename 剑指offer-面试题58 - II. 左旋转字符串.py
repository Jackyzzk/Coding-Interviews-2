class Solution(object):
    """
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，
该函数将返回左旋转两位得到的结果"cdefgab"。
输入: s = "abcdefg", k = 2
输出: "cdefgab"
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
1 <= k < s.length <= 10000
链接：https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof
    """
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        s = s[n:] + s[:n]
        return s


def main():
    s, k = "abcdefg", 2
    # s, k = "lrloseumgh", 6
    test = Solution()
    ret = test.reverseLeftWords(s, k)
    print(ret)


if __name__ == '__main__':
    main()
