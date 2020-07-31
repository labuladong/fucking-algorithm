

## question
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
## solution

### 我自己

```python
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        if numbers == []: return 
        if len(numbers) == 1: return numbers[0]
        _res = numbers[0]
        for i in range(1,len(numbers)):
            if _res >= numbers[i]: _res=numbers[i]
        return _res

```

### 直接查找
时间复杂度O(n),空间复杂度O(1)
代码

class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        return min(numbers)

### 二分查找(特例分析)


使用二分法解这个题目,先看普通的情况,给定数组numbers = [3,4,5,1,2],通过观察可以看出来最小的数字是1,并且这个数组能看做是由两部分组成的,第一部分为前面的递增数组[3,4,5],第二部分为后面的递增数组[1,2],也能看出来前面递增数组中所有的数字大于后面递增数组中的数,而我们所要找的数字1是位于后面递增数组的第一位
使用二分法,设置头尾两个指针low和high,mid = (low + high) / 2
当numbers[mid] >= numbers[low]时,说明mid此时位于前面的递增数组中,令mid = low
当numbers[mid] <= numbers[high]时,说明mid此时位于后面的递增数组中,令mid = high
可以看出来这样操作,指针low永远位于前面的递增数组中,指针high位于后面的递增数组中,循环到最后low指向前面递增数组的最后一位,指针high指向后面数组的第一位,所以终止条件可以设定成high-low == 1,此时返回numbers[high]即可
好了,上面是对一般情况的梳理.下面我们看一些特例
当数组为[1,2,3,4,5]时,意思是把数组前0个元素搬到后面,这样的话最小值就是第一个值,所以我们将初始的mid = low,指向第一个元素
当数组为[1,0,1,1,1]时,我们看下此时low = 0,high=4,mid = 2,并且numbers[low] == numbers[high] == numbers[mid],我们是无法判断mid是位于前面还是后面的递增数组的,所以当初先这样的情况需通过顺序查找
我么就分分析下[1,0,1,1,1],当不加入上面的条件时,初始low = 0,high=4,mid = 2,numbers[mid] <= numbers[low],此时mid=2,此时遍历的数组变为[1,1,1],可以看到其实最小值是0,但这个数组中没有包含0,所以需要加入上面的条件来判断

时间复杂度O(logn),空间复杂度O(1)

代码
```py
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        if not numbers:
            return None
        low = 0
        high = len(numbers) - 1
        mid = low
        while numbers[low] >= numbers[high]:
            if high - low == 1:
                mid = high
                return numbers[mid]
            mid = (low + high) / 2
            if numbers[low] == numbers[high] and numbers[mid] == numbers[low]:
                temp = numbers[low]
                for i in numbers[low:high+1]:
                    if temp > i:
                        temp = i
                return temp
            if numbers[mid] >= numbers[low]:#位于前面的递增数组
                low = mid
            elif numbers[mid] <= numbers[high]:#位于后面的递增数组
                high = mid
        return numbers[mid]
```


### 分治法


分治法是不断的缩小范围,从而找到符合条件的解
二分法的分析我们知道,数组可以分为前后两个递增数组,下面的分析也都利用递增的特性
当numbers[mid] > numbers[high]时,说明最小值在mid的右边,缩小范围low = mid + 1
当numbers[mid] == numbers[high]时,我们不知道最小值的范围,但是可以肯定的是去除numbers[high]是没有影响的,缩小范围high -= 1
当numbers[mid] < numbers[high]时,我们知道最小值的不是numbers[mid]]就是在mid的左边,缩小范围high = mid
代码
```py
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        if not numbers:
            return None
        low = 0
        high = len(numbers) - 1
        while low < high:
            mid = (low + high) >> 1  ## 用位移的方法 来除以 二
            if numbers[mid] > numbers[high]:
                low = mid + 1
            elif numbers[mid] == numbers[high]:
                high -= 1
            else:
                high = mid
        return numbers[low]
```

作者：xiao-xue-66
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/pythonti-jie-er-fen-fa-shuang-100he-zhi-jie-cha-zh/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。