<!-- TOC -->

- [question](#question)
- [solution](#solution)
    - [从低到高](#%E4%BB%8E%E4%BD%8E%E5%88%B0%E9%AB%98)

<!-- /TOC -->

## question
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。


输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1


输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

提示：
2 <= n <= 58
注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/

通过次数24,380提交次数44,834

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution

### 从低到高
这样 更省时间

```py
class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        def _max(x,_record):
            if x in _record: return _record[x]
            res = 0 
            for i in range(1, x): 
                res = max(res, _max(x-i,_record) * i, i * (x-i))
                ## _max(x-i) 里至少会做一次切分， 所以还要保留 i* (x -i), 此时的 （x-i) 是没有切分的 。
            return res

        _record = {1:1,2:1,3:2}          ## _record  记录已经实现的值， 实现 动态规划A
        if n in _record: return _record[n]
        for _j in range(4,n+1):
            res = _max(_j,_record)
            if _j not in _record: _record[_j]=res
        return _record[n]
  ```      
```py
class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        def _max(x,_record):
            
            if x in _record: return _record[x]  
            res = 0 
            for i in range(1, x): 
                res = max(res, _max(x-i,_record) * i, i * (x-i))  
                
            if x not in _record: _record[x]=res
            return res
        _record = {1:1,2:1,3:2}          ## _record  记录已经实现的值， 实现 动态规划A
        res = _max(n,_record)
        return res
    ```   

作者：mu-xie-a
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/mian14_-dong-tai-gui-hua-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。