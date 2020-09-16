## question
[剑指 Offer 57 - II. 和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/)
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5
 

通过次数57,174提交次数82,746
## solution

### code 

```py
class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        import math
        for n in range(2,(int(math.sqrt(2*target))+2)):
            if (2*target % n) == 0 and ((2*target/n) ^ n ) % 2 == 1:
                a1 = ((2*target/n) - n +1 )/ 2
                if a1: res.append([a1+i for i in range(n)])
        return res[::-1]
```


