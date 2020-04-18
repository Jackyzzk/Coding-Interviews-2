class Solution(object):
    """
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
1 <= nums.length <= 50000
1 <= nums[i] <= 10000
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
    """
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n, p2 = len(nums), -1
        for p1 in range(n):
            if nums[p1] & 1:
                p2 += 1
                nums[p1], nums[p2] = nums[p2], nums[p1]
        return nums


def main():
    nums = [1, 2, 3, 4]
    test = Solution()
    ret = test.exchange(nums)
    print(ret)


if __name__ == '__main__':
    main()
