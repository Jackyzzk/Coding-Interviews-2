class Solution(object):
    """
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
输入: [1,2,3,4,5]
输出: True
输入: [0,0,1,2,5]
输出: True
数组长度为 5 
数组的数取值为 [0, 13] .
链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
    """
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        small, large, rec = 13, 0, 0
        for i in range(5):
            if nums[i] != 0:
                if rec >> nums[i] & 1:
                    return False
                else:
                    rec |= 1 << nums[i]
                if nums[i] < small:
                    small = nums[i]
                if nums[i] > large:
                    large = nums[i]
        return large - small < 5


def main():
    nums = [1, 2, 3, 4, 5]
    # nums = [0, 0, 1, 2, 5]
    # nums = [0, 0, 2, 2, 5]  # False
    # nums = [0, 0, 8, 5, 4]
    # nums = [11, 0, 9, 0, 0]  # True
    test = Solution()
    ret = test.isStraight(nums)
    print(ret)


if __name__ == '__main__':
    main()
