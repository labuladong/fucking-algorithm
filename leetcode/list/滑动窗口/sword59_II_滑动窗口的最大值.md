**要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)**
**辅助队列来记录最大值**， deque
from collections import deque
<!-- TOC -->

- [question](#question)
- [solution](#solution)

<!-- /TOC -->

## question
请定义一个队列并实现函数 max_value 得到队列里的最大值，**要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)**。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：
输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]

示例 2：
输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
 

限制：
1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution

参考作者：quantumdriver
参考链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/solution/python-xiang-jie-wei-he-tian-jia-fu-zhu-dui-lie-ji/<!-- -->


看到不少同学直接用max()函数，显然这是不符合题目中O(1)O(1)时间复杂度的。因为max()会在列表中检查每一个元素，从而返回最大值，所以max()是O(n)O(n)的时间复杂度。


要想在O(1)O(1)时间内做到取出最大值，我们可以想到，能否用一个cur_max的变量，来记录并且比较每一次新入队的value，这个想法是极好的，但是如果队列是[4,3]这个样子，cur_max只会记下4是最大的，当调用一次pop_front()后，此时队列为[3]，而cur_max没有变化，所以单个变量记录最大值行不通。

进一步地我们可以想到，一个变量不行，那我直接用一个辅助队列记录值OK不OK呢？

答案是OK的。我们让辅助队列的数从大到小排列好，要找最大值直接返回辅助队列的头部即可，同时这也是O(1)O(1)时间复杂度的操作，完美契合题意。下面详细讲讲辅助队列怎么能够实现这个操作。

详细步骤
我们先初始化两个队列：
原始队列que = []，帮助我们记录原始数值。
辅助队列sort_que = []，帮助我们对原始数值进行排序。

对于原始队列que，来一个就装一个，走一个就放一个，没啥好担心的。

重点是这个辅助队列sort_que。

第一个问题：sort_que里面怎么排序？
要回答这个问题，我们首先要知道，队列的性质是先进先出。

假设原始队列是[1,2]，那么先走的那一位是队列里面的1。我们的sort_que的头部理应为2，因为原始队列[1,2]的最大值是2。即使对原始队列[1,2]调用pop_front造成1的离开，最大值依然是2，此时，我们仍然需要保持sort_que的头部仍是2。

这个要求，就衍生出了sort_que队列的怎么排序了，请看代码：

while sort_que and sort_que[-1] < value:
sort_que.pop()
self.sort_que.append(value)
这就是说，如果sort_que不为空，并且sort_que的最后一位元素小于当前入队元素value的话，直接把最后一位元素弹走，直到sort_que为空，或sort_que的最后一位元素大于等于value。这就保证了，sort_que的头部总是原始队列que的最大值~

第二个问题：原始队列que发生pop_front时sort_que该怎么变动？
这个其实比较简单，当que弹出的数恰好等于sort_que的头部元素时，咱把sort_que的头部也跟着弹出就好。请看代码：

res = que.pop(0)
if res == sort_que[0]:
sort_que.pop(0)


```py
class MaxQueue(object):

    def __init__(self):
        from collections import deque
        self._queue = deque([])
        self.sort_queue = deque([])

    def max_value(self):
        """
        :rtype: int
        """
        return self.sort_queue[0] if self.sort_queue else -1


    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        while self.sort_queue and self.sort_queue[-1] < value:
            self.sort_queue.pop()
        self.sort_queue.append(value)
        self._queue.append(value)


    def pop_front(self):
        """
        :rtype: int
        """
        if not self._queue:
            return -1
        res = self._queue.popleft()
        if res == self.sort_queue[0]:
            self.sort_queue.popleft()
        return res

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
```

作者：mu-xie-a
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/solution/fu-zhu-dui-lie-deque-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。