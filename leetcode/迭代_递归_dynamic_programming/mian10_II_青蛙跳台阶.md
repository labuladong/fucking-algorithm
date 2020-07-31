
## question

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

输入：n = 2
输出：2

输入：n = 7
输出：21
提示：

0 <= n <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


## solution
青蛙跳n级台阶，假如先跳一级，剩下n-1级，假如先跳2级，那就还有n-2级，斐波那契数列出现了A

代码
```py
class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 2
        a = 1
        b = 1
        for _ in xrange(n):
            a,b = b ,a+b
        return a % 1000000007
```
作者：mu-xie-a
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/solution/mian10_fei-bo-na-qi-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。