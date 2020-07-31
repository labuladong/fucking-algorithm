import heapq
<!-- TOC -->

- [question](#question)
- [solution](#solution)

<!-- /TOC -->

## question
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。


输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]


输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
 

限制：
最多会对 addNum、findMedia进行 50000 次调用。
注意：本题与主站 295 题相同：https://leetcode-cn.com/problems/find-median-from-data-stream/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution
参考作者：jyd
参考链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/solution/mian-shi-ti-41-shu-ju-liu-zhong-de-zhong-wei-shu-y/

针对本题，根据以上思路，可以将数据流保存在一个列表中，并在添加元素时 保持数组有序 。此方法的时间复杂度为 O(N) ，其中包括： 查找元素插入位置 O(logN) （二分查找）、向数组某位置插入元素 O(N) （插入位置之后的元素都需要向后移动一位）。

借助 堆 可进一步优化时间复杂度。

建立一个 小顶堆 A 和 大顶堆 B ，各保存列表的一半元素，且规定：

A 保存 较大 的一半，长度为 `N/2`（ N 为偶数）  或 `(N+1)/2 `（ N 为奇数）；
B 保存 较小 的一半，长度为 `N/2`（ N 为偶数）  或 `(N-1)/2 `（ N 为奇数）；

随后，中位数可仅根据 A,B 的堆顶元素计算得到。

```py
import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.big_heap=[]
        self.small_heap=[]


    def addNum(self, num):
        if len(self.big_heap) == len(self.small_heap):
            heapq.heappush(self.small_heap,-num)
            heapq.heappush(self.big_heap,-heapq.heappop(self.small_heap))
        else:
            heapq.heappush(self.big_heap,num)
            heapq.heappush(self.small_heap,-heapq.heappop(self.big_heap))


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.big_heap) != len(self.small_heap):
            return self.big_heap[0] 
        else:
            return ((self.big_heap[0] -self.small_heap[0])/2.0)



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```
作者：mu-xie-a
链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/solution/mian41_da-xiao-ding-dui-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。