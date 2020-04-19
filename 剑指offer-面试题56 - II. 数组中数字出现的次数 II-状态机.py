class Solution(object):
    """
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
输入：nums = [3,4,3,3]
输出：4
输入：nums = [9,1,7,9,7,9,7]
输出：1
1 <= nums.length <= 10000
1 <= nums[i] < 2^31
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # a, b = 0, 0
        # for x in nums:
        #     b = b ^ x & ~ a
        #     a = a ^ x & ~ b
        # return b
        # 用一对二进制数来表示一个三进制，其中一个代表个位，另一个代表进位
        # 个位 units，进位 carry，输入 x
        # 用这样的一个三进制，0：初始化，1：该位来了一个1，2：该位来了两个1，0：该位来了3个1恢复初始化
        #    输入x   原carry 原units   现carry 现units
        #      0        0       0         0      0
        #      0        0       1         0      1
        #      0        1       0         1      0
        #      1        0       0         0      1
        #      1        0       1         1      0
        #      1        1       0         0      0
        # 总共就有 6 种情况，根据以上情况写出逻辑表达式
        # units = 0 的情况：(x == 0 and units == 0) or (x == 1 and (units == 1 or carry == 1))
        # units = 1 的情况：(x == 0 and units == 1) or (x == 1 and units == 0 and carry == 0)
        # carry = 0 的情况：(x == 0 and carry == 0) or (x == 1 and (units == 0 or carry == 1))
        # carry = 1 的情况：(x == 0 and carry == 1) or (x == 1 and units == 1 and carry == 0)
        # 观察发现 x 与 units 互不相同， x 与 carry 也互不相同
        # 逻辑运算律之吸收律： A + ~AB = A + B
        # units = (x ^ units) & ((x & ~carry) | ~x) = (x ^ units) & ~carry
        # carry = (x ^ carry) & ((x & units) | ~x) =
        # units 和 carry 不能同时为 1
        units, carry = 0, 0
        for x in nums:
            units, carry = (x ^ units) & ~carry, (x ^ carry) & (~x | units)
        return units


def main():
    nums = [3, 4, 3, 3]
    nums = [9, 1, 7, 9, 7, 9, 7]
    test = Solution()
    ret = test.singleNumber(nums)
    print(ret)


if __name__ == '__main__':
    main()
