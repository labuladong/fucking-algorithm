此题  局部最优 和 全局最优 没关系， 所以得 遍历所有

**用本身 来存储 值，空间复杂度 降为 O1**
**执行频率高的放在前面， 减少频率少的操作**
<!-- TOC -->

- [question](#question)
- [solution](#solution)
    - [空间优化](#%E7%A9%BA%E9%97%B4%E4%BC%98%E5%8C%96)
    - [执行频率 再优化](#%E6%89%A7%E8%A1%8C%E9%A2%91%E7%8E%87-%E5%86%8D%E4%BC%98%E5%8C%96)

<!-- /TOC -->

## question
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？


输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
 

提示：

0 < grid.length <= 200
0 < grid[0].length <= 200
通过次数17,696提交次数26,131

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution
就是 时间 复杂度 有点危险
空间复杂度 O m*n


```py
class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        _record = {}            ## _record 做记录， 


        def _reverse(grid,j,i,_record):
            _key = str(j)+ "_"+ str(i)
            if _key in _record:
                return _record[_key]
            _max = 0
            if j == 0 and i ==0:
                return grid[j][i] 
            elif j == 0:
                return (grid[j][i]  + _reverse(grid,j,i-1,_record))
            elif i == 0:
                return (grid[j][i] + _reverse(grid,j-1,i,_record))
            else:
                return (grid[j][i] + max(_reverse(grid,j-1,i,_record), _reverse(grid,j,i-1,_record)))

        for i in range(m):
            for j in range(n):
                 _val = _reverse(grid,i,j,_record)  ## 从小的开始 遍历。
                 _key = str(i)+ "_"+ str(j)
                 _record[_key] = _val

        return _reverse(grid,m-1,n-1,_record)
```       

### 空间优化

空间复杂度优化：
由于 dp[i][j]dp[i][j] 只与 dp[i-1][j]dp[i−1][j] , dp[i][j-1]dp[i][j−1] , grid[i][j]grid[i][j] 有关系，因此可以将原矩阵 gridgrid 用作 dpdp 矩阵，即直接在 gridgrid 上修改即可。
应用此方法可省去 dpdp 矩阵使用的额外空间，因此空间复杂度从 O(MN)O(MN) 降至 O(1)O(1) 。

参考作者：jyd
参考链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/solution/mian-shi-ti-47-li-wu-de-zui-da-jie-zhi-dong-tai-gu/

```py
class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        def _reverse(j,i):
            if j == 0 and i ==0:
                grid[j][i] = grid[j][i] 
            elif j == 0:
                grid[j][i] = grid[j][i]  + grid[j][i-1]
            elif i == 0:
                grid[j][i]= grid[j][i]  + grid[j-1][i]
            else:
                grid[j][i]= grid[j][i]  + max(grid[j][i-1] ,grid[j-1][i])

        for j in range(m):
            for i in range(n):
                 _reverse(j,i)

        return grid[m-1][n-1]
```

### 执行频率 再优化
**执行频率高的放在前面， 减少频率少的操作**

但仍可提升效率：当 grid 矩阵很大时， i = 0或 j = 0的情况仅占极少数，相当循环每轮都冗余了一次判断。因此，可先初始化矩阵第一行和第一列，再开始遍历递推。

```py
class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        for i in xrange(1,n):
            grid[0][i]= grid[0][i]  + grid[0][i-1]
        for j in xrange(1,m):
            grid[j][0] = grid[j][0]  + grid[j-1][0]
        
        for j in xrange(1,m):
            for i in xrange(1,n):
                grid[j][i]= grid[j][i]  + max(grid[j][i-1] ,grid[j-1][i])

        return grid[m-1][n-1]
```
作者：mu-xie-a
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/solution/mian47-_dong-tai-gui-hua-_tan-xin-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。