## question
[剑指 Offer 44. 数字序列中某一位的数字](https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/)
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

 

示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0
 

限制：

0 <= n < 2^31
注意：本题与主站 400 题相同：https://leetcode-cn.com/problems/nth-digit/

通过次数18,026提交次数45,765
## solution

![规律](./sword44-1.png)

对于第 n 位对应的数字，我们令这个数字对应的数为 target，然后分三步进行。

首先找到这个数字对应的数是几位数，用 digits 表示；
然后确定这个对应的数的数值 target；
最后确定返回值是 target 中的哪个数字。
举个栗子：

比如输入的 n 是 365：

经过第一步计算我们可以得到第 365 个数字表示的数是三位数，n=365-9-90\times2=176n=365−9−90×2=176，digtis = 3。这时 n=176n=176 表示目标数字是三位数中的第 176176 个数字。

我们设目标数字所在的数为 number，计算得到 number=100+176/3=158number=100+176/3=158，idx 是目标数字在 number 中的索引，如果 idx = 0，表示目标数字是 number 中的最后一个数字。

根据步骤2，我们可以计算得到 idx = n % digits = 176 % 3 = 2，说明目标数字应该是 number = 158 中的第二个数字，即输出为 5。

代码

作者：z1m
链接：https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/solution/zhe-shi-yi-dao-shu-xue-ti-ge-zhao-gui-lu-by-z1m/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
### code 

```py
class Solution:
    def findNthDigit(self, n: int) -> int:
        # 首先判断target是几位数，用digits表示
        base = 9
        digits = 1
        while n - base * digits > 0:
            n -= base * digits
            base *= 10
            digits += 1
        # 计算target的值
        idx = n % digits  # 注意由于上面的计算，n现在表示digits位数的第n个数字
        if idx == 0: 
            idx = digits
        number = 1
        for i in range(1,digits):
            number *= 10
        if idx == digits:
            number += n // digits - 1
        else:
            number += n // digits
        # 找到target中对应的数字
        for i in range(idx,digits):
            number //= 10
        return number % 10

作者：z1m
链接：https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/solution/zhe-shi-yi-dao-shu-xue-ti-ge-zhao-gui-lu-by-z1m/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```