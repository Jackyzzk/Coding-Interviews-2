import random


class Solution(object):
    """
输入整数数组 arr ，找出其中最小的 k 个数。例如，
输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
输入：arr = [0,1,2,1], k = 1
输出：[0]
限制：
0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
    """
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        def partition(left, right):
            if left >= right:
                return
            mid = random.randint(left, right)
            arr[left], arr[mid] = arr[mid], arr[left]
            j = left
            for i in range(left + 1, right + 1):
                if arr[i] < arr[left]:
                    j += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[left], arr[j] = arr[j], arr[left]
            if j >= k - 1:
                partition(left, j - 1)
            else:
                partition(left, j - 1)
                partition(j + 1, right)

        partition(0, len(arr) - 1)
        return arr[:k]


def main():
    arr, k = [0, 1, 2, 1], 1
    # arr, k = [3, 2, 1], 2
    # arr, k = [0, 1, 2, 1], 1
    # arr, k = [0,0,0,1,2,2,3,7,6,1], 3
    test = Solution()
    ret = test.getLeastNumbers(arr, k)
    print(ret)


if __name__ == '__main__':
    main()
