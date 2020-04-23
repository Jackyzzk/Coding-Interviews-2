class Solution(object):
    """
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
s.length <= 40000
注意：本题与主站 3 题相同：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
链接：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        rec, ret = {}, 0
        pre, i = 0, -1
        for i, x in enumerate(s):
            if x not in rec:
                rec[x] = i  # 记录最后出现的下标
            else:
                ret = max(ret, i - pre)
                pre = max(pre, rec[x] + 1)
                rec[x] = i
        ret = max(ret, i - pre + 1)
        return ret


def main():
    s = "abcabcbb"
    # s = "bbbbb"
    # s = "pwwkew"
    s = "dvdf"  # 3
    # s = ''
    s = "cdd"  # 2
    # s = "abba"  # 2
    test = Solution()
    ret = test.lengthOfLongestSubstring(s)
    print(ret)


if __name__ == '__main__':
    main()
