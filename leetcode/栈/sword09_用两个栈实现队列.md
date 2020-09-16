

入队入到stack1
出队从stack2出，Stack2为空时，将stack1倒入stack2，这样可以保证队列顺序

<!-- TOC -->

- [question](#question)
- [solution](#solution)

<!-- /TOC -->

## question
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

 

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

示例 2：
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution


入队入到stack1
出队从stack2出，Stack2为空时，将stack1倒入stack2，这样可以保证队列顺序


参考链接 https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/solution/shuang-zhan-yi-ge-ru-yi-ge-chu-by-ajfhkjgo/


```py
class CQueue(object):
    
    def __init__(self):
        self._item = []
        self._vice = []

    def appendTail(self, value):
        self._item.append(value)

    def deleteHead(self):
        if not self._vice:
            while self._item:
                self._vice.append(self._item.pop())
        if self._vice:  ##  每一次都需要 先把 之前的 的 pop 完，才 append();  
            return self._vice.pop()
        else:
            return -1
```

解题思路
append , remove

代码
```py
class CQueue(object):
    
    def __init__(self):
        self._item = []

    def appendTail(self, value):
        self._item.append(value)

    def deleteHead(self):
        if self._item:
            _value = self._item[0]
            self._item.remove(_value)
            return _value
        else:
            return -1
```
作者：mu-xie-a
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/solution/list-shi-xian-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。