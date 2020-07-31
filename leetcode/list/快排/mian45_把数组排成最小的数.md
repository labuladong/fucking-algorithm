str 转 int , 若拼接字符串 x + y > y + x ，则 m > n ；

## question
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。


输入: [10,2]
输出: "102"

输入: [3,30,34,5,9]
输出: "3033459"
 

提示:
0 < nums.length <= 100

输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution
推荐思路
推荐作者：jyd
推荐链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/solution/mian-shi-ti-45-ba-shu-zu-pai-cheng-zui-xiao-de-s-4/
此题求拼接起来的 “最小数字” ，本质上是一个排序问题。
排序判断规则： 设 nums任意两数字的字符串格式 x 和 y ，则
若拼接字符串 x + y > y + x ，则 m > n ；
反之，若 x + y < y + x ，则 n < m ；
根据以上规则，套用任何排序方法对 nums 执行排序即可。





解题思路
重点 在于 字符如何比大小， 应该按照 lenth 来比较

如 3,30, 342,34,3405
应该是 30 3 3405 34 342

```py
class Solution(object):
    def minNumber(self, nums):
        def _compare(low,high):
            _low,_high = str(low),str(high)
            len_low,len_high = len(_low),len(_high)
            if len_low == len_high:
                return True if _low <= _high else False
            elif len_low < len_high:
                # print _low,_high[:len_low+1]
                if _low < _high[:len_low]:
                    return True 
                elif _low == _high[:len_low]:
                    return _compare(_low,_high[len_low:])
                else:
                    return False
            else:
                if _low[:len_high] < _high:
                    return True 
                elif _low[:len_high] == _high:
                    return _compare(_low[len_high:],_high)
                else:
                    return False

        def partition(_list,low,high):
            _val = _list[low]
            while low < high:
                # while low < high and _list[high] >= _val:
                while low < high and _compare(_val,_list[high]):
                    high = high - 1
                _list[low] = _list[high]
                # while low < high and _list[low] <= _val:
                while low < high and _compare(_list[low],_val):
                    low = low + 1
                _list[high] = _list[low]
            _list[low] = _val
            return low
        def qsort(_list,low,high):
            if low < high:
                _index = partition(_list,low,high)
                qsort(_list,low,_index-1)
                qsort(_list,_index+1,high)
        high = len(nums) -1
        qsort(nums,0,high)
        return ''.join(str(i) for i in nums)
```
作者：mu-xie-a
链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/solution/strintbi-da-xiao-by-mu-xie-a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。