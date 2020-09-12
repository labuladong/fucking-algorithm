
## questions
(940. 不同的子序列 II](https://leetcode-cn.com/problems/distinct-subsequences-ii/)
给定一个字符串 S，计算 S 的不同非空子序列的个数。

因为结果可能很大，所以返回答案模 10^9 + 7.

 

示例 1：

输入："abc"
输出：7
解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。
示例 2：

输入："aba"
输出：6
解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。
示例 3：

输入："aaa"
输出：3
解释：3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。
 

 

提示：

S 只包含小写字母。
1 <= S.length <= 2000

## solution
方法一：动态规划
虽然解决这题的代码很短，但它的算法并不是很容易设计。我们会用动态规划先求出包括空序列的所有子序列，再返回答案之前再减去空序列。

我们用 dp[k] 表示 S[0 .. k] 可以组成的不同子序列的数目。如果 S 中的所有字符都不相同，例如 S = "abcx"，那么状态转移方程就是简单的 dp[k] = dp[k-1] * 2，例如 dp[2] = 8，它包括 ("", "a", "b", "c", "ab", "ac", "bc", "abc") 这 8 个不同的子序列，而 dp[3] 在这些子序列的末尾增加 x，就可以得到额外的 8 个不同的子序列，即 ("x", "ax", "bx", "cx", "abx", "acx", "bcx", "abcx")，因此 dp[3] = 8 * 2 = 16。

但当 S 中有相同字母的时候，就要考虑重复计数的问题了，例如当 S = "abab" 时，我们有：

dp[0] = 2，它包括 ("", "a")；

dp[1] = 4，它包括 ("", "a", "b", "ab")；

dp[2] = 7，它包括 ("", "a", "b", "aa", "ab", "ba", "aba")；

dp[3] = 12，它包括 ("", "a", "b", "aa", "ab", "ba", "bb", "aab", "aba", "abb", "bab", "abab")。

当从 dp[2] 转移到 dp[3] 时，我们只会在 dp[2] 中的 ("b", "aa", "ab", "ba", "aba") 的末尾增加 b，而忽略掉 ("", "a")，因为它们会得到重复的子序列。我们可以发现，这里的 ("", "a") 刚好就是 dp[0]，也就是上一次增加 b 之前的子序列集合。因此我们就得到了如下的状态转移方程：

dp[k] = 2 * dp[k - 1] - dp[last[S[k]] - 1]

即在计算 dp[k] 时，首先会将 dp[k - 1] 对应的子序列的末尾添加 S[k] 得到额外的 dp[k - 1] 个子序列，并减去重复出现的子序列数目，这个数目即为上一次添加 S[k] 之前的子序列数目 dp[last[S[k]] - 1]。

作者：LeetCode
链接：https://leetcode-cn.com/problems/distinct-subsequences-ii/solution/bu-tong-de-zi-xu-lie-ii-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
### code
```py
class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        s0 = S[0]
        last = {}
        _now,_pre = 1,1
        
        for index, element in enumerate(S):
            if element not in last:
                _now = _pre * 2
                last[element] = _pre
            else:
                _now = _pre * 2 - last[element]
                last[element] = _pre
            _pre = _now
        return (_now -1) % (10**9 + 7)
```