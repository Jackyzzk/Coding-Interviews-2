class Solution(object):
    """
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  
输入：[3,4,5,1,2]   输出：1
输入：[2,2,2,0,1]   输出：0
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
    """
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        p1, p2 = 0, len(numbers) - 1
        while p1 < p2:
            t = (p1 + p2) >> 1
            if numbers[t] < numbers[p2]:
                p2 = t
            elif numbers[t] > numbers[p2]:  # 比较标准统一选取右端点
                p1 = t + 1
            else:
                p2 -= 1
        return numbers[p2]


def main():
    nums = [3, 4, 5, 1, 2]
    nums = [2, 2, 2, 0, 1]
    nums = [1, 3, 5]  # 1
    nums = [3, 1, 3]
    nums = [3, 1, 3, 3]
    nums = [1, 2, 1]
    nums = [1, 1]
    nums = [10, 10, 10, 1, 10]
    nums = [1, 3, 3]

    test = Solution()
    ret = test.minArray(nums)
    print(ret)


if __name__ == '__main__':
    main()
