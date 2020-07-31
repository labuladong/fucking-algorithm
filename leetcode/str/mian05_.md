
## question
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

输入：s = "We are happy."
输出："We%20are%20happy."
 

限制：
0 <= s 的长度 <= 10000

通过次数44,801提交次数58,356

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution
```py
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        
        python内置的replace函数用来替换字符串中指定的字符
        时间复杂度O(n),空间复杂度O(1)

        """
        return s.replace(' ','%20')



```

```py
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str

        从头到尾开始扫描,如果当前字符为空格,则用'%20'替换
        时间复杂度O(n),空间复杂度O(n)

        """
        s = list(s)
        for i in range(len(s)):
            if s[i] == ' ':
                s[i] = '%20'
        return ''.join(s)

作者：xiao-xue-66
链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/solution/pythonti-jie-duo-chong-fang-shi-jie-jue-by-xiao-xu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```