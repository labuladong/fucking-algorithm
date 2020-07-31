<!-- TOC -->

- [question](#question)
- [solution](#solution)

<!-- /TOC -->
## question
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

 

示例：

输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

提示：

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sums-divisible-by-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution

参考了 LotusPanda https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/solution/xiong-mao-shua-ti-python3-you-qian-zhui-he-fu-xi-p/
1 题解
这道题用前缀和的思路进行解题时无疑了(看到了连续子数组，就大概想到了这个方法，然后这道题是加了点小变形，就是和被K整除这个条件，mod运算在Python中的实现和其它语言稍有不同，下面会讲到，也是给自己充电，之前没注意过负数求mod这一点)，

1.1类似题目 前缀和的题目，：
560. 和为K的子数组
1248. 统计「优美子数组」
1371. 每个元音包含偶数次的最长子字符串

```py
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        pre_mod_list = {0:0}
        _sum, res= 0, 0
        for i in range(len(A)):
            _sum = _sum + A[i]
            _mod = _sum % K
            if _mod == 0:
                res = res + 1
            if _mod in pre_mod_list:
                res = res + pre_mod_list[_mod]
                pre_mod_list[_mod] = pre_mod_list[_mod] + 1 
            else:
                pre_mod_list[_mod] = 1
        return res
```
作者：mu-xie-a
链接：https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/solution/qian-zhui-he-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。