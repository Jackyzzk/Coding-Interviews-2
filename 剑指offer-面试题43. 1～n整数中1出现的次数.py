class Solution(object):
    """
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。
输入：n = 12
输出：5
输入：n = 13
输出：6
1 <= n < 2^31
注意：本题与主站 233 题相同：https://leetcode-cn.com/problems/number-of-digit-one/
链接：https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof
    """
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        def convert(s):
            if s == '':
                return 0
            else:
                return int(s)

        def partition(i):
            if nums[i] == '1':
                if nums[:i]:
                    self.count += convert(nums[:i]) * 10 ** len(nums[i + 1:])  # 借位
                self.count += convert(nums[i + 1:]) + 1  # 不借，左边的值就只剩唯一的了
            elif nums[i] == '0':
                self.count += convert(nums[:i]) * 10 ** len(nums[i + 1:])
            else:
                self.count += (convert(nums[:i]) + 1) * 10 ** len(nums[i + 1:])

        self.count = 0
        nums = str(n)
        n = len(nums)
        for t in range(n):
            partition(t)
        return self.count


def main():
    n = 12
    n = 118  # 33
    test = Solution()
    ret = test.countDigitOne(n)
    print(ret)


if __name__ == '__main__':
    main()
