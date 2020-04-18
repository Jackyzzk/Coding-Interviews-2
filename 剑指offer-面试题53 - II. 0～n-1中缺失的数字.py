class Solution(object):
    """
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
输入: [0,1,3]
输出: 2
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
1 <= 数组长度 <= 10000
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
    """
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1, p2 = 0, len(nums) - 1
        while p1 < p2:
            t = (p1 + p2) >> 1
            if nums[t] == t:
                p1 = t + 1
            else:
                p2 = t
        if p1 == nums[p1]:
            return p1 + 1
        return p1


def main():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 9]
    nums = [0, 1, 3]
    nums = [0]
    # nums = [1]
    test = Solution()
    ret = test.missingNumber(nums)
    print(ret)


if __name__ == '__main__':
    main()
