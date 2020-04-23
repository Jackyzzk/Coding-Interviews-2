class Solution(object):
    """
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。
输入: [7,5,6,4]
输出: 5
0 <= 数组长度 <= 50000
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
    """
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def partition(arr):
            if len(arr) < 2:
                return arr
            mid = len(arr) >> 1
            left = partition(arr[:mid])
            right = partition(arr[mid:])
            return merge(left, right)

        def merge(arr1, arr2):
            n1, n2 = len(arr1), len(arr2)
            arr = [0] * (n1 + n2)
            i = j = k = 0
            while i < n1 and j < n2:
                if arr1[i] <= arr2[j]:
                    arr[k] = arr1[i]
                    i += 1
                else:
                    arr[k] = arr2[j]
                    self.count += n1 - i
                    j += 1
                k += 1
            while i < n1:
                arr[k] = arr1[i]
                i += 1
                k += 1
            while j < n2:
                arr[k] = arr2[j]
                j += 1
                k += 1
            return arr

        self.count = 0
        partition(nums)
        return self.count


def main():
    nums = [7, 5, 6, 4, 1]
    nums = []
    test = Solution()
    ret = test.reversePairs(nums)
    print(ret)


if __name__ == '__main__':
    main()
