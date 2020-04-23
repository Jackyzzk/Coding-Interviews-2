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
        def dfs():
            for i in range(n):
                if i > 0 and s[i] == s[i - 1] and not visit[i - 1]:
                    continue
                if not visit[i]:
                    rec.append(s[i])
                    visit[i] = 1
                    dfs()
                    rec.pop()
                    visit[i] = 0
            if len(rec) == n:
                ret.append(''.join(rec))

        s, n = list(s), len(s)
        s.sort()
        visit = [0] * n
        ret, rec = [], []
        dfs()
        return ret


def main():
    s = 'abc'
    s = "aab"  # ["aba","aab","baa"]
    # s = 'f'  # ["f"]
    test = Solution()
    ret = test.permutation(s)
    print(ret)


if __name__ == '__main__':
    main()
