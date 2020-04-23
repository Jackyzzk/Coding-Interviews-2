class Solution(object):
    """
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
1 <= s 的长度 <= 8
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
    """
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def swap(start, t):
            s[start:] = [s[t]] + s[start:t] + s[t + 1:]

        def back(start, t):
            s[start:] = s[start + 1:t + 1] + [s[start]] + s[t + 1:]

        def dfs(start=0):
            if start == n:
                ret.append(''.join(s))
            for i in range(start, n):
                if i > start and s[i] == s[i - 1]:
                    continue
                swap(start, i)  # 交换的时候不能破坏排序，否则影响去重判断 s[i] == s[i - 1]
                dfs(start + 1)
                back(start, i)

        ret, s = [], list(s)
        n = len(s)
        s.sort()
        dfs()
        return ret


def main():
    s = 'abc'
    # s = ''
    # s = "baa"  # ["aba","aab","baa"]
    # s = 'f'  # ["f"]
    # s = "suvyls"
    # s = 'ababa'
    test = Solution()
    ret = test.permutation(s)
    print(ret)


if __name__ == '__main__':
    main()
