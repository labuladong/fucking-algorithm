**递归 + 二分法**

<!-- TOC -->

- [question](#question)
- [solution](#solution)

<!-- /TOC -->

## question

实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。



输入: 2.00000, 10
输出: 1024.00000

输入: 2.10000, 3
输出: 9.26100

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
 

说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
注意：本题与主站 50 题相同：https://leetcode-cn.com/problems/powx-n/

## solution

参考作者：xiao-xue-66
参考链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/pythonti-jie-jian-dan-yi-dong-de-fang-fa-e-by-xiao/

拿到题目后,我们直观的思考是直接递归即可,上例子分析: 求2的10次方

我们使用递归解这个问题,很容易想到将递归进行10次即可,假设要求2的10000次方,那就需要递归10000次,这方法可能是很容易的想到的,但可能并不是高效的
下面我们考虑这样的思考方式,当我们在求解2的4次方这个问题时,我们需要每次乘以2的操作,根据上面描述的递归方法需要进行4次递归的操作,下面这样考虑,
**当我们开始时求出2 * 2=4,这时我们不进行4 * 2=8,8 * 2=16的操作,而进行4 * 4=16,**
因为前面的4已经计算出来了,直接使用即可,这样递归次数减少的两次,以此类推到更多的数上面,这样可以减少递归的次数




```py
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def _mypow(x,n):
            if n ==0:
                return 1
            if n == 1:
                return x
            half_n = _mypow(x,n/2)
            if n %2 == 1:           ## 所有 powx_n 的问题 都可以这样。  其实还是用到的 二分法的 思路。
                return half_n * half_n * x
            else:
                return half_n * half_n
        if n < 0:
            return 1/_mypow(x,-n)
        return _mypow(x,n)



作者：mu-xie-a
链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/mian16_di-gui-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```