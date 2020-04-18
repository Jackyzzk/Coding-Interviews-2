class Solution(object):
    """
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/
链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
    """
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k < 2:
            return nums
        rec, ret = [float('-inf')], []
        for i in range(k - 1):
            x = nums[i]
            if x > rec[0]:
                rec = [x]
            else:
                while rec[-1] < x:  # 维护一个单调栈
                    rec.pop()
                rec.append(x)

        for i in range(k - 1, len(nums)):
            x = nums[i]
            if nums[i - k] == rec[0]:
                rec.pop(0)
            if x > rec[0]:
                rec = [x]
            else:
                while rec[-1] < x:
                    rec.pop()
                rec.append(x)
            ret.append(rec[0])
        return ret


def main():
    nums, k = [1, 3, -1, -3, 5, 3, 6, 7], 3
    # nums, k = [5, 4, 3, 2, 1], 2
    # nums, k = [1, -1], 1
    # nums, k = [1, 3, 1, 2, 0, 5], 3  # [3,3,2,5]
    test = Solution()
    ret = test.maxSlidingWindow(nums, k)
    print(ret)


if __name__ == '__main__':
    main()
