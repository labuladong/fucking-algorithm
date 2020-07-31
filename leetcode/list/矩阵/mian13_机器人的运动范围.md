<!-- TOC -->

- [question](#question)
- [solution](#solution)
    - [代码](#%E4%BB%A3%E7%A0%81)

<!-- /TOC -->

## question
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

输入：m = 2, n = 3, k = 1
输出：3

输入：m = 3, n = 1, k = 0
输出：1

提示：
1 <= n,m <= 100
0 <= k <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution
![image.png](https://pic.leetcode-cn.com/72ed66bd4e90911c848fd70eb4dfa494c1a433139af398569b23addf44d90f4d-image.png)



### 代码

```python
class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def _dfs(i,j,seen):
            for dx,dy in self._around:
                x,y = i+dx,j+dy
                if 0 <= x < self.m and 0<= y < self.n and (x,y) not in seen and self._is_vaild(x,y):
                    seen[(x,y)] = 1
                    self._res = self._res +1
                    _dfs(x,y,seen)

        self.k = k
        self.m = m
        self.n = n
        self._res = 1
        # self._around = [(0,1),(0,-1),(1,0),(-1,0)]
        self._around = [(0,1),(1,0)]  ## 只用到这两个
        seen = {(0,0):1}
        _dfs(0,0,seen)
        return self._res

    def _is_vaild(self,i,j):
        # for _ in str(i):
        #     _sum = _sum + int(_)
        # for _ in str(j):
        #     _sum = _sum + int(_)
        # return True if _sum <= self.k else False          ## str, int 简单易行，
        _sum = 0
        for k in [i,j]:
            if k < 100:
                _sum = _sum + k / 10 + k % 10
            elif k == 100:
                _sum = _sum + 1
            else:
                return False
        return True if _sum <= self.k else False
```

### 数位之和计算：
设一数字 x ，向下取整除法符号 // ，求余符号 %，则有：
x %10 ：得到 x 的个位数字；
x // 10 ： 令 x 的十进制数向右移动一位，即删除个位数字。
因此，可通过循环求得数位和 s ，数位和计算的封装函数如下所示：
```py
def sums(x):
    s = 0
    while x != 0:
        s += x % 10
        x = x // 10
    return s
```
作者：jyd
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。