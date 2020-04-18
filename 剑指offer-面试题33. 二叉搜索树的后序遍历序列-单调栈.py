class Solution(object):
    """
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
参考以下这颗二叉搜索树：
     5
    / \
   2   6
  / \
 1   3
输入: [1,6,3,2,5]
输出: false
输入: [1,3,2,6,5]
输出: true
数组长度 <= 1000
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
    """
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        def dfs(p1, p2):
            if p1 >= p2:
                return True
            i = p1
            while postorder[i] < postorder[p2]:
                i += 1
            mid = i
            while postorder[i] > postorder[p2]:
                i += 1
            if i == p2 and dfs(p1, mid - 1) and dfs(mid, p2 - 1):
                return True

        if dfs(0, len(postorder) - 1):
            return True
        return False


def main():
    post = [1, 6, 3, 2, 5]
    # post = [1, 3, 2, 6, 5]
    # post = [4, 6, 7, 5]  # True
    test = Solution()
    ret = test.verifyPostorder(post)
    print(ret)


if __name__ == '__main__':
    main()
