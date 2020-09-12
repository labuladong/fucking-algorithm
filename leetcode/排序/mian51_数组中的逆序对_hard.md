

## questions
[剑指 Offer 51. 数组中的逆序对](https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/)
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

 

示例 1:

输入: [7,5,6,4]
输出: 5
 

限制：

0 <= 数组长度 <= 50000

通过次数40,262提交次数87,668
## solution
「归并排序」是分治思想的典型应用，它包含这样三个步骤：

分解： 待排序的区间为 [l, r][l,r]，令 m = \lfloor \frac{l + r}{2} \rfloorm=⌊2l+r⌋，我们把 [l, r][l,r] 分成 [l, m][l,m] 和 [m + 1, r][m+1,r]
解决： 使用归并排序递归地排序两个子序列
合并： 把两个已经排好序的子序列 [l, m][l,m] 和 [m + 1, r][m+1,r] 合并起来
在待排序序列长度为 11 的时候，递归开始「回升」，因为我们默认长度为 11 的序列是排好序的。

思路

那么求逆序对和归并排序又有什么关系呢？关键就在于「归并」当中「并」的过程。我们通过一个实例来看看。假设我们有两个已排序的序列等待合并，分别是 L = \{ 8, 12, 16, 22, 100 \}L={8,12,16,22,100} 和 R = \{ 9, 26, 55, 64, 91 \}R={9,26,55,64,91}。一开始我们用指针 lPtr = 0 指向 LL 的首部，rPtr = 0 指向 RR 的头部。记已经合并好的部分为 MM。


L = [8, 12, 16, 22, 100]   R = [9, 26, 55, 64, 91]  M = []
     |                          |
   lPtr                       rPtr
我们发现 lPtr 指向的元素小于 rPtr 指向的元素，于是把 lPtr 指向的元素放入答案，并把 lPtr 后移一位。


L = [8, 12, 16, 22, 100]   R = [9, 26, 55, 64, 91]  M = [8]
        |                       |
      lPtr                     rPtr
这个时候我们把左边的 88 加入了答案，我们发现右边没有数比 88 小，所以 88 对逆序对总数的「贡献」为 00。

接着我们继续合并，把 99 加入了答案，此时 lPtr 指向 1212，rPtr 指向 2626。


L = [8, 12, 16, 22, 100]   R = [9, 26, 55, 64, 91]  M = [8, 9]
        |                          |
       lPtr                       rPtr
此时 lPtr 比 rPtr 小，把 lPtr 对应的数加入答案，并考虑它对逆序对总数的贡献为 rPtr 相对 RR 首位置的偏移 11（即右边只有一个数比 1212 小，所以只有它和 1212 构成逆序对），以此类推。

我们发现用这种「算贡献」的思想在合并的过程中计算逆序对的数量的时候，只在 lPtr 右移的时候计算，是基于这样的事实：当前 lPtr 指向的数字比 rPtr 小，但是比 RR 中 [0 ... rPtr - 1] 的其他数字大，[0 ... rPtr - 1] 的其他数字本应当排在 lPtr 对应数字的左边，但是它排在了右边，所以这里就贡献了 rPtr 个逆序对。

利用这个思路，我们可以写出如下代码。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/shu-zu-zhong-de-ni-xu-dui-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




首先我们可以使用暴力法，也就是 O(N^2)O(N 
2
 ) 将所有可能枚举出来，如果满足逆，则 cnt+1，最后返回 cnt 即可。这种做法虽然时间复杂度很差，但是在面试的时候，也可以作为一种兜底算法，以及缓解紧张情绪的解法。

我们接下来介绍更广泛使用的，效率更高的解法 分治。 我们进行一次归并排序，并在归并过程中计算逆序数，换句话说 逆序对是归并排序的副产物。

如果不熟悉归并排序，可以先查下相关资料。 如果你直接想看归并排序代码，那么将的代码统计 cnt 部分删除就好了。

归并排序实际上会把数组分成两个有序部分，我们不妨称其为左和右，归并排序的过程中会将左右两部分合并成一个有序的部分，对于每一个左右部分，我们分别计算其逆序数，然后全部加起来就是我们要求的逆序数。 那么分别如何求解左右部分的逆序数呢？

首先我们知道归并排序的核心在于合并，而合并两个有序数组是一个简单题目。 我这里给贴一下大概算法：

```py
def mergeTwo(nums1, nums2):
    res = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums[j]:
            res.append(nums[i])
            i += 1
        else:
            res.append(nums[j])
            j += 1
    while i < len(nums1) :
        res.append(num[i])
        i += 1
    while j < len(nums1) :
        res.append(num[j])
        j += 1
    return res
```

而我们要做的就是在上面的合并过程中统计逆序数。
️
比如对于左：[1，2，3，4]右：[2，5]。 其中 i，j 指针如粗体部分。 那么 逆序数就是 mid - i + 1 也就是 3 - 2 + 1 = 2 即（3，2)和 (4，2)。 其原因在于如果 3 大于 2，那么 3 后面不用看了，肯定都大于 2。
️
之后会变成：[1，2，3，4] 右：[2，5]

作者：fe-lucifer
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/jian-dan-yi-dong-gui-bing-pai-xu-python-by-azl3979/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
### code


```py
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.cnt = 0
        kk = self.mergeSort(nums)
        # print "## sorted :", kk
        return self.cnt
    
    def merge(self, left, right):
        l, r, length_l,length_r = 0, 0, len(left), len(right)
        res = []
        while l < length_l and r < length_r:
            if left[l] <= right[r]:
                res.append(left[l])
                l = l + 1
            else:
                self.cnt = self.cnt + length_l -l
                # print "## ",left[l:], right[r]
                res.append(right[r])
                r = r + 1
        if l < length_l:
            res = res + left[l:]
        if r < length_r:
            res = res + right[r:]
        return res

    def mergeSort(self, nums):
        # print nums
        if len(nums) <= 1: return nums
        mid =(len(nums)-1) / 2
        left = self.mergeSort(nums[:mid+1])
        right = self.mergeSort(nums[mid+1:])
        return self.merge(left, right)
```