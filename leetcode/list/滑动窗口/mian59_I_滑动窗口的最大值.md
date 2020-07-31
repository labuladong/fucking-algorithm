
## question
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：
你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution


利用队列。 先进先出。

时间复杂度 On + n * (k + k )
空间复杂度 n + k

代码
```py
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        _window = []
        _vice = []
        _res = []
        def _pop():
            x = _window[0]
            _window.remove(x)
        def _push(x):
            _window.append(x)
        for i in xrange(len(nums)):
            if i+1 < k:
                _push(nums[i])
            else:
                _push(nums[i])
                _res.append(max(_window))
                _pop()
        return _res
```
            

这个解法 其实 如下， 精简后

```py
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums == []:
            return []

        _window =[]
        _res =[]
        for j in xrange(k-1,len(nums)):
            _res.append(max(nums[j-k+1:j+1])) 
        return  _res
```
作者：mu-xie-a
链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/hua-dong-chuang-kou-dui-lie-chang-wei-k-by-mu-xie-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。