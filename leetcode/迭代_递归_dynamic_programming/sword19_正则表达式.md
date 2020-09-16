
<!-- TOC -->

- [question](#question)
- [solution](#solution)
    - [递归](#%E9%80%92%E5%BD%92)
    - [动态规划](#%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92)

<!-- /TOC -->

## question
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。
注意：本题与主站 10 题相同：https://leetcode-cn.com/problems/regular-expression-matching/


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


## solution

### 递归

首先，我们考虑只有 '.' 的情况。这种情况会很简单：我们只需要从左到右依次判断 s[i] 和 p[i] 是否匹配。

如果有星号，它会出现在 p[1] 的位置，这时有两种情况：

星号代表匹配 0 个前面的元素。如 '##' 和 a*##，这时我们直接忽略 p 的 a*，比较 ## 和 ##；
星号代表匹配一个或多个前面的元素。如 aaab 和 a*b，这时我们将忽略 s 的第一个元素，比较 aab 和 a*b。
以上任一情况忽略掉元素进行比较时，剩下的如果匹配，我们认为 s 和 p 是匹配的。

```py

class Solution(object):
    def isMatch(self, s, p):
        
        if not p: return not s
        if not s and len(p) == 1: return False
        _first_match = bool(s and p[0] in {s[0],'.'})
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s,p[2:]) or _first_match and self.isMatch(s[1:],p)  ## 继续匹配 0 个到 多个。
        else:
            return _first_match and self.isMatch(s[1:],p[1:])

```

### 动态规划
很容易想到，dp[i][j] 表示的状态是 s 的前 i 项和 p 的前 j 项是否匹配。

转移方程
现在如果已知了 dp[i-1][j-1] 的状态，我们该如何确定 dp[i][j] 的状态呢？我们可以分三种情况讨论，其中，前两种情况考虑了所有能匹配的情况，剩下的就是不能匹配的情况了：

s[i] == p[j] or p[j] == '.'：比如 abb 和 abb，或者 abb 和 ab. ，很容易得到 dp[i][j] = dp[i-1][j-1] = True。因为 ab 和 ab 是匹配的，如果后面分别加一个 b，或者 s 加一个 b 而 p 加一个 . ，仍然是匹配的。

p[j] == '*'：当 p[j] 为星号时，由于星号与前面的字符相关，因此我们比较星号前面的字符 p[j-1] 和 s[i] 的关系。根据星号前面的字符与 s[i] 是否相等，又可分为以下两种情况：

p[j-1] != s[i]：如果星号前一个字符匹配不上，星号匹配了 0 次，应忽略这两个字符，看 p[j-2] 和 s[i] 是否匹配。 这时 dp[i][j] = dp[i][j-2]。

p[j-1] == s[i] or p[j-1] == '.':星号前面的字符可以与 s[i] 匹配，这种情况下，星号可能匹配了前面的字符的 0 个，也可能匹配了前面字符的多个，当匹配 0 个时，如 ab 和 abb*，或者 ab 和 ab.* ，这时我们需要去掉 p 中的 b* 或 .* 后进行比较，即 dp[i][j] = dp[i][j-2]；当匹配多个时，如 abbb 和 ab*，或者 abbb 和 a.*，我们需要将 s[i] 前面的与 p 重新比较，即 dp[i][j] = dp[i-1][j]

其他情况：以上两种情况把能匹配的都考虑全面了，所以其他情况为不匹配，即 dp[i][j] = False
将以上进行归纳得到状态转移方程

  
dp(i)(j)=   dp(i−1)(j−1),                   s(i) = p(j) or p(j) = .
dp(i)(j)=   dp(i)(j−2),                     p(j) = *, p(j-1) != s(i)
dp(i)(j)=   dp(i−1)(j)ordp(i)(j−2),         p(j) = *, p(j-1)=s(i) or p(j-1) = .
dp(i)(j)=   False                           else
​	

参考作者：z1m
参考链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/solution/hui-su-dong-tai-gui-hua-by-ml-zimingmeng/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```py
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p: return not s
        if not s and len(p) == 1: return False
        m, n = len(s) +1,len(p)+1
        dp=[[False for _ in range(n)] for _ in range(m)]
        dp[0][0] = True
        dp[0][1] = False

        ##  dp[0]表示s字段是一个空字符，所以dp[0][0]=True，是因为两个空字符是匹配的，同理，dp[0][1]=False就比较好理解了，就是空字符和任何一个单独的字符都不匹配， '*'也要和前一个字符串结合才能起作用。如果c等于2，意思就是p字符串有两个字符，如果末尾是'*'，那无论'*'字符前面是什么，都可以算0，也就是一个空字符，所以dp[0][2] = dp[0][0] =True就是这个道理
        for c in range(2, n):
            j = c - 1
            if p[j] == '*':
                dp[0][c] = dp[0][c - 2]

        for _s in range(1,m):
            for _p in range(1,n):
                if s[_s-1] == p[_p-1] or p[_p-1] =='.': 
                    dp[_s][_p]=dp[_s-1][_p-1]
                elif p[_p-1]=='*':
                    if p[_p-2] =='.' or s[_s-1] == p[_p-2]:
                       dp[_s][_p]= dp[_s-1][_p] or dp[_s][_p-2] 
                    else:
                       dp[_s][_p]= dp[_s][_p-2] 
                else:
                       dp[_s][_p]= False
        return dp[m-1][n-1]
```