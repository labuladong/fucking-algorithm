## question
[剑指 Offer 58 - II. 左旋转字符串](https://accounts.google.com/b/0/AddMailService)
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

 

示例 1：

输入: s = "abcdefg", k = 2
输出: "cdefgab"
示例 2：

输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
 

限制：

1 <= k < s.length <= 10000
## solution
https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/solution/yuan-di-ju-bu-fan-zhuan-zheng-ti-fan-zhuan-xiang-j/
### code 

```py
class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        if not s or n > len(s) or not n: return s
        return ''.join([s[n:],s[:n]])  ## ''.join()  比 s[n:] + s[:n] 性能更高
```


