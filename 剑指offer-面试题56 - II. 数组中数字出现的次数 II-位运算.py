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
        a, b = 0, 0
        for x in nums:
            b = b ^ x & ~ a
            a = a ^ x & ~ b

        return b


def main():
    nums = [3, 4, 3, 3]
    # nums = [9, 1, 7, 9, 7, 9, 7]
    test = Solution()
    ret = test.singleNumber(nums)
    print(ret)


if __name__ == '__main__':
    main()
