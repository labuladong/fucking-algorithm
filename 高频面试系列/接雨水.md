# 如何高效解决接雨水问题



![](https://labuladong.online/algo/images/souyisou1.png)

**通知：为满足广大读者的需求，网站上架 [速成目录](https://labuladong.online/algo/intro/quick-learning-plan/)，如有需要可以看下，谢谢大家的支持~另外，建议你在我的 [网站](https://labuladong.online/algo/) 学习文章，体验更好。**



读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| :----: | :----: | :----: |
| [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | [11. 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/) | 🟠 |
| [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | [42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/) | 🔴 |

**-----------**




> [!NOTE]
> 阅读本文前，你需要先学习：
> 
> - [数组双指针技巧汇总](https://labuladong.online/algo/essential-technique/array-two-pointers-summary/)

力扣第 42 题「接雨水」挺有意思，在面试题中出现频率还挺高的，本文就来步步优化，讲解一下这道题。

先看一下题目：

<Problem slug="trapping-rain-water" />

就是用一个数组表示一个条形图，问你这个条形图最多能接多少水。

```java
int trap(int[] height);
```

下面就来由浅入深介绍暴力解法 -> 备忘录解法 -> 双指针解法，在 O(N) 时间 O(1) 空间内解决这个问题。

## 一、核心思路

> [!TIP]
> 做算法题，如果对题目提出的问题没有思路，不妨尝试化简问题，先从局部思考，先写出最简单粗暴的解法，也许会有突破点。逐步优化后也许就能找到最优解。

比如这道题，先不考虑整个柱状图能装多少水，仅仅考虑位置 `i` 这一个位置能装下多少水？

![](https://labuladong.online/algo/images/rain-water/0.jpg)

能装 2 格水，因为 `height[i]` 的高度为 0，而这里最多能盛 2 格水，2-0=2。

为什么位置 `i` 最多能盛 2 格水呢？因为，位置 `i` 能达到的水柱高度和其左边的最高柱子、右边的最高柱子有关，我们分别称这两个柱子高度为 `l_max` 和 `r_max`；**位置 `i` 最大的水柱高度就是 `min(l_max, r_max)`**。

也就是说，对于位置 `i`，能够装的水为：





```python
water[i] = min(
    # 左边最高的柱子
    max(height[0..i]),  
    # 右边最高的柱子
    max(height[i..end]) 
) - height[i]
```

![](https://labuladong.online/algo/images/rain-water/1.jpg)

![](https://labuladong.online/algo/images/rain-water/2.jpg)



这就是本问题的核心思路，我们可以简单写一个暴力算法：

```java
class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int res = 0;
        for (int i = 1; i < n - 1; i++) {
            int l_max = 0, r_max = 0;
            // 找右边最高的柱子
            for (int j = i; j < n; j++)
                r_max = Math.max(r_max, height[j]);
            // 找左边最高的柱子
            for (int j = i; j >= 0; j--)
                l_max = Math.max(l_max, height[j]);
            // 如果自己就是最高的话，
            // l_max == r_max == height[i]
            res += Math.min(l_max, r_max) - height[i];
        }
        return res;
    }
}
```

这个解法应该是很直接粗暴的，时间复杂度 O(N^2)，空间复杂度 O(1)。但是很明显这种计算 `r_max` 和 `l_max` 的方式非常笨拙，每次都要用 for 循环去遍历，我们是不是可以优化一下这个过程？

## 二、备忘录优化

之前的暴力解法，不是在每个位置 `i` 都要计算 `r_max` 和 `l_max` 吗？我们直接把结果都提前计算出来，别傻不拉几的每次都遍历，这时间复杂度不就降下来了嘛。

**我们开两个数组 `r_max` 和 `l_max` 充当备忘录，`l_max[i]` 表示位置 `i` 左边最高的柱子高度，`r_max[i]` 表示位置 `i` 右边最高的柱子高度**。预先把这两个数组计算好，避免重复计算：

```java
class Solution {
    public int trap(int[] height) {
        if (height.length == 0) {
            return 0;
        }
        int n = height.length;
        int res = 0;
        // 数组充当备忘录
        int[] l_max = new int[n];
        int[] r_max = new int[n];
        // 初始化 base case
        l_max[0] = height[0];
        r_max[n - 1] = height[n - 1];
        // 从左向右计算 l_max
        for (int i = 1; i < n; i++)
            l_max[i] = Math.max(height[i], l_max[i - 1]);
        // 从右向左计算 r_max
        for (int i = n - 2; i >= 0; i--)
            r_max[i] = Math.max(height[i], r_max[i + 1]);
        // 计算答案
        for (int i = 1; i < n - 1; i++)
            res += Math.min(l_max[i], r_max[i]) - height[i];
        return res;
    }
}
```


<hr/>
<a href="https://labuladong.online/algo-visualize/leetcode/trapping-rain-water/" target="_blank">
<details style="max-width:90%;max-height:400px">
<summary>
<strong>🎃 代码可视化动画🎃</strong>
</summary>
</details>
</a>
<hr/>



这个优化其实和暴力解法思路差不多，就是避免了重复计算，把时间复杂度降低为 O(N)，已经是最优了，但是空间复杂度是 O(N)。下面来看一个精妙一些的解法，能够把空间复杂度降低到 O(1)。

## 三、双指针解法

> [!NOTE]
> 这个解法作为思路拓展，看看就好，不必过于执着最优解。因为对于大部分人，在真实的面试/笔试中，能够使用朴实无华的方法见招拆招，写出上面的解法就可以了。虽然多了一些空间复杂度，但一般判题平台还是能过的。
> 
> 除非过不了所有测试用例，且你写完了其他题目还有富余的时间，再花时间针对上面的解法进行优化也不迟。

这种解法的思路是完全相同的，但在实现手法上非常巧妙，我们这次也不要用备忘录提前计算了，而是用双指针**边走边算**，节省下空间复杂度。

首先，看一部分代码：

```java
int trap(int[] height) {
    int left = 0, right = height.length - 1;
    int l_max = 0, r_max = 0;
    
    while (left < right) {
        l_max = Math.max(l_max, height[left]);
        r_max = Math.max(r_max, height[right]);
        // 此时 l_max 和 r_max 分别表示什么？
        left++; right--;
    }
}
```

对于这部分代码，请问 `l_max` 和 `r_max` 分别表示什么意义呢？

很容易理解，**`l_max` 是 `height[0..left]` 中最高柱子的高度，`r_max` 是 `height[right..end]` 的最高柱子的高度**。

明白了这一点，直接看解法：

```java
class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int l_max = 0, r_max = 0;

        int res = 0;
        while (left < right) {
            l_max = Math.max(l_max, height[left]);
            r_max = Math.max(r_max, height[right]);

            // res += min(l_max, r_max) - height[i]
            if (l_max < r_max) {
                res += l_max - height[left];
                left++;
            } else {
                res += r_max - height[right];
                right--;
            }
        }
        return res;
    }
}
```

你看，其中的核心思想和之前一模一样，换汤不换药。但是细心的读者可能会发现次解法还是有点细节差异：

之前的备忘录解法，`l_max[i]` 和 `r_max[i]` 分别代表 `height[0..i]` 和 `height[i..end]` 的最高柱子高度。

```java
res += Math.min(l_max[i], r_max[i]) - height[i];
```

![](https://labuladong.online/algo/images/rain-water/3.jpg)

但是双指针解法中，`l_max` 和 `r_max` 代表的是 `height[0..left]` 和 `height[right..end]` 的最高柱子高度。比如这段代码：

```java
if (l_max < r_max) {
    res += l_max - height[left];
    left++; 
} 
```

![](https://labuladong.online/algo/images/rain-water/4.jpg)

此时的 `l_max` 是 `left` 指针左边的最高柱子，但是 `r_max` 并不一定是 `left` 指针右边最高的柱子，这真的可以得到正确答案吗？

其实这个问题要这么思考，我们只在乎 `min(l_max, r_max)`。**对于上图的情况，我们已经知道 `l_max < r_max` 了，至于这个 `r_max` 是不是右边最大的，不重要。重要的是 `height[i]` 能够装的水只和较低的 `l_max` 之差有关**：

![](https://labuladong.online/algo/images/rain-water/5.jpg)

这样，接雨水问题就解决了。

## 扩展：盛最多水的容器

下面我们看一道和接雨水问题非常类似的题目，力扣第 11 题「盛最多水的容器」：





<Problem slug="container-with-most-water" />

```java
// 函数签名如下
int maxArea(int[] height);
```

这题和接雨水问题很类似，可以完全套用前文的思路，而且还更简单。两道题的区别在于：

**接雨水问题给出的类似一幅直方图，每个横坐标都有宽度，而本题给出的每个横坐标是一条竖线，没有宽度**。

我们前文讨论了半天 `l_max` 和 `r_max`，实际上都是为了计算 `height[i]` 能够装多少水；而本题中 `height[i]` 没有了宽度，那自然就好办多了。

举个例子，如果在接雨水问题中，你知道了 `height[left]` 和 `height[right]` 的高度，你能算出 `left` 和 `right` 之间能够盛下多少水吗？

不能，因为你不知道 `left` 和 `right` 之间每个柱子具体能盛多少水，你得通过每个柱子的 `l_max` 和 `r_max` 来计算才行。

反过来，就本题而言，你知道了 `height[left]` 和 `height[right]` 的高度，能算出 `left` 和 `right` 之间能够盛下多少水吗？

可以，因为本题中竖线没有宽度，所以 `left` 和 `right` 之间能够盛的水就是：

```python
min(height[left], height[right]) * (right - left)
```

类似接雨水问题，高度是由 `height[left]` 和 `height[right]` 较小的值决定的。

解决这道题的思路依然是双指针技巧：

**用 `left` 和 `right` 两个指针从两端向中心收缩，一边收缩一边计算 `[left, right]` 之间的矩形面积，取最大的面积值即是答案**。

先直接看解法代码吧：

```java
class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int res = 0;
        while (left < right) {
            // [left, right] 之间的矩形面积
            int cur_area = Math.min(height[left], height[right]) * (right - left);
            res = Math.max(res, cur_area);
            // 双指针技巧，移动较低的一边
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return res;
    }
}
```


<hr/>
<a href="https://labuladong.online/algo-visualize/leetcode/container-with-most-water/" target="_blank">
<details style="max-width:90%;max-height:400px">
<summary>
<strong>🎃 代码可视化动画🎃</strong>
</summary>
</details>
</a>
<hr/>



代码和接雨水问题大致相同，不过肯定有读者会问，下面这段 if 语句为什么要移动较低的一边：





```java
// 双指针技巧，移动较低的一边
if (height[left] < height[right]) {
    left++;
} else {
    right--;
}
```



**其实也好理解，因为矩形的高度是由 `min(height[left], height[right])` 即较低的一边决定的**：

你如果移动较低的那一边，那条边可能会变高，使得矩形的高度变大，进而就「有可能」使得矩形的面积变大；相反，如果你去移动较高的那一边，矩形的高度是无论如何都不会变大的，所以不可能使矩形的面积变得更大。

至此，这道题也解决了。









**＿＿＿＿＿＿＿＿＿＿＿＿＿**



![](https://labuladong.online/algo/images/souyisou2.png)