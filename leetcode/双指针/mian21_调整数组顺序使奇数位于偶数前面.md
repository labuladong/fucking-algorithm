

## question
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 

注：[3,1,2,4] 也是正确的答案之一。

提示
1 <= nums.length <= 50000
1 <= nums[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution

```python
class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0 or len(nums)==1:
            return nums
        for i in range(len(nums)):
            if nums[i]%2==0:
                p1=i  ## 第一个 偶数
                break
            if i==len(nums)-1: return nums
        p2=p1+1
        while p2<len(nums):
            if nums[p2]%2==1:  ## 每遇到 一个  奇数。 都和 第一个  偶数 交换， 事实上 所有奇数 都在第一个 偶数 之前， 所以，前半段都是奇数，后半段都是 偶数。
                nums[p1],nums[p2]=nums[p2],nums[p1]
                p1+=1
                p2+=1
            else:
                p2+=1
        return nums
```

### 解法2：首端快慢指针
双指针一快一慢，慢指针p1用于定位需要被替换的偶数位，当快指针p2指向奇数时，两个数值才交换。

复杂度分析：
时间复杂度 O(n)：n为数组 nums长度。
空间复杂度 O(1)：双指针p1, p2占用常数大小的额外空间


### 解法3：两端双指针
双指针一前一后，当满足p1指向偶数，p2指向奇数时，两个数值才交换。

复杂度分析：
时间复杂度 O(n)：n为数组 nums长度。
空间复杂度 O(1)：双指针p1, p2占用常数大小的额外空间。


```py
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if len(nums)==0 or len(nums)==1:
            return nums
        p1,p2=0,len(nums)-1
        while p1<p2:
            if nums[p1]%2==1 and nums[p2]%2==1:
                p1+=1
            elif nums[p1]%2==0 and nums[p2]%2==0:
                p2-=1
            elif nums[p1]%2==0 and nums[p2]%2==1:
                nums[p1],nums[p2]=nums[p2],nums[p1]
                p1+=1
                p2-=1
            elif nums[p1]%2==1 and nums[p2]%2==0:
                p1+=1
                p2-=1
        return nums
```
作者：tMEvDjNBzk
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/solution/python-3chong-jie-fa-by-tmevdjnbzk/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
