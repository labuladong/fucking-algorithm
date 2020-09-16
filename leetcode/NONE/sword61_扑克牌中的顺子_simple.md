## question
[剑指 Offer 61. 扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/)
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

 

示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True
 

限制：

数组长度为 5 

数组的数取值为 [0, 13] .
## solution

### code 

```py
class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if 'J' in nums: nums[nums.index('J')] = 11
        # if 'Q' in nums: nums[nums.index('Q')] = 12
        # if 'K' in nums: nums[nums.index('K')] = 13
        # if 'A' in nums: nums[nums.index('A')] = 1
        # if 'O' in nums: nums[nums.index('K')] = 0
        nums.sort()
        if 0 not in nums:
            if (nums[0] + 4)== (nums[1] + 3) == (nums[2] + 2) == (nums[3] + 1) == nums[4]:  return True
            else: return False
        else:
            list_0 = []
            while 0 in nums:
                list_0.append(nums.pop(0))
            if len(nums) == 1: return True
            elif self.cur_samll(nums) and (nums[-1] - nums[0]) <= 4: return True
            else: return False
        
    def cur_samll(self, nums):
        if len(nums) == 1: return True
        return (nums[0] < nums[1]) and self.cur_samll(nums[1:])


```


