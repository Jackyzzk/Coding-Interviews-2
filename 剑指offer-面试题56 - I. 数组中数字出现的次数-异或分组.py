class Solution(object):
    """
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
2 <= nums <= 10000
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
    """
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        partition = 0
        for x in nums:
            partition ^= x
        # partition &= -partition
        partition &= ~partition + 1  # 取到最后的 1 连同它的位
        a, b = 0, 0
        for x in nums:
            if x & partition:
                a ^= x
            else:
                b ^= x
        return [a, b]


def main():
    nums = [1, 2, 10, 4, 1, 4, 3, 3]
    test = Solution()
    ret = test.singleNumbers(nums)
    print(ret)


if __name__ == '__main__':
    main()
