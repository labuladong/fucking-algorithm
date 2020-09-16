## question

有个马戏团正在设计叠罗汉的表演节目，一个人要站在另一人的肩膀上。出于实际和美观的考虑，在上面的人要比下面的人矮一点且轻一点。已知马戏团每个人的身高和体重，请编写代码计算叠罗汉最多能叠几个人。

示例：

输入：height = [65,70,56,75,60,68] weight = [100,150,90,190,95,110]
输出：6
解释：从上往下数，叠罗汉最多能叠 6 层：(56,90), (60,95), (65,100), (68,110), (70,150), (75,190)
提示：

height.length == weight.length <= 10000
通过次数4,303提交次数16,881

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/circus-tower-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## solution
题目给出两个维度，两个维度上都满足严格递增的要求才可以叠上去。
考虑需要严格递增，先按照 heightheight 升序排序，同时 heightheight 相同的人按照 weightweight 降序排序。
这样排序下来，直接在数组中查找关于 weightweight 的最长递增子序列就能得到答案。
一个升序，一个降序的是与我们的解决方法相关（我们在排序之后，直接查找体重的最长递增子序列就能得到答案），如： height = [3, 2, 2, 3, 1, 6]，weight = [7,3,5,6,2,10]height=[3,2,2,3,1,6]，weight=[7,3,5,6,2,10]。两个都升序的排序结果是 height = [1, 2, 2, 3, 3, 6]，weight = [2,3,5,6,7,10]height=[1,2,2,3,3,6]，weight=[2,3,5,6,7,10]，直接查找体重的最长递增子序列结果是 66，可以看到，同一身高内部可能存在体重的递增。因此，会被加入结果。而使用身高升序，体重降序，排序结果为height = [1, 2, 2, 3, 3, 6]，weight = [2,5,3,7,6,10]height=[1,2,2,3,3,6]，weight=[2,5,3,7,6,10]，可以看到体重的最长递增子序列结果是 44

作者：mo-ran-40
链接：https://leetcode-cn.com/problems/circus-tower-lcci/solution/dong-tai-gui-hua-zui-chang-di-zeng-zi-xu-lie-by-mo/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



方法二：贪心 + 二分查找
思路与算法

考虑一个简单的贪心，如果我们要使上升子序列尽可能的长，则我们需要让序列上升得尽可能慢，因此我们希望每次在上升子序列最后加上的那个数尽可能的小。

基于上面的贪心思路，我们维护一个数组 d[i]d[i] ，表示长度为 ii 的最长上升子序列的末尾元素的最小值，用 \textit{len}len 记录目前最长上升子序列的长度，起始时 lenlen 为 11，d[1] = \textit{nums}[0]d[1]=nums[0]。

同时我们可以注意到 d[i]d[i] 是关于 ii 单调递增的。因为如果 d[j] \geq d[i]d[j]≥d[i] 且 j < ij<i，我们考虑从长度为 ii 的最长上升子序列的末尾删除 i-ji−j 个元素，那么这个序列长度变为 jj ，且第 jj 个元素 xx（末尾元素）必然小于 d[i]d[i]，也就小于 d[j]d[j]。那么我们就找到了一个长度为 jj 的最长上升子序列，并且末尾元素比 d[j]d[j] 小，从而产生了矛盾。因此数组 d[]d[] 的单调性得证。

我们依次遍历数组 \textit{nums}[]nums[] 中的每个元素，并更新数组 d[]d[] 和 lenlen 的值。如果 \textit{nums}[i] > d[\textit{len}]nums[i]>d[len] 则更新 len = len + 1len=len+1，否则在 d[1 \ldots len]d[1…len]中找满足 d[i - 1] < \textit{nums}[j] < d[i]d[i−1]<nums[j]<d[i] 的下标 ii，并更新 d[i] = \textit{nums}[j]d[i]=nums[j]。

根据 dd 数组的单调性，我们可以使用二分查找寻找下标 ii，优化时间复杂度。

最后整个算法流程为：

设当前已求出的最长上升子序列的长度为 \textit{len}len（初始时为 11），从前往后遍历数组 \textit{nums}nums，在遍历到 \textit{nums}[i]nums[i] 时：

如果 \textit{nums}[i] > d[\textit{len}]nums[i]>d[len] ，则直接加入到 dd 数组末尾，并更新 \textit{len} = \textit{len} + 1len=len+1；

否则，在 dd 数组中二分查找，找到第一个比 \textit{nums}[i]nums[i] 小的数 d[k]d[k] ，并更新 d[k + 1] = \textit{nums}[i]d[k+1]=nums[i]。

以输入序列 [0, 8, 4, 12, 2][0,8,4,12,2] 为例：

第一步插入 00，d = [0]d=[0]；

第二步插入 88，d = [0, 8]d=[0,8]；

第三步插入 44，d = [0, 4]d=[0,4]；

第四步插入 1212，d = [0, 4, 12]d=[0,4,12]；

第五步插入 22，d = [0, 2, 12]d=[0,2,12]。

最终得到最大递增子序列长度为 33。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
### code
```py
class Solution(object):
    def bestSeqAtIndex(self, height, weight):
        """
        :type height: List[int]
        :type weight: List[int]
        :rtype: int
        """
        import bisect
        length = len(height)
        if length <= 1: return length
        sorted_index = sorted(list(range(length)), key=lambda i:(height[i],-weight[i]))
        dp = [0]
        dp[0] = weight[sorted_index[0]]
        for j in range(1,length):
            w_j = weight[sorted_index[j]]
            if dp[-1] < w_j:
                dp.append(w_j)
            else:
                new_index = bisect.bisect_left(dp,w_j)
                dp[new_index] = w_j
        return len(dp)
```


