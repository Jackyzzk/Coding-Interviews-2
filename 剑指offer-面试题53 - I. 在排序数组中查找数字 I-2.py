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
        def search_left(p1, p2):
            while p1 < p2:
                t = (p1 + p2) >> 1
                if nums[t] < target:
                    p1 = t + 1
                else:
                    p2 = t
            return p2 if nums[p2] == target else -1  # 搜索区间从右往左夹，区间右边界成了关键

        def search_right(p1, p2):
            while p1 < p2:
                t = (p1 + p2 + 1) >> 1
                if nums[t] > target:
                    p2 = t - 1
                else:
                    p1 = t
            return p1 if nums[p1] == target else -1 # 搜索区间从左往右夹， 区间左边界成了关键

        if not nums or target > nums[-1] or target < nums[0]:
            return 0
        p1, p2 = 0, len(nums) - 1
        left = search_left(p1, p2)
        if left != -1:
            return search_right(p1, p2) - left + 1
        else:
            return 0


def main():
    nums, target = [5, 7, 7, 8, 8, 10], 8
    # nums, target = [1, 4], 4  # 1
    # nums, target = [], 0
    nums, target = [5, 7, 7, 8, 8, 10], 6
    test = Solution()
    ret = test.search(nums, target)
    print(ret)


if __name__ == '__main__':
    main()
