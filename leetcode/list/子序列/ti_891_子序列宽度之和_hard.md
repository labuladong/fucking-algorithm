## question

[891. 子序列宽度之和](https://leetcode-cn.com/problems/sum-of-subsequence-widths/)
给定一个整数数组 A ，考虑 A 的所有非空子序列。

对于任意序列 S ，设 S 的宽度是 S 的最大元素和最小元素的差。

返回 A 的所有子序列的宽度之和。

由于答案可能非常大，请返回答案模 10^9+7。

 

示例：

输入：[2,1,3]
输出：6
解释：
子序列为 [1]，[2]，[3]，[2,1]，[2,3]，[1,3]，[2,1,3] 。
相应的宽度是 0，0，0，1，1，2，2 。
这些宽度之和是 6 。
 

提示：

1 <= A.length <= 20000
1 <= A[i] <= 20000

## solution
题目中涉及到“最大”、“最小”，不妨先排个序看看。

排完序之后，我们可以观察到：一个元素是最大元素：当且仅当它是被选取元素中最右边的一个；一个元素是最小元素，当且仅当它是被选取元素中最左边的一个。

所以说，假设排序后一个元素左边有leftleft个元素，右边有rightright个元素，那么这个元素作为最小值出现的子序列一共有2^{right}2 right 个（右边的每个元素可以选取或不选取）；而作为最大值出现的子序列一共有2^{left}2 left 个。因此，元素A[i]对最后的总和的贡献就等于：

(2^{left}-2^{right})\cdot A[i]=(2^i - 2^{n - i - 1})\cdot A[i](2 left −2 right )⋅A[i]=(2 i −2 n−i−1 )⋅A[i]

那么，我们只要预先计算好2的各个幂次的值，就能很轻松地求出最后的结果了。

作者：lucifer1004
链接：https://leetcode-cn.com/problems/sum-of-subsequence-widths/solution/pai-xu-shu-xue-by-lucifer1004/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


答案可以拆分为求所有子序列中，每个子序列的最大值之和，以及最小值之和这两个等价的问题。
以最大值之和为例，考虑原序列S中一个数s，它作为最大值在一个子序列T中出现，意味着S中所有大于s的数都不能在T中出现，这样的子序列个数就等于删去不允许的数后以及这个数本身后，一个长度为rank(s)的序列的所有子序列个数。
我们不难知道，一个长度为k的序列，其全部子序列（包括空的，但不包括也可以，因为空的意味着只有这个数s本身，其宽度为0）的个数为2^k，因此，答案就是将原序列S排序后的序列S'依次求和，求和的每一项是S'[i]*2^i。
类似地，最小值的求和是S'[i]*2^(len(S)-i-1)。
两者相减就是最终答案，注意每一步都要对1000000007取模。
这里为了快速计算2的幂，可以先预处理出来。

作者：iridaze
链接：https://leetcode-cn.com/problems/sum-of-subsequence-widths/solution/891-zi-xu-lie-kuan-du-zhi-he-jian-dan-shu-xue-by-i/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```py

class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        nums = sorted(A, key=lambda x:x)
        res, len_nums = 0, len(nums)
        for index_min, element_min in enumerate(nums):
            count_max = 1 << index_min
            count_min = 1 << (len_nums - index_min -1)
            _single = (count_max -count_min) * element_min
            res = res + _single
        return res % (10**9 + 7)
```