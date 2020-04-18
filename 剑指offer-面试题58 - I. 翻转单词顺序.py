class Solution(object):
    """
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，
则输出"student. a am I"。

输入: "the sky is blue"
输出: "blue is sky the"
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
注意：本题与主站 151 题相同：https://leetcode-cn.com/problems/reverse-words-in-a-string/
注意：此题对比原题有改动
链接：https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof
    """
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        rec, pre = [], -1
        for i, x in enumerate(s):
            if x == ' ':
                if s[pre + 1] != ' ':
                    rec.append(s[pre + 1:i])
                pre = i
        if s[-1] != ' ':
            rec.append(s[pre + 1:])
        s = ' '.join(rec[::-1])
        return s


def main():
    s = "I am a student. "
    s = "the sky is blue"
    s = "  hello world!  "
    s = "a good   example"
    s = ''
    test = Solution()
    ret = test.reverseWords(s)
    print(ret)


if __name__ == '__main__':
    main()
