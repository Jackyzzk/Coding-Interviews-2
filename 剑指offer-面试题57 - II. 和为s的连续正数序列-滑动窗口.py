class Solution(object):
    """
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
输入：target = 9
输出：[[2,3,4],[4,5]]
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
1 <= target <= 10^5
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
    """
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        p1, p2, acc = 1, 1, 1
        while p2 < target:
            if acc < target:
                p2 += 1
                acc += p2
            elif acc > target:
                acc -= p1
                p1 += 1
            else:
                p2 += 1
                ret.append([i for i in range(p1, p2)])
                acc += p2 - p1
                p1 += 1
        return ret


def main():
    target = 9
    # target = 15
    test = Solution()
    ret = test.findContinuousSequence(target)
    print(ret)


if __name__ == '__main__':
    main()
