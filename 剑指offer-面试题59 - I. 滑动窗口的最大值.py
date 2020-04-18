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
        def push(x):
            que.append(x)
            if x > self.rec[0]:
                self.rec = [x]
            else:
                while self.rec[-1] < x:
                    self.rec.pop()
                self.rec.append(x)

        def out():
            if que.pop(0) == self.rec[0]:
                self.rec.pop(0)

        if k == 1:
            return nums
        que, self.rec, ret = [], [float('-inf')], []
        for i in range(k - 1):
            push(nums[i])

        for i in range(k - 1, len(nums)):
            push(nums[i])
            ret.append(self.rec[0])
            out()
        return ret


def main():
    nums, k = [1, 3, -1, -3, 5, 3, 6, 7], 3
    nums, k = [5, 4, 3, 2, 1], 2
    nums, k = [1, -1], 1
    # nums, k = [1, 3, 1, 2, 0, 5], 3  # [3,3,2,5]
    test = Solution()
    ret = test.maxSlidingWindow(nums, k)
    print(ret)


if __name__ == '__main__':
    main()
