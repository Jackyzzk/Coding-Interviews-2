class Solution(object):
    """
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，
11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。
请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
0 <= num < 2 ** 31
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
    """
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        # num = str(num)
        # n = len(num)
        # opt = [1] * (n + 1)
        # for i in range(1, n + 1):
        #     if i > 1 and '0' < num[i - 2] < '3' and '0' <= num[i - 1] < '6':
        #         opt[i] = opt[i - 1] + opt[i - 2]
        #     else:
        #         opt[i] = opt[i - 1]
        # return opt[n]

        num = str(num)
        n = len(num)
        pre, cur = 1, 1
        for i in range(1, n + 1):
            can = False
            if i > 1:
                if num[i - 2] == '1':
                    can = True
                elif num[i - 2] == '2' and '0' <= num[i - 1] < '6':
                    can = True
            if can:
                pre, cur = cur, pre + cur
            else:
                pre = cur
        return cur


def main():
    num = 12258
    # num = 18580  # 2
    # num = 18822  # 4
    test = Solution()
    ret = test.translateNum(num)
    print(ret)


if __name__ == '__main__':
    main()
