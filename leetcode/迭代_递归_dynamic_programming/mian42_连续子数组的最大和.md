把当前的 最大 存入自己，（空间复杂度为 O1，）

<!-- TOC -->

- [question](#question)
- [solution](#solution)

<!-- /TOC -->

## question
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。


输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100
注意：本题与主站 53 题相同：https://leetcode-cn.com/problems/maximum-subarray/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution
时间复杂度 On, 空间复杂度 O1.

代码
```py
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _res = nums[0] 
        for i in xrange(1,len(nums)):
            if nums[i -1] >= 0:  ## 
                nums[i] = nums[i-1] + nums[i]  ## 把当前的 最大 存入自己，（空间复杂度为 O1，）     因为要求连续， 所以当前的 最大 一定是需要加上自己。
            else:                               ## 小于 0，  最大的是自己，
                nums[i] = nums[i]
            _res = _res if nums[i] <= _res else nums[i]

        return _res
```
作者：mu-xie-a
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/solution/mian42_dong-tai-gui-hua-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。