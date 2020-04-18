class Solution(object):
    """
输入一个整型数组，数组里有正数也有负数。
数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # opt = [float('-inf')] * (n + 1)
        # for i, x in enumerate(nums):
        #     opt[i + 1] = max(opt[i] + x, x)
        # return max(opt)

        pre = rec = float('-inf')
        for x in nums:
            pre = max(pre + x, x)
            rec = max(pre, rec)
        return rec


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [-1]
    test = Solution()
    ret = test.maxSubArray(nums)
    print(ret)


if __name__ == '__main__':
    main()
