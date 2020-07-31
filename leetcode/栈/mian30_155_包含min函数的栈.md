**辅助，非严格降序**
<!-- TOC -->

- [question](#question)
- [solutions](#solutions)
    - [正解](#%E6%AD%A3%E8%A7%A3)
    - [欺骗算法](#%E6%AC%BA%E9%AA%97%E7%AE%97%E6%B3%95)

<!-- /TOC -->

## question
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 

提示：

各函数的调用总次数不超过 20000 次
 

注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solutions

参考作者：jyd
参考链接：https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/solution/mian-shi-ti-30-bao-han-minhan-shu-de-zhan-fu-zhu-z/


### 正解
普通栈的 push() 和 pop() 函数的复杂度为 O(1) ；而获取栈最小值 min() 函数需要遍历整个栈，复杂度为 O(N) 。

本题难点： 将 min() 函数复杂度降为 O(1) ，可通过建立辅助栈实现；
数据栈 AA ： 栈 AA 用于存储所有元素，保证入栈 push() 函数、出栈 pop() 函数、获取栈顶 top() 函数的正常逻辑。
辅助栈 BB ： 栈 BB 中存储栈 AA 中所有 非严格降序 的元素，则栈 AA 中的最小元素始终对应栈 BB 的栈顶元素，即 min() 函数只需返回栈 BB 的栈顶元素即可。
因此，只需设法维护好 栈 BB 的元素，使其保持非严格降序，即可实现 min() 函数的 O(1) 复杂度。

函数设计：
push(x) 函数： 重点为保持栈 BB 的元素是 非严格降序 的。

将 xx 压入栈 AA （即 A.add(x) ）；
若 ① 栈 BB 为空 或 ② xx 小于等于 栈 BB 的栈顶元素，则将 xx 压入栈 BB （即 B.add(x) ）。
pop() 函数： 重点为保持栈 A, BA,B 的 元素一致性 。

执行栈 AA 出栈（即 A.pop() ），将出栈元素记为 yy ；
若 yy 等于栈 BB 的栈顶元素，则执行栈 B 出栈（即 B.pop() ）。
top() 函数： 直接返回栈 AA 的栈顶元素即可，即返回 A.peek() 。
min() 函数： 直接返回栈 BB 的栈顶元素即可，即返回 B.peek() 。

```py
class MinStack(object):
    
    def __init__(self):

        self._item = []
        self._vice = []

    def push(self, x):
        self._item.append(x)
        if self._vice and x <= self._vice[-1]:  ## <=
            self._vice.append(x)
        elif not self._vice:
            self._vice.append(x)
        else:
            pass


    def pop(self):
        if self._item:
            x = self._item[-1]
            if self._vice and x == self._vice[-1]:
                self._vice.pop()
            self._item.pop()

    def top(self):
        return self._item[-1] if self._item else -1


    def min(self):
        if self._vice:
            return self._vice[-1]
```


### 欺骗算法

```py
class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._item = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._item.append(x)


    def pop(self):
        """
        :rtype: None
        """
        if self._item:
            self._item.pop()


    def top(self):
        """
        :rtype: int
        """
        return self._item[-1] if self._item else -1


    def min(self):
        """
        :rtype: int
        """
        if self._item:
            return min(self._item)
        else:
            return None
```
作者：mu-xie-a
链接：https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/solution/listshi-xian-appendpopmin-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。