主程序寻找起点，辅助函数用于在给定起点和已探测节点的基础上继续DFS探测，同时用一个字典保留已探测的节点避免重复探测。
当探测节点个数等于目标字符串长度时，即可返回；否则回溯至上一节点

作者：luanhz
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/solution/pythonjian-dan-yi-dong-chang-gui-dfshui-su-by-luan/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

<!-- TOC -->

- [question](#question)
- [solution](#solution)

<!-- /TOC -->

## question

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
提示：

1 <= board.length <= 200
1 <= board[i].length <= 200
注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


## solution
```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.word = word
        self.width = len(board)
        self.length = len(board[0])
        self._all_trace = [(-1,0),(0,1),(1,0),(0,-1)]  ## 这解决了 上下左右 寻找的问题

        for i in range(self.width):
            for j in range(self.length):
                if board[i][j] == word[0]:
                    seen = {}  ## 记录 路径， 方便 回溯
                    seen[(i,j)] = 1
                    if self._dfs(i,j, seen): return True
        return False    

    def _dfs(self, i, j, seen):
        if len(seen) >= len(self.word): return True     ## 当长度够， 就返回
        for dx, dy in self._all_trace:
            # x, y = x+dx, y+dy       ##  def _dfs(self, x, y, seen):   当我用这句话时，整体都出错了，原因是 x,y 变量混乱， ， 赋值
            x, y = i+dx, j+dy
            if self.is_vaild(x,y) and (x,y) not in seen and self.board[x][y] == self.word[len(seen)]:
                seen[(x,y)] = 1
                if self._dfs(x,y,seen): ## 深度 遍历
                    return True
                seen.pop((x,y))     ## 回溯   （在 （x,y）上下左右都走一遍 仍没 True 时）
        return False

    def is_vaild(self, i, j):
        #判断坐标是否在范围合法
        return True if 0 <= i < self.width and 0 <= j < self.length else False
```