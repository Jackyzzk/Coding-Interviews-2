class Solution(object):
    """
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
输入: s, p = "aa", "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
输入: s, p = "aa", "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
输入: s, p = "ab", ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
输入: s, p = "aab", "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
输入: s, p = "mississippi", "mis*is*p*."
输出: false
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof
    """
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n1, n2 = len(s), len(p)
        opt = [[False] * (n2 + 1) for i in range(n1 + 1)]
        opt[0][0] = True
        for j in range(2, n2 + 1):  # 初始化，如果不从2开始，p[j - 1] = p[-1] 有可能取到 p 最后的 * 号
            if p[j - 1] == '*':
                opt[0][j] = opt[0][j - 2]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    opt[i][j] = opt[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        opt[i][j] = opt[i - 1][j] or opt[i][j - 2]
                    else:  # 如果 p 的前一位与 s 不相等，不能把 s 的这一位去掉
                        opt[i][j] = opt[i][j - 2]
        return opt[n1][n2]


def main():
    s, p = "aa", "a*"
    s, p = "aa", "a"
    s, p = "ab", ".*"  # True
    # a.*b，它将会匹度配最长的以a开始，以b结束的字符串。如果用它来搜索aabab的话，它会匹配整个字符串aabab。这被称为贪婪匹配。
    s, p = "aab", "c*a*b"
    s, p = "mississippi", "mis*is*p*."
    s, p = "ab", ".*c"  # False
    s, p = "aaa", "a*a"  # True
    s, p = "aaa", "ab*a*c*a"  # True
    s, p = "a", "ab*a"
    test = Solution()
    ret = test.isMatch(s, p)
    print(s, p, ret)


if __name__ == '__main__':
    main()
