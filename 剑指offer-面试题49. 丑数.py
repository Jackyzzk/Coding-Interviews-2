class Solution(object):
    """
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
1 是丑数。
n 不超过1690。
注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/
链接：https://leetcode-cn.com/problems/chou-shu-lcof
    """
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 由于丑数只包含因子 2, 3, 5 因此较大的丑数一定能够通过某较小丑数 * 某因子得到
        # 而不是由当前因子构成的上一个丑数 * 当前因子构成
        nums, count = [1], 1
        pre2, pre3, pre5 = 0, 0, 0
        while count < n:
            cur2 = nums[pre2] * 2
            cur3 = nums[pre3] * 3
            cur5 = nums[pre5] * 5
            cur = min(cur2, cur3, cur5)
            if cur == cur2:
                pre2 += 1
            if cur == cur3:
                pre3 += 1
            if cur == cur5:
                pre5 += 1
            nums.append(cur)
            count += 1
        return nums[-1]


def main():
    n = 10
    test = Solution()
    ret = test.nthUglyNumber(n)
    print(ret)


if __name__ == '__main__':
    main()
