# 一个方法团灭 LeetCode 打家劫舍问题



![](https://labuladong.online/algo/images/souyisou1.png)

**通知：为满足广大读者的需求，网站上架 [速成目录](https://labuladong.online/algo/intro/quick-learning-plan/)，如有需要可以看下，谢谢大家的支持~另外，建议你在我的 [网站](https://labuladong.online/algo/) 学习文章，体验更好。**



读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| :----: | :----: | :----: |
| [198. House Robber](https://leetcode.com/problems/house-robber/) | [198. 打家劫舍](https://leetcode.cn/problems/house-robber/) | 🟠 |
| [213. House Robber II](https://leetcode.com/problems/house-robber-ii/) | [213. 打家劫舍 II](https://leetcode.cn/problems/house-robber-ii/) | 🟠 |
| [337. House Robber III](https://leetcode.com/problems/house-robber-iii/) | [337. 打家劫舍 III](https://leetcode.cn/problems/house-robber-iii/) | 🟠 |

**-----------**



> [!NOTE]
> 阅读本文前，你需要先学习：
> 
> - [二叉树系列算法（纲领篇）](https://labuladong.online/algo/essential-technique/binary-tree-summary/)
> - [动态规划核心框架](https://labuladong.online/algo/essential-technique/dynamic-programming-framework/)

今天来讲「打家劫舍」系列问题（英文版叫 House Robber），这个系列是比较有代表性和技巧性的动态规划题目。

打家劫舍系列总共有三道，难度设计比较合理，层层递进。第一道是比较标准的动态规划问题，而第二道融入了环形数组的条件，第三道更绝，把动态规划的自底向上和自顶向下解法和二叉树结合起来，我认为很有启发性。

下面，我们从第一道开始分析。

## 打家劫舍 I

力扣第 198 题「打家劫舍」的题目如下：

街上有一排房屋，用一个包含非负整数的数组 `nums` 表示，每个元素 `nums[i]` 代表第 `i` 间房子中的现金数额。现在你是一名专业盗贼，你希望**尽可能多**的盗窃这些房子中的现金，但是，**相邻的房子不能被同时盗窃**，否则会触发报警器，你就凉凉了。

请你写一个算法，计算在不触动报警器的前提下，最多能够盗窃多少现金呢？函数签名如下：

```java
int rob(int[] nums);
```

比如说输入 `nums=[2,1,7,9,3,1]`，算法返回 12，小偷可以盗窃 `nums[0], nums[3], nums[5]` 三个房屋，得到的现金之和为 2 + 9 + 1 = 12，是最优的选择。

题目很容易理解，而且动态规划的特征很明显。我们前文 [动态规划详解](https://labuladong.online/algo/essential-technique/dynamic-programming-framework/) 做过总结，**解决动态规划问题就是找「状态」和「选择」，仅此而已**。







假想你就是这个专业强盗，从左到右走过这一排房子，在每间房子前都有两种**选择**：抢或者不抢。

如果你抢了这间房子，那么你**肯定**不能抢相邻的下一间房子了，只能从下下间房子开始做选择。

如果你不抢这件房子，那么你可以走到下一间房子前，继续做选择。

当你走过了最后一间房子后，你就没得抢了，能抢到的钱显然是 0（**base case**）。

以上的逻辑很简单吧，其实已经明确了「状态」和「选择」：**你面前房子的索引就是状态，抢和不抢就是选择**。

![](https://labuladong.online/algo/images/robber/1.jpg)

在两个选择中，每次都选更大的结果，最后得到的就是最多能抢到的 money：

```java
class Solution {
    // 主函数
    public int rob(int[] nums) {
        return dp(nums, 0);
    }

    // 定义：返回 nums[start..] 能抢到的最大值
    private int dp(int[] nums, int start) {
        if (start >= nums.length) {
            return 0;
        }
        
        int res = Math.max(
                // 不抢，去下家
                dp(nums, start + 1), 
                // 抢，去下下家
                nums[start] + dp(nums, start + 2)
            );
        return res;
    }
}
```

明确了状态转移，就可以发现对于同一 `start` 位置，是存在重叠子问题的，比如下图：

![](https://labuladong.online/algo/images/robber/2.jpg)

盗贼有多种选择可以走到这个位置，如果每次到这都进入递归，岂不是浪费时间？所以说存在重叠子问题，可以用备忘录进行优化：

```java
class Solution {

    private int[] memo;
    // 主函数
    public int rob(int[] nums) {
        // 初始化备忘录
        memo = new int[nums.length];
        Arrays.fill(memo, -1);
        // 强盗从第 0 间房子开始抢劫
        return dp(nums, 0);
    }

    // 定义：返回 dp[start..] 能抢到的最大值
    private int dp(int[] nums, int start) {
        if (start >= nums.length) {
            return 0;
        }
        // 避免重复计算
        if (memo[start] != -1) return memo[start];
        
        int res = Math.max(
            dp(nums, start + 1), 
            dp(nums, start + 2) + nums[start]
        );
        // 记入备忘录
        memo[start] = res;
        return res;
    }
}
```


<hr/>
<a href="https://labuladong.online/algo-visualize/leetcode/house-robber/" target="_blank">
<details style="max-width:90%;max-height:400px">
<summary>
<strong>🎃 代码可视化动画🎃</strong>
</summary>
</details>
</a>
<hr/>



这就是自顶向下的动态规划解法，我们也可以略作修改，写出**自底向上**的解法：

```java
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        // dp[i] = x 表示：
        // 从第 i 间房子开始抢劫，最多能抢到的钱为 x
        // base case: dp[n] = 0
        int[] dp = new int[n + 2];
        for (int i = n - 1; i >= 0; i--) {
            dp[i] = Math.max(dp[i + 1], nums[i] + dp[i + 2]);
        }
        return dp[0];
    }
}
```

我们又发现状态转移只和 `dp[i]` 最近的两个状态有关，所以可以进一步优化，将空间复杂度降低到 O(1)。

```java
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        // 记录 dp[i+1] 和 dp[i+2]
        int dp_i_1 = 0, dp_i_2 = 0;
        // 记录 dp[i]
        int dp_i = 0; 
        for (int i = n - 1; i >= 0; i--) {
            dp_i = Math.max(dp_i_1, nums[i] + dp_i_2);
            dp_i_2 = dp_i_1;
            dp_i_1 = dp_i;
        }
        return dp_i;
    }
}
```

以上的流程，在我们 [动态规划详解](https://labuladong.online/algo/essential-technique/dynamic-programming-framework/) 中详细解释过，相信大家都能手到擒来了。我认为很有意思的是这个问题的 follow up，需要基于我们现在的思路做一些巧妙的应变。

## 打家劫舍 II

力扣第 213 题「打家劫舍 II」和上一道题描述基本一样，强盗依然不能抢劫相邻的房子，输入依然是一个数组，但是告诉你**这些房子不是一排，而是围成了一个圈**。

也就是说，现在第一间房子和最后一间房子也相当于是相邻的，不能同时抢。比如说输入数组 `nums=[2,3,2]`，算法返回的结果应该是 3 而不是 4，因为开头和结尾不能同时被抢。

这个约束条件看起来应该不难解决，我们前文 [单调栈问题汇总](https://labuladong.online/algo/data-structure/monotonic-stack/) 说过一种解决环形数组的方案，那么在这个问题上怎么处理呢？

首先，首尾房间不能同时被抢，那么只可能有三种不同情况：要么都不被抢；要么第一间房子被抢最后一间不抢；要么最后一间房子被抢第一间不抢。

![](https://labuladong.online/algo/images/robber/3.jpg)

那就简单了啊，这三种情况，哪种的结果最大，就是最终答案呗！不过，其实我们不需要比较三种情况，只要比较情况二和情况三就行了，**因为这两种情况对于房子的选择余地比情况一大呀，房子里的钱数都是非负数，所以选择余地大，最优决策结果肯定不会小**。

所以只需对之前的解法稍作修改即可：

```java
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        return Math.max(robRange(nums, 0, n - 2), 
                        robRange(nums, 1, n - 1));
    }

    // 定义：返回闭区间 [start,end] 能抢到的最大值
    int robRange(int[] nums, int start, int end) {
        int n = nums.length;
        int dp_i_1 = 0, dp_i_2 = 0;
        int dp_i = 0;
        for (int i = end; i >= start; i--) {
            dp_i = Math.max(dp_i_1, nums[i] + dp_i_2);
            dp_i_2 = dp_i_1;
            dp_i_1 = dp_i;
        }
        return dp_i;
    }
}
```

至此，第二问也解决了。

## 打家劫舍 III

力扣第 337 题「打家劫舍 III」又想法设法地变花样了，此强盗发现现在面对的房子不是一排，不是一圈，而是一棵二叉树！房子在二叉树的节点上，相连的两个房子不能同时被抢劫，果然是传说中的高智商犯罪。函数的签名如下：

```java
int rob(TreeNode root);
```

比如说输入为下图这样一棵二叉树：

```
     3
    / \
   2   3
    \   \ 
     3   1
```

算法应该返回 7，因为抢劫第一层和第三层的房子可以得到最高金额 3 + 3 + 1 = 7。

如果输入为下图这棵二叉树：

```
     3
    / \
   4   5
  / \   \ 
 1   3   1
```

那么算法应该返回 9，如果抢劫第二层的房子可以获得最高金额 4 + 5 = 9。

整体的思路完全没变，还是做抢或者不抢的选择，去收益较大的选择。甚至我们可以直接按这个套路写出代码：

```java
class Solution {
    Map<TreeNode, Integer> memo = new HashMap<>();
    public int rob(TreeNode root) {
        if (root == null) return 0;
        // 利用备忘录消除重叠子问题
        if (memo.containsKey(root)) 
            return memo.get(root);
        // 抢，然后去下下家
        int do_it = root.val
            + (root.left == null ? 
                0 : rob(root.left.left) + rob(root.left.right))
            + (root.right == null ? 
                0 : rob(root.right.left) + rob(root.right.right));
        // 不抢，然后去下家
        int not_do = rob(root.left) + rob(root.right);
        
        int res = Math.max(do_it, not_do);
        memo.put(root, res);
        return res;
    }
}
```


<hr/>
<a href="https://labuladong.online/algo-visualize/leetcode/house-robber-iii/" target="_blank">
<details style="max-width:90%;max-height:400px">
<summary>
<strong>👾 代码可视化动画👾</strong>
</summary>
</details>
</a>
<hr/>



分析下时间复杂度，虽然看这个递归结构似乎是一棵四叉树，但实际上由于备忘录的优化，递归函数做的事情就是还是遍历每个节点，不会多次进入同一个节点，所以时间复杂度是还是 $O(N)$，`N` 为树的节点数。空间复杂度是备忘录的大小，即 $O(N)$。

如果对时间/空间复杂度分析有困惑，可以参考 [时空复杂度分析实用指南](https://labuladong.online/algo/essential-technique/complexity-analysis/)。

但是这道题巧妙的点在于，还有更漂亮的解法。比如一个读者评论了这样一个解法：

```java
class Solution {
    int rob(TreeNode root) {
        int[] res = dp(root);
        return Math.max(res[0], res[1]);
    }

    // 返回一个大小为 2 的数组 arr
    // arr[0] 表示不抢 root 的话，得到的最大钱数
    // arr[1] 表示抢 root 的话，得到的最大钱数
    int[] dp(TreeNode root) {
        if (root == null)
            return new int[]{0, 0};
        int[] left = dp(root.left);
        int[] right = dp(root.right);
        // 抢，下家就不能抢了
        int rob = root.val + left[0] + right[0];
        // 不抢，下家可抢可不抢，取决于收益大小
        int not_rob = Math.max(left[0], left[1])
                    + Math.max(right[0], right[1]);
        
        return new int[]{not_rob, rob};
    }
}
```

时间复杂度还是 $O(N)$，空间复杂度只有递归函数堆栈所需的空间，即树的高度 $O(H)$，不需要备忘录的额外空间。

你看他和我们的思路不一样，修改了递归函数的定义，略微修改了思路，使得逻辑自洽，依然得到了正确的答案，而且代码更漂亮。这就是我们前文 [二叉树思维（纲领篇）](https://labuladong.online/algo/essential-technique/binary-tree-summary/) 中讲到的后序位置的妙用。

实际上，这个解法比我们的解法运行时间要快得多，虽然算法分析层面时间复杂度是相同的。原因在于此解法没有使用额外的备忘录，减少了数据操作的复杂性，所以实际运行效率会快。








<hr>
<details class="hint-container details">
<summary><strong>引用本文的题目</strong></summary>

<strong>安装 [我的 Chrome 刷题插件](https://labuladong.online/algo/intro/chrome/) 点开下列题目可直接查看解题思路：</strong>

| LeetCode | 力扣 | 难度 |
| :----: | :----: | :----: |
| - | [剑指 Offer II 089. 房屋偷盗](https://leetcode.cn/problems/Gu0c2T/?show=1) | 🟠 |
| - | [剑指 Offer II 090. 环形房屋偷盗](https://leetcode.cn/problems/PzWKhm/?show=1) | 🟠 |

</details>
<hr>



**＿＿＿＿＿＿＿＿＿＿＿＿＿**



![](https://labuladong.online/algo/images/souyisou2.png)