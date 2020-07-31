**top min 用最大堆**
<!-- TOC -->

- [question](#question)
- [solution](#solution)
    - [heap](#heap)
    - [quick 到 K](#quick-%E5%88%B0-k)
    - [quicksort所有](#quicksort%E6%89%80%E6%9C%89)

<!-- /TOC -->

## question
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 
示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]
 

限制：
0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution

### heap
```py
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        if arr == [] or len(arr)==1:
            return arr
        _heap = myheap()
        for i in arr:
            if len(_heap.item) >= k:
                _max = _heap.item[0]
                if i < _max:
                    _heap.extract()
                    _heap._add(i)
            else:
                _heap._add(i)
        return _heap.item.values()

class myheap(): 
    def __init__(self):
        self.item = {}
        self.length = 0

    def _add(self,val):
        self.item[self.length] = val
        self.length = self.length + 1
        self.shif_up(self.length-1)

    def shif_up(self, cnx):
        if cnx > 0:
            parent_index = (cnx -1) / 2
            # print parent_index,cnx
            if self.item[parent_index] < self.item[cnx]:
                self.item[parent_index],self.item[cnx] = self.item[cnx],self.item[parent_index]
                self.shif_up(parent_index)

    def ship_down(self, cnx):
        left_index = cnx * 2 +1
        right_index = cnx * 2 +2
        largest_index = cnx 
        if left_index <= self.length and self.item[left_index] > self.item[largest_index] and self.item[left_index] > self.item[right_index]:
            largest_index = left_index
        elif right_index <= self.length and self.item[right_index] > self.item[largest_index]:
            largest_index = right_index
        else:
            pass
        if largest_index != cnx:
            self.item[cnx], self.item[largest_index]= self.item[largest_index],self.item[cnx]
            self.ship_down(largest_index)

    
    def extract(self):
        if self.length <= 0:
            raise Exception('empty')
        val = self.item[0]
        self.item[0]=self.item[self.length-1]
        self.length = self.length - 1
        self.ship_down(0)
        return val
```

### quick 到 K

```py
class Solution():
    def partition(self, _list, l, r):
        _init = _list[l]
        while l < r:
            while l < r and _init <= _list[r]:
                r = r -1
            _list[l]=_list[r]
            while l < r and _list[l] <= _init:
                l = l + 1
            _list[r]=_list[l]
        _list[l] = _init
        return l

    def getLeastNumbers(self, arr, k):
        if k > len(arr) or k <= 0: 
            return []
        high = len(arr) -1
        low = 0
        _list = arr
        _index = self.partition(_list,low,high)
        while _index != k-1:
            if _index < k-1:
                low = _index +1
                _index = self.partition(_list,low,high)
            if _index > k-1:
                high = _index -1
                _index = self.partition(_list,low,high)
        return arr[:k]
```

参考作者：gelthin
参考链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/gelthin-kuai-pai-partition-by-gelthin/
同题目 215. 数组中的第K个最大元素

同题目 面试题 17.14. 最小K个数， 其题解 gelthin-最坏情况partition-O(nk)中分析了最坏情况下，所有元素都相同，partition每一次只能排出一个元素，效率为 O(n*k)

这题直接用 partition， 直至找到 pivot_index == k, 使其前的 k 个值小于 pivot, 后面的值大于 pivot.
不需要完全排完序再处理。

我之前的想法是找到第 k 小的元素，然后在把其他元素和它比较，保留比它小的。
但实际上， 如果使用 partition，找到第 k 小的元素时，arr 已经发生了改变。当我们判断这个元素为第 k 大，实际上就是其前面的元素都比它小，其后面元素都比它大。这里也已经知道了前 k 小的元素。

这里的循环 partition 相当于 selection 的复杂度，平均下来是 O(n) 的复杂度。

T(n) = T(n/2) + O(n)

与带 selection 的 partition 有一些不同之处。按照 Huangyu 老师的 PPT 写的***过于冗余，且复杂。
按照算法导论上有很好的代码模板。在 GitHub 上搜索 ACM 搜到了 quicksort 一个不错的不错的实现

突然醒悟其实这就是基于partition 实现的 selection，不同之处只是在于: 返回第 k+1 个元素还是前 k 个元素。

### quick_sort所有

```py
class Solution():
    def partition(self, _list, l, r):
        _init = _list[l]
        while l < r:
            while l < r and _init <= _list[r]:
                r = r -1
            _list[l]=_list[r]
            while l < r and _list[l] <= _init:
                l = l + 1
            _list[r]=_list[l]
        _list[l] = _init
        return l

    def getLeastNumbers(self, arr, k):
        def quick_sort(_list, low, high):
            if low < high:
                _val = self.partition(_list,low,high)
                new_high =_val-1   
                new_low = _val + 1
                # quick_sort(_list,low, (_val-1 ))  ## 网页上不允许  直接 用 （val -1） 在函数参数里
                quick_sort(_list,low,new_high )
                quick_sort(_list,new_low,high)
        high = len(arr) -1
        quick_sort(arr,0,high)
        return arr[:k]
```
作者：mu-xie-a
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。