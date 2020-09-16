
## question
[剑指 Offer 56 - I. 数组中数字出现的次数](https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/)
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
 

限制：

2 <= nums.length <= 10000
 

通过次数48,281提交次数67,956
## solution
### 136. 只出现一次的数字 1
题目大意是除了一个数字出现一次，其他都出现了两次，让我们找到出现一次的数。我们执行一次全员异或即可。

```py

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number = 0
        for num in nums:
            single_number ^= num
        return single_number
```
复杂度分析
时间复杂度：O(N)O(N)，其中N为数组长度。
空间复杂度：O(1)O(1)
### 137. 只出现一次的数字 2
题目大意是除了一个数字出现一次，其他都出现了三次，让我们找到出现一次的数。 灵活运用位运算是本题的关键。

```py
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            cnt = 0  # 记录当前 bit 有多少个1
            bit = 1 << i  # 记录当前要操作的 bit
            for num in nums:
                if num & bit != 0:
                    cnt += 1
            if cnt % 3 != 0:
                # 不等于0说明唯一出现的数字在这个 bit 上是1
                res |= bit

        return res - 2 ** 32 if res > 2 ** 31 - 1 else res
```
为什么 Python 最后需要对返回值进行判断？
如果不这么做的话测试用例是 [-2,-2,1,1,-3,1,-3,-3,-4,-2] 的时候，就会输出 4294967292。 其原因在于 Python 是动态类型语言，在这种情况下其会将符号位置的 1 看成了值，而不是当作符号 “负数”。 这是不对的。 正确答案应该是 - 4，-4 的二进制码是 1111...100，就变成 2^32-4=4294967292，解决办法就是 减去 2 ** 32 。

之所以这样不会有问题的原因还在于题目限定的数组范围不会超过 2 ** 32

### 645. 错误的集合
这题没有限制空间复杂度，因此直接 hashmap 存储一下没问题。 不多说了，我们来看一种空间复杂度 O(1)O(1) 的解法。

这里我们的思路是，将 nums 的所有索引提取出一个数组 idx，那么由 idx 和 nums 组成的数组构成 singleNumbers 的输入，其输出是唯二不同的两个数。

但是我们不知道哪个是缺失的，哪个是重复的，因此我们需要重新进行一次遍历，判断出哪个是缺失的，哪个是重复的。

和 260. 只出现一次的数字 3 思路基本一样，我直接复用了代码。

```py
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = 0  # 所有数字异或的结果
        a = 0
        b = 0
        for n in nums:
            ret ^= n
        # 找到第一位不是0的
        h = 1
        while(ret & h == 0):
            h <<= 1
        for n in nums:
            # 根据该位是否为0将其分为两组
            if (h & n == 0):
                a ^= n
            else:
                b ^= n

        return [a, b]

    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums = [0] + nums
        idx = []
        for i in range(len(nums)):
            idx.append(i)
        a, b = self.singleNumbers(nums + idx)
        for num in nums:
            if a == num:
                return [a, b]
        return [b, a]
```

感谢 @云龙 的提醒，上面的 h 计算过程甚至可以简化为 h = res ^ (res & (res-1))

复杂度分析

时间复杂度：O(N)O(N)
空间复杂度：O(N)O(N)，这里我使用了 idx 数组。

### 260. 只出现一次的数字 3(就是本题)
题目大意是除了两个数字出现一次，其他都出现了两次，让我们找到这个两个数。

我们进行一次全员异或操作，得到的结果就是那两个只出现一次的不同的数字的异或结果。

我们刚才讲了异或的规律中有一个 任何数和本身异或则为0， 因此我们的思路是能不能将这两个不同的数字分成两组 A 和 B。
分组需要满足两个条件.

两个独特的的数字分成不同组

相同的数字分成相同组

这样每一组的数据进行异或即可得到那两个数字。

问题的关键点是我们怎么进行分组呢？

由于异或的性质是，同一位相同则为 0，不同则为 1. 我们将所有数字异或的结果一定不是 0，也就是说至少有一位是 1.

我们随便取一个，分组的依据就来了， 就是你取的那一位是 0 分成 1 组，那一位是 1 的分成一组。
这样肯定能保证 2. 相同的数字分成相同组，不同的数字会被分成不同组么。 很明显当然可以， 因此我们选择是 1，也就是
说 两个独特的的数字 在那一位一定是不同的，因此两个独特元素一定会被分成不同组。

```py
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = 0  # 所有数字异或的结果
        a = 0
        b = 0
        for n in nums:
            ret ^= n
        # 找到第一位不是0的
        h = 1
        while(ret & h == 0):
            h <<= 1
        for n in nums:
            # 根据该位是否为0将其分为两组
            if (h & n == 0):
                a ^= n
            else:
                b ^= n

        return [a, b]
```
复杂度分析

时间复杂度：O(N)O(N)，其中N为数组长度。
空间复杂度：O(1)O(1)

作者：fe-lucifer
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/zhi-chu-xian-yi-ci-de-shu-xi-lie-wei-yun-suan-by-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
### code
```py
class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res_two = 0 
        for i in nums:
            res_two = res_two ^ i
        res = res_two

        h = 1
        while(res & h == 0):
            h <<= 1
        # print "  res: ",res, h
        a, b = 0, 0
        for i in nums:
            if (i & h) == 0:
                a = a ^ i
            else:
                b = b ^ i

        return [a, b]



```