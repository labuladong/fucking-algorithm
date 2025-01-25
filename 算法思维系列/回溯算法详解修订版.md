# 回溯算法解题套路框架



![](https://labuladong.online/algo/images/souyisou1.png)

**通知：为满足广大读者的需求，网站上架 [速成目录](https://labuladong.online/algo/intro/quick-learning-plan/)，如有需要可以看下，谢谢大家的支持~另外，建议你在我的 [网站](https://labuladong.online/algo/) 学习文章，体验更好。**



读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| :----: | :----: | :----: |
| [46. Permutations](https://leetcode.com/problems/permutations/) | [46. 全排列](https://leetcode.cn/problems/permutations/) | 🟠 |

**-----------**



> [!NOTE]
> 阅读本文前，你需要先学习：
> 
> - [二叉树结构基础](https://labuladong.online/algo/data-structure-basic/binary-tree-basic/)
> - [二叉树的遍历框架](https://labuladong.online/algo/data-structure-basic/binary-tree-traverse-basic/)
> - [多叉树结构及遍历框架](https://labuladong.online/algo/data-structure-basic/n-ary-tree-traverse-basic/)

> tip：本文有视频版：[回溯算法框架套路详解](https://www.bilibili.com/video/BV1P5411N7Xc/)。建议关注我的 B 站账号，我会用视频领读的方式带大家学习那些稍有难度的算法技巧。



这篇文章是很久之前的一篇 [回溯算法详解](https://mp.weixin.qq.com/s/trILKSiN9EoS58pXmvUtUQ) 的进阶版。把框架给你讲清楚，你会发现回溯算法问题都是一个套路。

本文解决几个问题：

回溯算法是什么？解决回溯算法相关的问题有什么技巧？如何学习回溯算法？回溯算法代码是否有规律可循？

其实回溯算法和我们常说的 DFS 算法基本可以认为是同一种算法，它们的细微差异我在 [关于 DFS 和回溯算法的若干问题](https://labuladong.online/algo/essential-technique/backtrack-vs-dfs/) 中有详细解释，本文聚焦回溯算法，不展开。

**抽象地说，解决一个回溯问题，实际上就是遍历一棵决策树的过程，树的每个叶子节点存放着一个合法答案。你把整棵树遍历一遍，把叶子节点上的答案都收集起来，就能得到所有的合法答案**。

站在回溯树的一个节点上，你只需要思考 3 个问题：

1、路径：也就是已经做出的选择。

2、选择列表：也就是你当前可以做的选择。

3、结束条件：也就是到达决策树底层，无法再做选择的条件。

如果你不理解这三个词语的解释，没关系，我们后面会用「全排列」这个经典的回溯算法问题来帮你理解这些词语是什么意思，现在你先留着印象。

代码方面，回溯算法的框架：

```python
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```







**其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」**，特别简单。

什么叫做选择和撤销选择呢，这个框架的底层原理是什么呢？下面我们就通过「全排列」这个问题来解开之前的疑惑，详细探究一下其中的奥妙！

## 全排列问题解析

力扣第 46 题「全排列」就是给你输入一个数组 `nums`，让你返回这些数字的全排列。

> [!NOTE]
> **我们这次讨论的全排列问题不包含重复的数字，包含重复数字的扩展场景我在后文 [回溯算法秒杀排列组合子集的九种题型](https://labuladong.online/algo/essential-technique/permutation-combination-subset-all-in-one/) 中讲解**。
> 
> 另外，有些读者之前看过的全排列算法代码可能是那种 `swap` 交换元素的写法，和我在本文介绍的代码不同。这是回溯算法两种穷举思路，我会在后文 [球盒模型：回溯算法穷举的两种视角](https://labuladong.online/algo/practice-in-action/two-views-of-backtrack/) 讲明白。现在还不适合直接跟你讲那个解法，你照着我的思路学习即可。

我们在高中的时候就做过排列组合的数学题，我们也知道 `n` 个不重复的数，全排列共有 `n!` 个。那么我们当时是怎么穷举全排列的呢？

比方说给三个数 `[1,2,3]`，你肯定不会无规律地乱穷举，一般是这样：

先固定第一位为 1，然后第二位可以是 2，那么第三位只能是 3；然后可以把第二位变成 3，第三位就只能是 2 了；然后就只能变化第一位，变成 2，然后再穷举后两位……

其实这就是回溯算法，我们高中无师自通就会用，或者有的同学直接画出如下这棵回溯树：

![](https://labuladong.online/algo/images/backtracking/1.jpg)

只要从根遍历这棵树，记录路径上的数字，其实就是所有的全排列。**我们不妨把这棵树称为回溯算法的「决策树」**。

**为啥说这是决策树呢，因为你在每个节点上其实都在做决策**。比如说你站在下图的红色节点上：

![](https://labuladong.online/algo/images/backtracking/2.jpg)

你现在就在做决策，可以选择 1 那条树枝，也可以选择 3 那条树枝。为啥只能在 1 和 3 之中选择呢？因为 2 这个树枝在你身后，这个选择你之前做过了，而全排列是不允许重复使用数字的。

**现在可以解答开头的几个名词：`[2]` 就是「路径」，记录你已经做过的选择；`[1,3]` 就是「选择列表」，表示你当前可以做出的选择；「结束条件」就是遍历到树的底层叶子节点，这里也就是选择列表为空的时候**。

如果明白了这几个名词，可以把「路径」和「选择」列表作为决策树上每个节点的属性，比如下图列出了几个蓝色节点的属性：

![](https://labuladong.online/algo/images/backtracking/3.jpg)

**我们定义的 `backtrack` 函数其实就像一个指针，在这棵树上游走，同时要正确维护每个节点的属性，每当走到树的底层叶子节点，其「路径」就是一个全排列**。

再进一步，如何遍历一棵树？这个应该不难吧。回忆一下之前 [学习数据结构的框架思维](https://labuladong.online/algo/essential-technique/algorithm-summary/) 写过，各种搜索问题其实都是树的遍历问题，而多叉树的遍历框架就是这样：

```java
void traverse(TreeNode root) {
    for (TreeNode child : root.childern) {
        // 前序位置需要的操作
        traverse(child);
        // 后序位置需要的操作
    }
}
```

> [!NOTE]
> 细心的读者肯定会疑问：多叉树 DFS 遍历框架的前序位置和后序位置应该在 for 循环外面，并不应该是在 for 循环里面呀？为什么在回溯算法中跑到 for 循环里面了？
> 
> 是的，DFS 算法的前序和后序位置应该在 for 循环外面，不过回溯算法和 DFS 算法略有不同，[解答回溯/DFS 算法的若干疑问](https://labuladong.online/algo/essential-technique/backtrack-vs-dfs/) 会具体讲解，这里可以暂且忽略这个问题。

而所谓的前序遍历和后序遍历，他们只是两个很有用的时间点，我给你画张图你就明白了：

![](https://labuladong.online/algo/images/backtracking/4.jpg)

**前序遍历的代码在进入某一个节点之前的那个时间点执行，后序遍历代码在离开某个节点之后的那个时间点执行**。

回想我们刚才说的，「路径」和「选择」是每个节点的属性，函数在树上游走要正确处理节点的属性，那么就要在这两个特殊时间点搞点动作：

![](https://labuladong.online/algo/images/backtracking/5.jpg)

现在，你是否理解了回溯算法的这段核心框架？

```python
for 选择 in 选择列表:
    # 做选择
    将该选择从选择列表移除
    路径.add(选择)
    backtrack(路径, 选择列表)
    # 撤销选择
    路径.remove(选择)
    将该选择再加入选择列表
```

**我们只要在递归之前做出选择，在递归之后撤销刚才的选择**，就能正确得到每个节点的选择列表和路径。

下面，直接看全排列代码：

```java
class Solution {
    List<List<Integer>> res = new LinkedList<>();

    // 主函数，输入一组不重复的数字，返回它们的全排列
    List<List<Integer>> permute(int[] nums) {
        // 记录「路径」
        LinkedList<Integer> track = new LinkedList<>();
        // 「路径」中的元素会被标记为 true，避免重复使用
        boolean[] used = new boolean[nums.length];
        
        backtrack(nums, track, used);
        return res;
    }

    // 路径：记录在 track 中
    // 选择列表：nums 中不存在于 track 的那些元素（used[i] 为 false）
    // 结束条件：nums 中的元素全都在 track 中出现
    void backtrack(int[] nums, LinkedList<Integer> track, boolean[] used) {
        // 触发结束条件
        if (track.size() == nums.length) {
            res.add(new LinkedList(track));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            // 排除不合法的选择
            if (used[i]) {
                // nums[i] 已经在 track 中，跳过
                continue;
            }
            // 做选择
            track.add(nums[i]);
            used[i] = true;
            // 进入下一层决策树
            backtrack(nums, track, used);
            // 取消选择
            track.removeLast();
            used[i] = false;
        }
    }
}
```


<hr/>
<a href="https://labuladong.online/algo-visualize/leetcode/permutations/" target="_blank">
<details style="max-width:90%;max-height:400px">
<summary>
<strong>🌈 代码可视化动画🌈</strong>
</summary>
</details>
</a>
<hr/>



我们这里稍微做了些变通，没有显式记录「选择列表」，而是通过 `used` 数组排除已经存在 `track` 中的元素，从而推导出当前的选择列表：

![](https://labuladong.online/algo/images/backtracking/6.jpg)

至此，我们就通过全排列问题详解了回溯算法的底层原理。当然，这个算法解决全排列不是最高效的，你可能看到有的解法连 `used` 数组都不使用，通过交换元素达到目的。但是那种解法稍微难理解一些，我会在 [球盒模型：回溯算法两种穷举视角](https://labuladong.online/algo/practice-in-action/two-views-of-backtrack/) 中介绍。

但是必须说明的是，不管怎么优化，都符合回溯框架，而且时间复杂度都不可能低于 O(N!)，因为穷举整棵决策树是无法避免的，你最后肯定要穷举出 N! 种全排列结果。

**这也是回溯算法的一个特点，不像动态规划存在重叠子问题可以优化，回溯算法就是纯暴力穷举，复杂度一般都很高**。

## 最后总结

回溯算法就是个多叉树的遍历问题，关键就是在前序遍历和后序遍历的位置做一些操作，算法框架如下：

```python
def backtrack(...):
    for 选择 in 选择列表:
        做选择
        backtrack(...)
        撤销选择
```

**写 `backtrack` 函数时，需要维护走过的「路径」和当前可以做的「选择列表」，当触发「结束条件」时，将「路径」记入结果集**。

其实想想看，回溯算法和动态规划是不是有点像呢？我们在动态规划系列文章中多次强调，动态规划的三个需要明确的点就是「状态」「选择」和「base case」，是不是就对应着走过的「路径」，当前的「选择列表」和「结束条件」？

动态规划和回溯算法底层都把问题抽象成了树的结构，但这两种算法在思路上是完全不同的。在 [二叉树心法（纲领篇）](https://labuladong.online/algo/essential-technique/binary-tree-summary/) 你将看到动态规划和回溯算法更深层次的区别和联系。







<hr>
<details class="hint-container details">
<summary><strong>引用本文的文章</strong></summary>

 - [Trie/字典树/前缀树代码实现](https://labuladong.online/algo/data-structure/trie-implement/)
 - [base case 和备忘录的初始值怎么定？](https://labuladong.online/algo/dynamic-programming/memo-fundamental/)
 - [【强化练习】同时运用两种思维解题](https://labuladong.online/algo/problem-set/binary-tree-combine-two-view/)
 - [【强化练习】回溯算法经典习题 I](https://labuladong.online/algo/problem-set/backtrack-i/)
 - [【强化练习】回溯算法经典习题 II](https://labuladong.online/algo/problem-set/backtrack-ii/)
 - [【强化练习】回溯算法经典习题 III](https://labuladong.online/algo/problem-set/backtrack-iii/)
 - [一文秒杀所有岛屿题目](https://labuladong.online/algo/frequency-interview/island-dfs-summary/)
 - [二叉树基础及常见类型](https://labuladong.online/algo/data-structure-basic/binary-tree-basic/)
 - [二叉树系列算法核心纲领](https://labuladong.online/algo/essential-technique/binary-tree-summary/)
 - [分治算法解题套路框架](https://labuladong.online/algo/essential-technique/divide-and-conquer/)
 - [动态规划和回溯算法的思维转换](https://labuladong.online/algo/dynamic-programming/word-break/)
 - [回溯算法实践：括号生成](https://labuladong.online/algo/practice-in-action/generate-parentheses/)
 - [回溯算法实践：数独和 N 皇后问题](https://labuladong.online/algo/practice-in-action/sudoku-nqueue/)
 - [回溯算法实践：集合划分](https://labuladong.online/algo/practice-in-action/partition-to-k-equal-sum-subsets/)
 - [回溯算法秒杀所有排列/组合/子集问题](https://labuladong.online/algo/essential-technique/permutation-combination-subset-all-in-one/)
 - [学习数据结构和算法的框架思维](https://labuladong.online/algo/essential-technique/algorithm-summary/)
 - [球盒模型：回溯算法穷举的两种视角](https://labuladong.online/algo/practice-in-action/two-views-of-backtrack/)
 - [算法学习和心流体验](https://labuladong.online/algo/fname.html?fname=心流)
 - [算法时空复杂度分析实用指南](https://labuladong.online/algo/essential-technique/complexity-analysis/)
 - [算法笔试「骗分」套路](https://labuladong.online/algo/other-skills/tips-in-exam/)
 - [经典动态规划：戳气球](https://labuladong.online/algo/dynamic-programming/burst-balloons/)
 - [背包问题的变体：目标和](https://labuladong.online/algo/dynamic-programming/target-sum/)
 - [解答回溯算法/DFS算法的若干疑问](https://labuladong.online/algo/essential-technique/backtrack-vs-dfs/)

</details><hr>




<hr>
<details class="hint-container details">
<summary><strong>引用本文的题目</strong></summary>

<strong>安装 [我的 Chrome 刷题插件](https://labuladong.online/algo/intro/chrome/) 点开下列题目可直接查看解题思路：</strong>

| LeetCode | 力扣 | 难度 |
| :----: | :----: | :----: |
| [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/?show=1) | [111. 二叉树的最小深度](https://leetcode.cn/problems/minimum-depth-of-binary-tree/?show=1) | 🟢 |
| [112. Path Sum](https://leetcode.com/problems/path-sum/?show=1) | [112. 路径总和](https://leetcode.cn/problems/path-sum/?show=1) | 🟢 |
| [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/?show=1) | [113. 路径总和 II](https://leetcode.cn/problems/path-sum-ii/?show=1) | 🟠 |
| [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/?show=1) | [131. 分割回文串](https://leetcode.cn/problems/palindrome-partitioning/?show=1) | 🟠 |
| [140. Word Break II](https://leetcode.com/problems/word-break-ii/?show=1) | [140. 单词拆分 II](https://leetcode.cn/problems/word-break-ii/?show=1) | 🔴 |
| [1593. Split a String Into the Max Number of Unique Substrings](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/?show=1) | [1593. 拆分字符串使唯一子字符串的数目最大](https://leetcode.cn/problems/split-a-string-into-the-max-number-of-unique-substrings/?show=1) | 🟠 |
| [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/?show=1) | [17. 电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/?show=1) | 🟠 |
| [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/?show=1) | [22. 括号生成](https://leetcode.cn/problems/generate-parentheses/?show=1) | 🟠 |
| [301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/?show=1) | [301. 删除无效的括号](https://leetcode.cn/problems/remove-invalid-parentheses/?show=1) | 🔴 |
| [332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/?show=1) | [332. 重新安排行程](https://leetcode.cn/problems/reconstruct-itinerary/?show=1) | 🔴 |
| [39. Combination Sum](https://leetcode.com/problems/combination-sum/?show=1) | [39. 组合总和](https://leetcode.cn/problems/combination-sum/?show=1) | 🟠 |
| [51. N-Queens](https://leetcode.com/problems/n-queens/?show=1) | [51. N 皇后](https://leetcode.cn/problems/n-queens/?show=1) | 🔴 |
| [638. Shopping Offers](https://leetcode.com/problems/shopping-offers/?show=1) | [638. 大礼包](https://leetcode.cn/problems/shopping-offers/?show=1) | 🟠 |
| [698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/?show=1) | [698. 划分为k个相等的子集](https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/?show=1) | 🟠 |
| [77. Combinations](https://leetcode.com/problems/combinations/?show=1) | [77. 组合](https://leetcode.cn/problems/combinations/?show=1) | 🟠 |
| [78. Subsets](https://leetcode.com/problems/subsets/?show=1) | [78. 子集](https://leetcode.cn/problems/subsets/?show=1) | 🟠 |
| [784. Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/?show=1) | [784. 字母大小写全排列](https://leetcode.cn/problems/letter-case-permutation/?show=1) | 🟠 |
| [89. Gray Code](https://leetcode.com/problems/gray-code/?show=1) | [89. 格雷编码](https://leetcode.cn/problems/gray-code/?show=1) | 🟠 |
| [93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/?show=1) | [93. 复原 IP 地址](https://leetcode.cn/problems/restore-ip-addresses/?show=1) | 🟠 |
| - | [剑指 Offer 34. 二叉树中和为某一值的路径](https://leetcode.cn/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/?show=1) | 🟠 |
| - | [剑指 Offer II 079. 所有子集](https://leetcode.cn/problems/TVdhkn/?show=1) | 🟠 |
| - | [剑指 Offer II 080. 含有 k 个元素的组合](https://leetcode.cn/problems/uUsW3B/?show=1) | 🟠 |
| - | [剑指 Offer II 081. 允许重复选择元素的组合](https://leetcode.cn/problems/Ygoe9J/?show=1) | 🟠 |
| - | [剑指 Offer II 083. 没有重复元素集合的全排列](https://leetcode.cn/problems/VvJkup/?show=1) | 🟠 |
| - | [剑指 Offer II 085. 生成匹配的括号](https://leetcode.cn/problems/IDBivT/?show=1) | 🟠 |

</details>
<hr>



**＿＿＿＿＿＿＿＿＿＿＿＿＿**



![](https://labuladong.online/algo/images/souyisou2.png)