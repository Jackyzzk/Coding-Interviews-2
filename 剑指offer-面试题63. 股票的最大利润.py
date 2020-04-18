class Solution(object):
    """
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
交易一次
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
0 <= 数组长度 <= 10^5
注意：本题与主站 121 题相同：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # rest -> hold -> rest
        rest, hold = 0, float('-inf')
        for x in prices:
            rest, hold = max(rest, hold + x), max(hold, 0 - x)  # 只交易一次，买入钱rest唯一，且为0
        return rest


def main():
    prices = [7, 1, 5, 3, 6, 4]
    test = Solution()
    ret = test.maxProfit(prices)
    print(ret)


if __name__ == '__main__':
    main()
