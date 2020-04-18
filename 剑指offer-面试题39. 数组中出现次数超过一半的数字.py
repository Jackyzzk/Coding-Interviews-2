class Solution(object):
    """
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
1 <= 数组长度 <= 50000
注意：本题与主站 169 题相同：https://leetcode-cn.com/problems/majority-element/
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
    """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 摩尔投票法
        t, count = nums[0], 0
        for x in nums:
            if count != 0:
                if x == t:
                    count += 1
                else:
                    count -= 1
            else:
                t = x
                count = 1
        return t


def main():
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    test = Solution()
    ret = test.majorityElement(nums)
    print(ret)


if __name__ == '__main__':
    main()
