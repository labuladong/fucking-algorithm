<!-- TOC -->

- [all](#all)
    - [conclusion](#conclusion)
    - [这种是传地址 [[]*n]*m](#%E8%BF%99%E7%A7%8D%E6%98%AF%E4%BC%A0%E5%9C%B0%E5%9D%80-nm)
    - [只交易一次](#%E5%8F%AA%E4%BA%A4%E6%98%93%E4%B8%80%E6%AC%A1)
    - [交易 无数次](#%E4%BA%A4%E6%98%93-%E6%97%A0%E6%95%B0%E6%AC%A1)
    - [交易两次](#%E4%BA%A4%E6%98%93%E4%B8%A4%E6%AC%A1)
    - [交易 k 次](#%E4%BA%A4%E6%98%93-k-%E6%AC%A1)
    - [冷冻期](#%E5%86%B7%E5%86%BB%E6%9C%9F)
    - [Best Time to Buy and Sell Stock with Transaction Fee](#best-time-to-buy-and-sell-stock-with-transaction-fee)

<!-- /TOC -->


[本文参考](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/gu-piao-jiao-yi-xi-lie-tan-xin-si-xiang-he-dong-2/)
[大神借鉴](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/solution/yi-ge-tong-yong-fang-fa-tuan-mie-6-dao-gu-piao-w-5/)
[大神借鉴2](https://github.com/labuladong/fucking-algorithm)
[DP总结](https://blog.csdn.net/qqxx6661/article/details/79951989)

# all

## conclusion

three Dimensions

    1 ： do  /  not do

    2 ： have stock /  donot have

    3 :  1st time, 2nd time, 3th time,... n time

**everytime after we add a variable , we add a dimension ; adding space to reduce time;**



## 这种是传地址 [[]*n]*m

`[[1]*2]*8 `, 这种 list  乘法，其实地址 是一样的， 这种不能用。
`dp = [[[None, None] for _ in range(k+1)] for _ in range(length)]  # (n, k+1, 2)`   而要用这种。

```py
>>> aa = [[1]*2]*8
>>> aa
[[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
>>> aa[0][1]=4
>>> aa
[[1, 4], [1, 4], [1, 4], [1, 4], [1, 4], [1, 4], [1, 4], [1, 4]]
>>> id(aa[0][1])
140459244539872
>>> id(aa[4][1])
140459244539872
```

## 只交易一次

```py
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。

 
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0
"""
        res = 0
        for i in xrange(1,len(prices)):
            for j in xrange(0,len(prices) -1):
                res = max(res, prices[i]-prices[j])
        return res 

        _max_record,_max_res = 0,0
        for i in xrange(1,len(prices)):     
            _max_record = max(_max_record, prices[-i])      ## 从 后算起， 当前的最大值。
            _max_res = max(_max_res, _max_record - prices[- i-1])   ## 当前最大值 - 前一天的值
        return _max_res

```

## 交易 无数次
```py
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

示例 3:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
        _res, _max_record = 0, 0
        for i in xrange(1, len(prices)):     
            _max_record = max(_max_record, prices[-i])
            if _max_record > prices[-i-1]:
                _res = _res + _max_record - prices[-i-1]
                _max_record = prices[-i-1]
        return _res
```

## 交易两次

状态转移方程
```py
dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])       # 右边:今天卖了昨天持有的股票，所以两天买入股票的次数都是j
dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])     # 右边:昨天没有持股而今天买入一只，故昨天买入的次数是j-1
```
注意上面的转移方程只是穷举了第三个维度，要求出整个 DP Table 的状态，需要对 i 和 j 进行遍历。


边界状态
观察状态转移方程知，边界状态需要考虑两个方面：i=0 和 j=0
```py
# j=0 
for i in range(n):
    dp[i][0][0] = 0		# 没有买入过股票，且手头没有持股，则获取的利润为0
    dp[i][0][1] = -float('inf')	# 没有买入过股票，不可能持股，用利润负无穷表示这种不可能

# i=0
for j in range(1, k+1):	# 前面j=0已经赋值了，这里j从1开始
    dp[0][k][0] = 0	
    dp[0][k][1] = -prices[0]
```

特别注意，上述两轮边界定义有交集——`dp[0][0][0]` 和 `dp[0][0][1]` ，后者会得到不同的结果，应以 `j=0 ` 时赋值结果为准。

作者：cheng-cheng-16
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/gu-piao-jiao-yi-xi-lie-tan-xin-si-xiang-he-dong-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```py

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<=1: return 0
        dp = [[[None, None] for _ in range(3)] for _ in range(n)]  # (n, k+1, 2)
        
        # 边界状态需要考虑：1.j=0时对i穷举; 2.i=0时对有效的j穷举(j=1,2)
        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = -float('inf')
        for j in range(1, 3):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]
        
        # 状态转移
        for i in range(1, n):
            for j in range(1, 3):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
        
        return dp[-1][-1][0]
```


## 交易 k 次
这道题理论上和 LeetCode 123（交易次数最多为2） 的解法一样，但是直接提交容易出现超内存的错误，是 DP Table 太大导致的。
有效的交易由买入和卖出构成，至少需要两天；反之，当天买入当天卖出则视为一次无效交易。如果题目给定的最大交易次数 `k<=n/2`，这个 k 是可以有效约束交易次数的；如果给定的 `k>n/2` ，那这个 k 实际上起不到约束作用了，可以认为 `k=+inf`，本题退化为 LeetCode 122（不限交易次数） 。

题目整体思路是判断 `k` 和 `n/2` 的大小关系，两个分支分别用 LeetCode 123 和 LeetCode 122 的代码解决，可有效防止内存超出

作者：cheng-cheng-16
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/gu-piao-jiao-yi-xi-lie-tan-xin-si-xiang-he-dong-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```py
class Solution(object):
    def maxProfit(self, k, prices):
        n = len(prices)
        if n <= 1: return 0

        if k >= n//2:   # 退化为不限制交易次数
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit
        else:           # 限制交易次数为k
            dp = [[[None, None] for _ in range(k+1)] for _ in range(n)]  # (n, k+1, 2)
            for i in range(n):
                dp[i][0][0] = 0
                dp[i][0][1] = -float('inf')
            for j in range(1, k+1):
                dp[0][j][0] = 0
                dp[0][j][1] = -prices[0]
            for i in range(1, n):
                for j in range(1, k+1):
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
            for i in range(len(dp)):
                print i,dp[i]
            return dp[-1][-1][0]
```

## 冷冻期
```py
"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
通过次数29,327提交次数54,288

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


        length = len(prices)
        if length <=1: return 0
        dp = [[None, None] for _ in range(length)]  # (n, k+1, 2)
        for i in range(length):
            dp[i][0] = 0
        dp[0][1]= - prices[0]
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        return dp[-1][0]
```


## Best Time to Buy and Sell Stock with Transaction Fee

```py
"""
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
注意:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
通过次数21,354提交次数32,321

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        length = len(prices)
        if length <=1: return 0
        dp = [[None, None] for _ in range(length)]  # (n, k+1, 2)
        for i in range(length):
            dp[i][0] = 0
        dp[0][1]= - prices[0]
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[-1][0]
```


