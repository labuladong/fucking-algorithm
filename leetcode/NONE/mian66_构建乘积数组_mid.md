## question
[剑指 Offer 66. 构建乘积数组](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/)

给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

 

示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
 

提示：

所有元素乘积之和不会溢出 32 位整数
a.length <= 100000
## solution
本题的难点在于 不能使用除法 ，即需要 只用乘法 生成数组 BB 。根据题目对 B[i]B[i] 的定义，可列表格，如下图所示。

根据表格的主对角线（全为 11 ），可将表格分为 上三角 和 下三角 两部分。分别迭代计算下三角和上三角两部分的乘积，即可 不使用除法 就获得结果。

![](./mian66-Picture1.png)

算法流程：
初始化：数组 BB ，其中 B[0] = 1B[0]=1 ；辅助变量 tmp = 1tmp=1 ；
计算 B[i]B[i] 的 下三角 各元素的乘积，直接乘入 B[i]B[i] ；
计算 B[i]B[i] 的 上三角 各元素的乘积，记为 tmptmp ，并乘入 B[i]B[i] ；
返回 BB 。
复杂度分析：
时间复杂度 O(N)O(N) ： 其中 NN 为数组长度，两轮遍历数组 aa ，使用 O(N)O(N) 时间。
空间复杂度 O(1)O(1) ： 变量 tmptmp 使用常数大小额外空间（数组 bb 作为返回值，不计入复杂度考虑）

作者：jyd
链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/solution/mian-shi-ti-66-gou-jian-cheng-ji-shu-zu-biao-ge-fe/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
### code 

```py
class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        n = len(a)
        b_up = [1] * n
        b_down = [1] * n
        for i in range(1,n):
            b_up[i] = b_up[i-1] * a[i-1]
            b_down[n-i-1] = b_down[n-i] * a[n-i]

        return [b_up[i]*b_down[i] for i in range(n)]
```


