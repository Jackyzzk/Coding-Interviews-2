class Solution(object):
    """
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
1 <= n <= 11
链接：https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof
    """
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        rec = {0: 1}
        for i in range(n):
            aux = {}
            for x in rec:
                for t in range(1, 7):
                    aux[x + t] = aux.get(x + t, 0) + rec[x]
            rec = aux
        # acc = sum(rec.values()) + 0.0  # 在python2中 '/' 会取整，所以补一个 0.0
        acc = 6 ** n + 0.0
        return [v / acc for v in rec.values()]


def main():
    n = 1
    n = 2
    n = 3  # [0.00463,0.01389,0.02778,0.0463,0.06944,0.09722,0.11574,0.125,
    # 0.125,0.11574,0.09722,0.06944,0.0463,0.02778,0.01389,0.00463]
    test = Solution()
    ret = test.twoSum(n)
    print(ret)


if __name__ == '__main__':
    main()
