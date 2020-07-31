**滑动窗口**  **前缀和**

<!-- TOC -->

- [question](#question)
- [solution](#solution)
    - [前缀和](#%E5%89%8D%E7%BC%80%E5%92%8C)

<!-- /TOC -->

## question
给你一个整数数组 nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。

 

示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
示例 3：

输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16
 

提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution
这里参考 两位 的解答，
作者：sweetiee
链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays/solution/

作者：LotusPanda
链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays/solution/。

解题思路
找到第 i 个奇数的位置，找到第i+k-1个奇数的位置，这就确定了两个边界，再看这两个边界的活动范围有多大就知道有几种组合了。
左边界的活动范围在当前第 i 个奇数到上一个奇数(即 i-1)之间，右边界的活动范围在当前第 i+k-1 到下一个边界(即 i+k)之间。

**左边范围 * 右边活动范围** 在各个位置上的累加就是结果。

```py
class Solution:
    def numberOfSubarrays(self, nums, k):
        l,r,l_ood,r_ood,count = 0,0,0,0,0
        res = 0
        while r < len(nums):
            if nums[r] % 2 ==1:
                r_ood = r_ood + 1
            if r_ood - l_ood == k:
                count_l,count_r=0,0
                r = r + 1       # 之前的是 % 2 ==1,所以需要 + 1， 那自然 待会计算是，count_r 也需要 + 1， 因为左右边界即使都是奇数，只要满足总的奇数为k,都是符合题意。 别忘了两端是奇数的情形。
                while r < len(nums) and nums[r] % 2 == 0:
                    count_r = count_r + 1
                    r = r + 1
                while l < len(nums) and nums[l] % 2 == 0:
                    count_l = count_l + 1
                    l = l + 1
                res = res + (count_r + 1) * (count_l + 1)
                l = l + 1    #  因为上面 所有 % 2 == 0 都结束了， 所以这里是 奇数， 自然 l 需要 右挪。同理 下面 l_ood 需要 + 1 .
                l_ood = l_ood + 1
                continue
            r = r + 1
        return res
```

### 前缀和
下面是 前缀和， 但是超时了。

```py
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        from collections import defaultdict
        odd_count_of_prelist=defaultdict(int)
        odd_count_of_prelist[0]=1
        odd_count = 0
        res = 0

        for i in xrange(len(nums)):
            if nums[i] % 2 ==1:
                odd_count = odd_count + 1
            odd_count_of_prelist[odd_count] = odd_count_of_prelist[odd_count] + 1 ## it is need to + 1, whether it is odd or not
            if odd_count - k in odd_count_of_prelist.keys():
                res = res + odd_count_of_prelist[odd_count - k]
        return res
```

作者：mu-xie-a
链接：https://leetcode-cn.com/problems/count-number-of-nice-subarrays/solution/hua-dong-chuang-kou-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。