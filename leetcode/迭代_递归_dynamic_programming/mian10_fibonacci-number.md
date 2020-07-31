

## question
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。



输入：n = 2
输出：1

输入：n = 5
输出：5
 

提示：
0 <= n <= 100
注意：本题与主站 509 题相同：https://leetcode-cn.com/problems/fibonacci-number/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution

参考作者：z1m
参考链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/solution/yi-wei-dong-tai-gui-hua-by-ml-zimingmeng/
3. 1. 什么是动态规划（dynamic programming，DP）
很多情况下我们都把动态规划想得太复杂了，我也是其中一个。quora 上有一个回答是这么说的：

首先在一张纸上写下 1+1+1+1+1+1+1+1=？1+1+1+1+1+1+1+1=？
“它等于多少呢？”
我们会立即脱口而出，“等于8！”
如果我们在左边添一个 1 +1+
“会等于多少呢？”
当然，不用想，“等于9！”
“为什么你会计算得这么快呢？”
“因为 8+1=98+1=9”
所以，我们没有重新计算 1+1+1+1+1+1+1+1+11+1+1+1+1+1+1+1+1 的值因为我们记住了前面的和等于8，所以再次计算时只需再加 1 就可以了。

我们通过记住一些事情来节省时间，这就是动态规划的精髓。 具体来说，如果一个问题的子问题会被我们重复利用，我们则可以考虑使用动态规划。


斐波那契数列是经典的一维动态规划题目。我们使用一个长度为 n+1 的数组 dp，dp[i] 为 F(N) 的值。然后初始化 dp[0]，dp[1]，计算每个位置上的值，最后返回第 n 项。

代码
```py
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:  return n
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1] % 1000000007

### 优化版
# class Solution(object):
#     def fib(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n < 2:  return n
#         a = 0
#         b = 1
#         for _ in range(n):
#             a,b = b,a+b
#         return a % 1000000007



        ###  超时 了
        # if n ==0:
        #     return 0
        # if n ==1:
        #     return 1
        # return self.fib(n-1) + self.fib(n-2)
```
作者：mu-xie-a
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/solution/mian10_dong-tai-gui-hua-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。