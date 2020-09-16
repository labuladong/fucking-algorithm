## question
[剑指 Offer 38. 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/)
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 

限制：

1 <= s 的长度 <= 8
## solution

### code 
```py
class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) == 1 or not s: return [s]
        self._len = len(s)
        return list(self.recur(s[1:], [s[0]]))

    def recur(self, _s, _list):
        if not _s: return _list
        new_list = set()    ## set 极大提升了效率
        _input_s = _s[0]
        _len = self._len - len(_s) + 1
        for i in range(_len):
            for j in _list:
                _l,_r = self.split(j,i)
                _new_str = _l + _input_s + _r
                new_list.add(_new_str)          ## set 直接 去重了。
        if len(_s) > 1:
            _s = _s[1:]
        else: 
            _s = ""
        return self.recur(_s,new_list)
        

    
    def split(self, _str, _index):
        if _index != 0 and _index != len(_str):
            return _str[:_index],_str[_index:]
        elif _index == len(_str):
            return _str,""
        else:
            return "",_str

```