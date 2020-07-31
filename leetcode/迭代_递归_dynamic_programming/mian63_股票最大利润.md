此题 属于 线性， 从后往前看时， 此时 局部最优 == 全局最优。

<!-- TOC -->

- [question](#question)
- [solution](#solution)
    - [动态规划](#%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92)
    - [贪心求解， 暴力](#%E8%B4%AA%E5%BF%83%E6%B1%82%E8%A7%A3-%E6%9A%B4%E5%8A%9B)

<!-- /TOC -->

## question
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。


输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
 

限制：
0 <= 数组长度 <= 10^5

注意：本题与主站 121 题相同：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution
此题 属于 线性， 从后往前看时， 局部最优 也就是 全局最优。


### 动态规划

考虑 每次

```py
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1 or 0:
            return 0
        _max_record = 0
        _max_res = 0 
        for i in xrange(1,len(prices)+1):           ## 从后向前，  空间复杂度 O1， 时间复杂度 On
            if _max_record > prices[-i]:            ## python 中 max() 函数 其实 比 if ,else 更 耗时
                _sub = _max_record - prices[-i]
                if _sub > _max_res : _max_res = _sub
            else:
                _max_record = prices[-i]
        return _max_res
```

### 贪心求解， 暴力
由 定义 可以 直接得出 ， 每次 减去 前面的 值。
```py
        res = 0
        for i in xrange(1,len(prices)):
            for j in xrange(0,len(prices) -1):
                res = max(res, prices[i]-prices[j])
        return res 
        ```
改进下， 时间有序， 从后往前遍历。

python 中 max() 函数 其实 比 if ,else 更 耗时。


```py
        for i in xrange(1,len(prices)):     
            _max_record = max(_max_record, prices[-i])      ## 从 后算起， 当前的最大值。
            _max_res = max(_max_res, _max_record - prices[- i-1])   ## 当前最大值 - 前一天的值
        return _max_res
```
作者：mu-xie-a
链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/solution/mian63_cong-hou-wang-qian-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。