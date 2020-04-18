class Solution(object):
    """
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，
因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
输入：m = 2, n = 3, k = 1     输出：3
输入：m = 3, n = 1, k = 0     输出：1
1 <= n,m <= 100
0 <= k <= 20
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
    """
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def judge(x, y):
            ret = 0
            while x:
                ret += x % 10
                x //= 10
            while y:
                ret += y % 10
                y //= 10
            return ret <= k

        def dfs(x, y):
            que = [(x, y)]
            visit[0][0], count = 1, 1
            while que:
                x, y = que.pop()
                for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= x + a < m and 0 <= y + b < n:
                        if not visit[x + a][y + b] and judge(x + a, y + b):
                            visit[x + a][y + b] = 1
                            count += 1
                            que.append((x + a, y + b))
            return count

        visit = [[0] * n for i in range(m)]
        return dfs(0, 0)


def main():
    m, n, k = 2, 3, 1
    # m, n, k = 3, 1, 0
    m, n, k = 11, 8, 16  # 88
    test = Solution()
    ret = test.movingCount(m, n, k)
    print(ret)


if __name__ == '__main__':
    main()
