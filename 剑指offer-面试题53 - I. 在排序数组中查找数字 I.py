class Solution(object):
    """
统计一个数字在排序数组中出现的次数。
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
0 <= 数组长度 <= 50000
注意：本题与主站 34 题相同（仅返回值不同）：
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
    """
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        p1, p2 = 0, len(nums) - 1
        while p1 < p2 - 1:
            t = (p1 + p2) >> 1
            if nums[t] < target:
                p1 = t
            elif nums[t] > target:
                p2 = t
            else:
                p1 = p2 = t
                break
        if not nums:
            return 0
        if nums[p1] != target and nums[p2] != target:
            return 0
        while p1 > -1 and nums[p1] == target:
            p1 -= 1
        while p2 < len(nums) and nums[p2] == target:
            p2 += 1
        return p2 - p1 - 1


def main():
    nums, target = [5, 7, 7, 8, 8, 10], 8
    # nums, target = [1, 4], 4  # 1
    nums, target = [], 0
    test = Solution()
    ret = test.search(nums, target)
    print(ret)


if __name__ == '__main__':
    main()
