**大数越界**


## question
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
 

说明：

用返回一个整数列表来代替打印
n 为正整数
通过次数27,931提交次数35,567

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
## solution
此处撰写解题思路
![image.png](https://pic.leetcode-cn.com/d9c7e3fa01417c073eda4466a2493a8fd029e5534e5fbe9dad0fd6739fc09a0c-image.png)


```python
class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [_ for _ in range(1,int('9'*n)+1)]
```

大数打印解法：
实际上，本题的主要考点是大数越界情况下的打印。需要解决以下三个问题：

1. 表示大数的变量类型：
无论是 short / int / long ... 任意变量类型，数字的取值范围都是有限的。因此，大数的表示应用字符串 String 类型。
2. 生成数字的字符串集：
使用 int 类型时，每轮可通过 +1+1 生成下个数字，而此方法无法应用至 String 类型。并且， String 类型的数字的进位操作效率较低，例如 "9999" 至 "10000" 需要从个位到千位循环判断，进位 4 次。

观察可知，生成的列表实际上是 nn 位 00 - 99 的 全排列 ，因此可避开进位操作，通过递归生成数字的 String 列表。

3. 递归生成全排列：
基于分治算法的思想，先固定高位，向低位递归，当个位已被固定时，添加数字的字符串。例如当 n = 2n=2 时（数字范围 1 - 991−99 ），固定十位为 00 - 99 ，按顺序依次开启递归，固定个位 00 - 99 ，终止递归并添加数字字符串

作者：jyd
链接：https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/solution/mian-shi-ti-17-da-yin-cong-1-dao-zui-da-de-n-wei-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

```py

class Solution:
    def printNumbers(self, n: int) -> [int]:
        def dfs(x):
            if x == n: # 终止条件：已固定完所有位
                res.append(''.join(num)) # 拼接 num 并添加至 res 尾部
                return
            for i in range(10): # 遍历 0 - 9
                num[x] = str(i) # 固定第 x 位为 i
                dfs(x + 1) # 开启固定第 x + 1 位
        
        num = ['0'] * n # 起始数字定义为 n 个 0 组成的字符列表
        res = [] # 数字字符串列表
        dfs(0) # 开启全排列递归
        return ','.join(res)  # 拼接所有数字字符串，使用逗号隔开，并返回



```
在此方法下，各数字字符串被逗号隔开，共同组成长字符串。返回的数字集字符串如下所示：


输入：n = 1
输出："0,1,2,3,4,5,6,7,8,9"

输入：n = 2
输出："00,01,02,...,10,11,12,...,97,98,99"

输入：n = 3
输出："000,001,002,...,100,101,102,...,997,998,999"