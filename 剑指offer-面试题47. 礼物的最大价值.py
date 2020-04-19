class Solution(object):
    """
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
0 < grid.length <= 200
0 < grid[0].length <= 200
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
    """
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # row, column = len(grid), len(grid[0])
        # opt = [[0] * column for i in range(row)]
        # for i in range(row):
        #     for j in range(column):
        #         opt[i][j] = max(opt[i - 1][j], opt[i][j - 1]) + grid[i][j]
        # return opt[-1][-1]

        row, column = len(grid), len(grid[0])
        opt = [0] * (column + 1)
        for i in range(row):
            for j in range(1, column + 1):
                opt[j] = max(opt[j], opt[j - 1]) + grid[i][j - 1]
        return opt[-1]


def main():
    grid = \
    [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    test = Solution()
    ret = test.maxValue(grid)
    print(ret)


if __name__ == '__main__':
    main()
