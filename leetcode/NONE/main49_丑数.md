
## question
[剑指 Offer 49. 丑数](https://leetcode-cn.com/problems/chou-shu-lcof/)
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

 

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。
注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/

通过次数28,505提交次数44,265
在真实的面试中遇到过这道题？
## solution
丑数的定义
我们把只包含因子 2、3 和 5 的数称作丑数.

根据题意， 一个丑数必然可以写为 A0 * A1 * ..... * A(n-1) * AnA0∗A1∗.....∗A(n−1)∗An, 其中 A ∈ [2, 3, 5]A∈[2,3,5] 。那么这个丑数也可以写为 (A0 * A1 * ..... * A(n-1)) * An(A0∗A1∗.....∗A(n−1))∗An, (A0 * A1 * ..... * A(n-1))(A0∗A1∗.....∗A(n−1)) 也是个丑数， 而 An ∈ [2, 3, 5]An∈[2,3,5]， 所以一个丑数乘以 2， 3， 5 之后， 一定还是一个丑数。

并且如果从丑数序列首个元素开始 *2 *3 *5 来计算， 丑数序列也是不会产生漏解的。

丑数的排列
假设当前存在 3 个数组 nums2, nums3, nums5 分别代表丑数序列从 1 开始分别乘以 2, 3, 5 的序列， 即


nums2 = {1*2, 2*2, 3*2, 4*2, 5*2, 6*2, 8*2...}
nums3 = {1*3, 2*3, 3*3, 4*3, 5*3, 6*3, 8*3...}
nums5 = {1*5, 2*5, 3*5, 4*5, 5*5, 6*5, 8*5...}
 注意 7 不是丑数. 
2, 3, 5 这前 3 个丑数一定要乘以其它的丑数， 所得的结果才是新的丑数， 所以上例中没有出现 7*2, 7*3, 7*5
那么， 最终的丑数序列实际上就是这 3 个有序序列对的合并结果， 计算丑数序列也就是相当于 合并 3 个有序序列。

合并 3 个有序序列
合并 3 个有序序列， 最简单的方法就是每一个序列都各自维护一个指针， 然后比较指针指向的元素的值， 将最小的放入最终的合并数组中， 并将相应指针向后移动一个元素。 这也就是：

合并过程中重复解的处理
nums2, nums3, nums5 中是存在重复的解的， 例如 nums2[2] == 3*2, nums3[1] == 2*3 都计算出了 6 这个结果， 所以在合并 3 个有序数组的过程中， 还需要跳过相同的结果， 这也就是为什么在比较的时候， 需要使用 3 个并列的 if... if... if... 而不是 if... else if... else 这种结构的原因。 当比较到元素 6 时， if (dp[i] == dp[p2] * 2)...if (dp[i] == dp[p3] * 3)... 可以同时指向 nums2, nums3 中 元素 6 的下一个元素

作者：mrsate
链接：https://leetcode-cn.com/problems/chou-shu-lcof/solution/chou-shu-ii-qing-xi-de-tui-dao-si-lu-by-mrsate/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
### code 
```py

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        res, i = [1], 0
        two, three, five = 0, 0, 0
        for i in range(1,n):
            s_two, s_three, s_five = 2 * res[two], 3 * res[three], 5 * res[five]
            # print "## ",s_two, s_three, s_five
            s_min = min(s_two, s_three, s_five)
            if s_min == s_two: two = two + 1
            if s_min == s_three: three = three + 1
            if s_min == s_five: five = five + 1
            if s_min not in res: res.append(s_min)
            i = i + 1
        return res[-1]
```
