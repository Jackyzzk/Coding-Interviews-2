class Solution(object):
    """
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
所有元素乘积之和不会溢出 32 位整数
a.length <= 100000
链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof
    """
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        n = len(a)
        ret = [1] * n
        for i in range(1, n):
            ret[i] = ret[i - 1] * a[i - 1]
        right = 1
        for i in range(n - 2, -1, -1):
            right *= a[i + 1]
            ret[i] *= right
        return ret


def main():
    a = [1, 2, 3, 4, 5]
    test = Solution()
    ret = test.constructArr(a)
    print(ret)


if __name__ == '__main__':
    main()
