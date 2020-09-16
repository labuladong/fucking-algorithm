## question
[剑指 Offer 60. n个骰子的点数](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/)
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

 

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

 

示例 1:

输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:

输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
 

限制：

1 <= n <= 11
## solution

### code 

```py
class Solution(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        _res = [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
        res = [0]
        _sum = (6 ** n)
        while n:
            new = []
            for num in [1, 2, 3, 4, 5, 6]:
                for cnt in res:
                    new.append(cnt+num)
                    # print new
            res = new
            n = n -1
        cnt = {}
        for i in res:
            if i not in cnt:
                cnt[i] = 1
            else:
                cnt[i] = cnt[i] + 1
        # print _sum
        return [(cnt[i]/1.00000/_sum) for i in cnt]
```


