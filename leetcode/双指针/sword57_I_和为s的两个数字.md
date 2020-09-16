## question

[剑指 Offer 57. 和为s的两个数字](https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/)
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
 

限制：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
通过次数42,710提交次数65,099

## solution
利用 HashMap 可以通过遍历数组找到数字组合，时间和空间复杂度均为 O(N)O(N) ；
注意本题的 numsnums 是 排序数组 ，因此可使用 双指针法 将空间复杂度降低至 O(1)O(1) 。

算法流程：
初始化： 双指针 ii , jj 分别指向数组 numsnums 的左右两端 （俗称对撞双指针）。
循环搜索： 当双指针相遇时跳出；
计算和 s = nums[i] + nums[j]s=nums[i]+nums[j] ；
若 s > targets>target ，则指针 jj 向左移动，即执行 j = j - 1j=j−1 ；
若 s < targets<target ，则指针 ii 向右移动，即执行 i = i + 1i=i+1 ；
若 s = targets=target ，立即返回数组 [nums[i], nums[j]][nums[i],nums[j]] ；
返回空数组，代表无和为 targettarget 的数字组合。

作者：jyd
链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/solution/sword-shi-ti-57-he-wei-s-de-liang-ge-shu-zi-shuang-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
### 双指针 + 二分法 
思路：二分法可加快范围的缩小（超过100%）
时间复杂度： O(lgN) ~ O(N)
空间复杂度： O(1)

算法流程：

初始化： 双指针i,j分别指向数组 nums的两端, split_index = (j + i) >> 1；
循环搜索： 当双指针相遇(i >= j - 1)或找到答案时跳出；
比较nums[j] + nums[i]与target；
c. 当 nums[j] + nums[i] > target时，此时可根据nums[i] + nums[split_index]的结果判断是否要加速缩进
当nums[i] + nums[split_index] > target，可知num[i]加上范围(split_index, j)内的任何一个元素均大于target，此时可加速缩进，令j = split_index - 1，split_index = (j + i) >> 1
当nums[i] + nums[split_index] < target，无法加速缩进，令j -= 1, 易知潜在的右边数字在范围(split_index, j)内，令split_index = (j + split_index) >> 1
当nums[i] + nums[split_index] = target，立即返回数组 [nums[i], nums[split_index]]
当 nums[j] + nums[i] < target时，此时可根据nums[split_index] + nums[j]的结果判断是否要加速缩进
当nums[split_index] + nums[j] < target，可知num[j]加上范围(i, split_index)内的任何一个元素均小于target，可加速缩进，令i = split_index + 1，split_index = (j + i) >> 1
当nums[split_index] + nums[j] > target，无法加速缩进，令i += 1, 易知潜在的左边数字在范围(i, split_index)内，令split_index = (split_index + i) >> 1
当nums[split_index] + nums[j] = target，立即返回数组 [nums[split_index], nums[j]]
当 nums[j] + nums[i] = target时，立即返回数组 [nums[i], nums[j]]
循环中没找到正确答案时，且最终i = j - 1 和 nums[j] + nums[i] = target时，返回数组 [nums[i], nums[j]]，否则返回[]


```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        split_index = (j + i) >> 1
        
        while i < j - 1:
            if nums[j] + nums[i] > target:            
                if nums[split_index] + nums[i] > target:
                    j = split_index - 1
                    split_index = (j + i) >> 1
                elif nums[split_index] + nums[i] < target:
                    j -= 1
                    split_index = (j + split_index) >> 1
                else:
                    return [nums[i], nums[split_index]]
            elif nums[j] + nums[i] < target:   
                if nums[split_index] + nums[j] < target:
                    i =  split_index + 1
                    split_index = (j + i) >> 1   
                elif nums[split_index] + nums[j] > target:
                    i += 1
                    split_index = (i + split_index) >> 1
                else:
                    return [nums[j], nums[split_index]]
            else:
                return [nums[i], nums[j]]

        if i == j - 1 and nums[j] + nums[i] == target:
            return [nums[i], nums[j]]
        else:
            return []
```
作者：harrisliao
链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/solution/shuang-zhi-zhen-gai-jin-ban-er-fen-fa-by-harrislia/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
### code 

```py
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or not target: return []
        l, r = 0, len(nums) -1
        while l < r:
            if nums[l] + nums[r] > target: r = r - 1
            if nums[l] + nums[r] < target: l = l + 1
            if nums[l] + nums[r] == target: return [nums[l],nums[r]] 
```