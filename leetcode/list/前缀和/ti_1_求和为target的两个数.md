**enumerate,  前缀和**

<!-- TOC -->

- [question](#question)
- [solution](#solution)

<!-- /TOC -->


## question
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。


给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




## solution

```py
class Solution(object):
    def twoSum(self, nums, target):
        aa = {}  ## 记录 已经遍历过的 {elememt: index} 
        bb = []  ## 记录 已经遍历过的  element
        for i, element in enumerate(nums):
            if target - element in bb:
                return [aa[target - element],i]
            else:
                bb.append(element)
                aa[element] = i
```

