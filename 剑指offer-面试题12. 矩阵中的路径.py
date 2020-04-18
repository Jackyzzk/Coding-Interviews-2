class Solution(object):
    """
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]
但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
1 <= board.length <= 200
1 <= board[i].length <= 200
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
    """
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row, column, n = len(board), len(board[0]), len(word)

        def dfs(x, y, k):
            if k == n:
                return True
            if x < 0 or x >= row or y < 0 or y >= column:
                return False
            if board[x][y] != word[k]:
                return False
            board[x][y] = word[k] * 2  # 表示 visited
            for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if dfs(x + a, y + b, k + 1):
                    return True
            board[x][y] = word[k]
            return False

        for i in range(row):
            for j in range(column):
                if dfs(i, j, 0):
                    return True
        return False


def main():
    board, word = \
        [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]], "ABCCED"
    # board, word = \
    #     [["a", "b"],
    #      ["c", "d"]], "abcd"
    # board, word = [["a"]], "a"
    test = Solution()
    ret = test.exist(board, word)
    print(ret)


if __name__ == '__main__':
    main()
