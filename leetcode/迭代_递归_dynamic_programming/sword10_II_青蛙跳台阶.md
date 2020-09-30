<!-- TOC -->

- [question](#question)
- [solution](#solution)
- [2 变态台阶问题](#2-变态台阶问题)

<!-- /TOC -->
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


```python
fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
```

第二种记忆方法

```python
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def fib(i):
    if i < 2:
        return 1
    return fib(i-1) + fib(i-2)
```
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
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/solution/sword10_fei-bo-na-qi-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


## 2 变态台阶问题

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

```python
fib = lambda n: n if n < 2 else 2 * fib(n - 1)
```
```py
fib = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)  # 1,2
fib = lambda n: n if n < 3 else fib(n - 1) + fib(n - 2) + f(n-3)  # 1,2,3
fib = lambda n: n if n < 4 else fib(n - 1) + fib(n - 2) + f(n-3) + f(n-4)    # 1,2,3,4
fib = lambda n: n if n < 5 else fib(n - 1) + fib(n - 2) + f(n-3) + f(n-4) + f(n-5)    # 1,2,3,4,5
...
...
## when frag can skip `n` step;
fib = lambda n: n if n < n else fib(n - 1) + fib(n - 2) + ... + f(2) + f(1)    # 1,2...n-1,n
fib(n-1) = lambda n-1: n-1 if n-1 < n-1 else fib(n - 2) + fib(n - 3) + ... + f(2) + f(1)    # 1,2...n-1
fib(n-2) = lambda n-2: n-2 if n-2 < n-2 else fib(n - 3) + fib(n - 4) + ... + f(2) + f(1)    # 1,2...n-2

fib(n) = 2 * fib(n-1)

```