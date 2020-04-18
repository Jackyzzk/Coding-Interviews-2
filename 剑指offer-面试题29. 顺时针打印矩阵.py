class Solution(object):
    """
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
限制：
0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
    """
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        ret = [matrix[0][0]]
        row, column = len(matrix), len(matrix[0])
        matrix[0][0] = 'v'
        i, j, count = 0, 0, 1
        direction, k = [(0, 1), (1, 0), (0, -1), (-1, 0)], 0

        while count < row * column:
            x, y = i + direction[k][0], j + direction[k][1]
            if 0 <= x < row and 0 <= y < column and matrix[x][y] != 'v':
                i, j = x, y
                ret.append(matrix[i][j])
                count += 1
                matrix[i][j] = 'v'
            else:
                k = (k + 1) % 4

        return ret


def main():
    matrix = \
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    matrix = \
        [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    test = Solution()
    ret = test.spiralOrder(matrix)
    print(ret)


if __name__ == '__main__':
    main()
