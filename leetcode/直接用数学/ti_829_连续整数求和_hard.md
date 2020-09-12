
## question
给定一个正整数 N，试求有多少组连续正整数满足所有数字之和为 N?

示例 1:

输入: 5
输出: 2
解释: 5 = 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
示例 2:

输入: 9
输出: 3
解释: 9 = 9 = 4 + 5 = 2 + 3 + 4
示例 3:

输入: 15
输出: 4
解释: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/consecutive-numbers-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution
方法二：简单数学 [超出时间限制]
假设 kk 个连续正整数的和为 NN，即 N = (x + 1) + (x + 2) + \cdots + (x + k)N=(x+1)+(x+2)+⋯+(x+k)，其中 x \geq 0x≥0，k \geq 1k≥1。上式经过拆分可以得到 N = kx + \frac{1}{2}k(k + 1)N=kx+ 21​	 k(k+1)，即 2N = k(2x + k + 1)2N=k(2x+k+1)。
我们可以枚举 kk，根据上面的等式，kk 的取值范围为 1 \leq k \leq 2N1≤k≤2N。对于每一个 kk，我们计算出 x = \frac{1}{2}(\frac{2N}{k} - k -1)x= 21​	 ( k2N​	−k−1)，如果得到的 xx 是一个非负整数，那么我们就找到了一组解。

方法三：进阶数学
在 2N = k(2x + k + 1)2N=k(2x+k+1) 中，我们可以发现 k < 2x + k + 1k<2x+k+1，因此有 k < \sqrt{2N}k< 2N​	 ，即我们只需要枚举 1 \leq k \leq \lfloor \sqrt{2N} \rfloor1≤k≤⌊ 2N​	 ⌋ 即可，此时通过枚举可以通过本题。我们还可以继续挖掘一些性质。由于 kk 和 2x + k + 12x+k+1 的奇偶性不同，此时将 2N2N 写成 2^\alpha * M2 α ∗M 的形式，其中 \alphaα 为 2N2N 中因子 22 的个数，MM 为一个奇数。对于 MM 的一种拆分 M = a * b, a \leq bM=a∗b,a≤b，可以将 2N2N 分成数 aa 和偶数 2^\alpha * b2 α ∗b 或者奇数 bb 和偶数 2^\alpha * a2 α ∗a，每一种分配方法中，将小的那个数给 kk，大的那个数给 2x + k + 12x+k+1，就对应了一组解，那么一种拆分方法对应了两组解。如果不限制 a \leq ba≤b，那么可以看作一种拆分方法对应了一组解。有一种特殊情况是 a = ba=b，此时这种拆分方法只对应了一组解，但仍然和之前的对应（一对一）相同。因此，我们只需要求出 MM 的拆分方法即可，其中 MM 为 NN 的最大奇因子。MM 的拆分方法等价于 MM 的因子个数。

作者：LeetCode
链接：https://leetcode-cn.com/problems/consecutive-numbers-sum/solution/lian-xu-zheng-shu-qiu-he-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
### code 
```py

class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        import math
        res = 0
        for i in range(1, int(math.sqrt(2*N))+1):
            if (2*N) % i == 0:
                if (2 * N / i - i) % 2 != 0  and (2 * N / i) > 0  :
                    res = res + 1
        return res
```