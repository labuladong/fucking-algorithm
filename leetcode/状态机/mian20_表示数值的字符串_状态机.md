
<!-- TOC -->

- [solution](#solution)
    - [状态机](#%E7%8A%B6%E6%80%81%E6%9C%BA)
        - [字符类型：](#%E5%AD%97%E7%AC%A6%E7%B1%BB%E5%9E%8B)
        - [状态定义：](#%E7%8A%B6%E6%80%81%E5%AE%9A%E4%B9%89)

<!-- /TOC -->

## solution
几个条件
空格只能出现在首尾，出现在中间一定是非法的
正负号只能出现在两个地方，第一个地方是整数的最前面，表示符号。第二个位置是 e 后面，表示指数的正负。如果出现在其它位置也一定是非法的
数字，数字没有进行特别的判断，题目没有前导0的问题
e 只能出现一次，并且 e 之后一定要有数字才是合法的， 12e 这种也是非法的
小数点，由于 e 之后的指数一定是整数，所以小数点最多只能出现一次，并且一定要在 e 之前。所以如果之前出现过小数点或者是 e,再次出现小数点就是非法的

作者：youaresb
链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/biao-shi-shu-zhi-de-zi-fu-chuan-fen-qing-chu-ji-ge/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


### 状态机
![image.png](https://pic.leetcode-cn.com/7998c600dfa355047daaaa82bf4431416d02575445896bc52be4c7b71ddb6bda-image.png)
本题使用有限状态自动机。根据字符类型和合法数值的特点，先定义状态，再画出状态转移图，最后编写代码即可。

#### 字符类型：
空格 「 」、数字「 0—9 」 、正负号 「 +- 」 、小数点 「 . 」 、幂符号 「 e 」 。

#### 状态定义：
按照字符串从左到右的顺序，定义以下 9 种状态。
```bash 
0 开始的空格
1 幂符号前的正负号
2 小数点前的数字
3 小数点、小数点后的数字
4 当小数点前为空格时，小数点、小数点后的数字
5 幂符号
6 幂符号后的正负号
7 幂符号后的数字
8 结尾的空格
```
#### 结束状态：
合法的结束状态有 2, 3, 7, 8 。

作者：jyd
链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/mian-shi-ti-20-biao-shi-shu-zhi-de-zi-fu-chuan-y-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

### 算法流程：
```bash
1 初始化：
    1.1 状态转移表 states ： 设 states[i] ，其中 i 为所处状态， states[i] 使用哈希表存储可转移至的状态。键值对 (key,value) 含义：若输入key ，则可从状态 i 转移至状态 value 。
    1.2 当前状态 p ： 起始状态初始化为 p=0 。
2 状态转移循环： 遍历字符串 s 的每个字符 c 。
    2.1 记录字符类型t ： 分为三种情况。
        当 c 为正负号时，t = 's' ;
        当 c 为数字时，t = 'd' ;
        否则，t = c ，即用字符本身表示字符类型 ;
    2.2 终止条件： 若字符类型 t 不在哈希表 states[p] 中，说明无法转移至下一状态，因此直接返回 False 。
    2.3 状态转移： 状态 pp 转移至 states[p][t] 。

3 返回值： 跳出循环后，若状态p∈ {2,3,7,8} ，说明结尾合法，返回 True ，否则返回 False 。
```
#### 复杂度分析：
时间复杂度 O(N) ： 其中 N 为字符串 s 的长度，判断需遍历字符串，每轮状态转移的使用 O(1) 时间。
空间复杂度 O(1) ： states 和 p 使用常数大小的额外空间

```python
class Solution:
    def isNumber(self, s):
        states = [
            { ' ': 0, 's': 1, 'd': 2, '.': 4 }, # 0. start with 'blank'
            { 'd': 2, '.': 4 } ,                # 1. 'sign' before 'e'
            { 'd': 2, '.': 3, 'e': 5, ' ': 8 }, # 2. 'digit' before 'dot'
            { 'd': 3, 'e': 5, ' ': 8 },         # 3. 'digit' after 'dot'
            { 'd': 3 },                         # 4. 'digit' after 'dot' (‘blank’ before 'dot')
            { 's': 6, 'd': 7 },                 # 5. 'e'
            { 'd': 7 },                         # 6. 'sign' after 'e'
            { 'd': 7, ' ': 8 },                 # 7. 'digit' after 'e'
            { ' ': 8 }                          # 8. end with 'blank'
        ]
        p = 0                           # start with state 0
        for c in s:
            if '0' <= c <= '9': t = 'd' # digit
            elif c in "+-": t = 's'     # sign
            else: t = c                 # dot, blank, e
            # print '$$$$ ',t,p,' * ',states[p]
            if t not in states[p]: return False
            p = states[p][t]
        return p in (2, 3, 7, 8)
"""
作者：jyd
链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/mian-shi-ti-20-biao-shi-shu-zhi-de-zi-fu-chuan-y-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
```