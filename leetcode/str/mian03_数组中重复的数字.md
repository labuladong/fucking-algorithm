<!-- TOC -->

- [question](#question)
- [solution](#solution)
    - [排序](#排序)
    - [哈希](#哈希)

<!-- /TOC -->

## question
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
 

限制：

2 <= n <= 100000

通过次数66,939提交次数99,791

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution
```py
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre_list = []
        for i in xrange(len(nums)):
            if nums[i] not in pre_list: ## in 时间复杂度 是 O n
                pre_list.append(nums[i])
            else:
                return nums[i]
```

### 排序
* 思路是将数组排好序,在查找重复数字,这个思路很简单
* 时间复杂度O(nlogn),空间复杂度O(1)
```py
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        pre = nums[0]
        for index in range(1, len(nums)):
            if pre == nums[index]:
                return pre
            pre = nums[index]
"""
作者：xiao-xue-66
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solution/pythonti-jie-san-chong-fang-fa-by-xiao-xue-66/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
```

### 哈希
* 遍历整个数组,当这个数字没有出现过哈希表的时候将其加入进去,如果在哈希表中则直接返回即可
* 时间复杂度O(n),空间复杂度O(n)
```py
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            else:
                return i
        
```