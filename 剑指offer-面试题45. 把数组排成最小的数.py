class Solution(object):
    """
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
输入: [10,2]
输出: "102"
输入: [3,30,34,5,9]
输出: "3033459"
0 < nums.length <= 100
输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof
    """
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n = len(str(max(nums)))
        nums = [str(x) for x in nums]
        aux = {x: x + x[0] * (n - len(x)) for x in nums}
        nums.sort(key=lambda x: (aux[x], x[-1]))
        return ''.join(nums)


def main():
    nums = [3, 30, 34, 5, 9]
    nums = [10, 2]
    nums = [824,938,1399,5607,6973,5703,9609,4398,8247]  # "1399439856075703697382478249389609"  重点在 8247 824的顺序
    # nums = [12,121]  # "12112"
    test = Solution()
    ret = test.minNumber(nums)
    print(ret)


if __name__ == '__main__':
    main()
