<!-- TOC -->

- [question](#question)
- [solution](#solution)
    - [动态规划](#%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92)
    - [更简洁的代码](#%E6%9B%B4%E7%AE%80%E6%B4%81%E7%9A%84%E4%BB%A3%E7%A0%81)
    - [用递归](#%E7%94%A8%E9%80%92%E5%BD%92)

<!-- /TOC -->

## question

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。


输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 

提示
0 <= num < 231


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution

### 动态规划

```py
class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        def _dp(num, _record):
            while len(_record) >= 3:
                _record.popitem(last=False)
            str_num = str(num)
            if str_num in _record:
                return _record[str_num]   ## 动态规划， 每次存储原来的 值。,  每次最多 需要 前两个。
            if 10 <= int(str_num) <= 25:
                _record[str_num] = 2
                return 2
            elif int(str_num) <=9 or len(str_num) == 2 :
                _record[str_num] = 1
                return 1
            else:
                _index = 0
                _s = str_num[0]
                if _s == '1':                ## 这时 有 两种 走法
                    num1, num2 = int(str_num[1:]),int(str_num[2:])
                    _sum = _dp(num1,_record) + _dp(num2,_record) 
                    _record[str_num]=_sum
                    return _sum
                elif _s == '2' and int(str_num[1]) <=5:              ## 这时 有 两种 走法
                    num1, num2 = int(str_num[1:]),int(str_num[2:])
                    _sum = _dp(num1,_record) + _dp(num2,_record) 
                    _record[str_num]=_sum
                    return _sum
                else:           ## 这时 只有 一种 走法
                    num1 = int(str_num[1:])  
                    _sum = _dp(num1,_record) 
                    _record[str_num]=_sum
                    return _sum
            

        origin_str = str_num = str(num)
        from collections import OrderedDict
        _record = OrderedDict()

        if 10 <= int(str_num) <= 25:
            _record[str_num] = 2
            return 2
        elif int(str_num) <=9 or len(str_num) == 2 :
            _record[str_num] = 1
            return 1
        else:
            for i in xrange(2,len(str_num)+1):
                _dp(str_num[-i:], _record)
            return _record[origin_str]
```

### 更简洁的代码
dp[i] = dp[i-2] (使用2个字符) + dp[i-1] (使用1个字符) if 10 <= int(s[i - 1:i + 1]) <= 25 else dp[i-1]
可以只使用两个变量表示上一个和当前的翻译方法数目

```py
class Solution:
    def translateNum(self, num: int) -> int:
        s, a, b = str(num), 1, 1
        for i in range(1, len(s)):
            a, b = b, ((a+b) if 10 <= int(s[i - 1:i + 1]) <= 25 else b)
        return b
```
作者：suibianfahui
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/python-4xing-dai-ma-onshi-jian-o1kong-jian-by-suib/

### 用递归
```py
class Solution(object):
    def translateNum(self, num):
        str_num = str(num)

        if str(num) in  ['0','1','2','3','4','5','6','7','8','9']:
            return 1
        elif str(num) in  ['10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']:
            return 2
        elif len(str_num) == 2:
            return 1
        else:
            _l2 = ['0','1','2','3','4','5']

            index = 0
            i = str_num[0]
            # print "## ",index, i,str_num
            if i == '1' :
                num1, num2 = int(str_num[index+1:]),int(str_num[index+2:])
                # print num1, num2
                sum = self.translateNum(num1) + self.translateNum(num2)
                return sum
            elif i == '2' and str_num[index+1] in _l2:
                num1, num2 = int(str_num[index+1:]),int(str_num[index+2:])
                sum = self.translateNum(num1) + self.translateNum(num2)
                return sum
            else:
                num1 = int(str_num[index+1:])
                return self.translateNum(num1) 
```

作者：mu-xie-a
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/mian46_di-gui-_fei-bo-na-qi-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。