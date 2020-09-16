## question
[剑指 Offer 64. 求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof/)
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

 

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
 

限制：

1 <= n <= 10000
通过次数65,712提交次数77,135
## solution
逻辑运算符的短路效应：
常见的逻辑运算符有三种，即 “与 \&\&&& ”，“或 ||∣∣ ”，“非 !! ” ；而其有重要的短路效应，如下所示：


if(A && B)  // 若 A 为 false ，则 B 的判断不会执行（即短路），直接判定 A && B 为 false

if(A || B) // 若 A 为 true ，则 B 的判断不会执行（即短路），直接判定 A || B 为 true
本题需要实现 “当 n = 1n=1 时终止递归” 的需求，可通过短路效应实现。


n > 1 && sumNums(n - 1) // 当 n = 1 时 n > 1 不成立 ，此时 “短路” ，终止后续递归

作者：jyd
链接：https://leetcode-cn.com/problems/qiu-12n-lcof/solution/sword-shi-ti-64-qiu-1-2-nluo-ji-fu-duan-lu-qing-xi-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



实验发现Python中的与运算并不像C和C++中那样，Python（2或3）的与运算的返回值是这样的：
（1）如果多个变量均非0（包括None、False等），那么返回最后一个变量的值。如3 and 2 and 'a'的返回值为'a'；
（2）如果多个变量中存在0值，则返回第一个0值。如1 and 'a' and 0 and None的返回值为0。

作者：Lullaby
链接：https://leetcode-cn.com/problems/qiu-12n-lcof/solution/64-pythonji-chu-ni-que-ding-ni-zhi-dao-ma-by-lulla/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
### code
```py
class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        self.recur(n)
        return self.res
    
    def recur(self,n):
        n > 1 and self.recur(n - 1)
        self.res += n

   
```