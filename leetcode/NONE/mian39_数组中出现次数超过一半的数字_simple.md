
## question

剑指 Offer 39. 数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

 

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
 

限制：

1 <= 数组长度 <= 50000

 

注意：本题与主站 169 题相同：https://leetcode-cn.com/problems/majority-element/

## solution
答案一定是排序后的数组的中间元素

代码
```py
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[int(len(nums)/2)]
```
作者：wow_leetcode
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solution/pythonpython3-yi-xing-shi-jian-ji-bai-7116-nei-cun/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
## code 

```py
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = {}
        if not nums: return None
        length = len(nums)/2
        for num in nums:
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] = cnt[num] + 1
            if cnt[num] > length:
                return num
```
