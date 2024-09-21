[![Star History Chart](https://api.star-history.com/svg?repos=labuladong/fucking-algorithm&type=Date)](https://star-history.com/#labuladong/fucking-algorithm&Date)


English version is on [labuladong.online](https://labuladong.online/algo/en/) too. Just enjoy：)

# labuladong 的算法笔记

本仓库总共 60 多篇原创文章，都是基于 LeetCode 的题目，涵盖了所有题型和技巧，而且一定要做到**举一反三，通俗易懂**，绝不是简单的代码堆砌，后面有目录。

我先吐槽几句。**刷题刷题，刷的是题，培养的是思维，本仓库的目的就是传递这种算法思维**。我要是只写一个包含 LeetCode 题目代码的仓库，有个锤子用？没有思路解释，没有思维框架，顶多写个时间复杂度，那玩意一眼就能看出来。

只想要答案的话很容易，题目评论区五花八门的答案，动不动就秀 python 一行代码解决，有那么多人点赞。问题是，你去做算法题，是去学习编程语言的奇技淫巧的，还是学习算法思维的呢？你的快乐，到底源自复制别人的一行代码通过测试，已完成题目 +1，还是源自自己通过逻辑推理和算法框架不看答案写出解法？

网上总有大佬喷我，说我写的东西太基础，要么说不能借助框架思维来学习算法。我只能说大家刷算法就是找工作吃饭的，不是打竞赛的，我也是一路摸爬滚打过来的，我们要的是清楚明白有所得，不是故弄玄虚无所指。

不想办法做到通俗易懂，难道要上来先把《算法导论》吹上天，然后把人家都心怀敬仰地劝退？

**做啥事情做多了，都能发现套路的，我把各种算法套路框架总结出来，相信可以帮助其他人少走弯路**。我这个纯靠自学的小童鞋，花了一年时间刷题和总结，自己写了一份算法小抄，后面有目录，这里就不废话了。

## 在开始学习之前

**1、先给本仓库点个 star，满足一下我的虚荣心**，文章质量绝对值你一个 star。我还在继续创作，给我一点继续写文的动力，感谢。

**2、建议收藏我的在线网站，每篇文章开头都有对应的力扣题目链接，可以边看文章边刷题，一共可以手把手带你刷 500 道题目**：

2024 最新地址：https://labuladong.online/algo/

~~GitHub Pages 地址：https://labuladong.online/algo/~~

~~Gitee Pages 地址：https://labuladong.gitee.io/algo/~~

## labuladong 刷题全家桶简介

### 一、算法可视化面板

我的算法网站、所有配套插件都集成了一个算法可视化工具，可以对数据结构和递归过程进行可视化，大幅降低理解算法的难度。几乎每道题目的解法代码都有对应的可视化面板，具体参见下方介绍。


### 二、学习网站

内容当然是我的系列算法教程中最核心的部分，我的算法教程都发布在网站 [labuladong.online](https://labuladong.online/algo/) 上，相信你会未来会在这里花费大量的学习时间，而不是仅仅加入收藏夹~

![](https://labuladong.github.io/pictures/简介/web_intro1.jpg)

### 三、Chrome 插件

**主要功能**：Chrome 插件可以在中文版力扣或英文版 LeetCode 上快捷查看我的「题解」或「思路」，并添加了题目和算法技巧之间的引用关系，可以和我的网站/公众号/课程联动，给我的读者提供最丝滑的刷题体验。安装使用手册见下方目录。

![](https://labuladong.github.io/pictures/简介/chrome_intro.jpg)


### 四、vscode 插件

**主要功能**：和 Chrome 插件功能基本相同，习惯在 vscode 上刷题的读者可以使用该插件。安装使用手册见下方目录。

![](https://labuladong.github.io/pictures/简介/vs_intro.jpg)


### 五、Jetbrains 插件

**主要功能**：和 Chrome 插件功能基本相同，习惯在 Jetbrains 家的 IDE（PyCharm/Intellij/Goland 等）上刷题的读者可以使用该插件。安装使用手册见下方目录。

![](https://labuladong.github.io/pictures/简介/jb_intro.jpg)


最后祝大家学习愉快，在题海中自在遨游！


# 文章目录

<!-- table start -->

### [本站简介](https://labuladong.online/algo/home/)

### [准备工作：安装刷题全家桶](https://labuladong.online/algo/intro/all/)
  * [配套 Chrome 刷题插件](https://labuladong.online/algo/intro/chrome/)
  * [配套 vscode 刷题插件](https://labuladong.online/algo/intro/vscode/)
  * [配套 JetBrains 刷题插件](https://labuladong.online/algo/intro/jetbrains/)
  * [算法可视化面板使用说明（必读）](https://labuladong.online/algo/intro/visualize/)
  * [使用可视化面板的 JS 基础（可选）](https://labuladong.online/algo/intro/js/)
  * [30 天刷题打卡挑战（可选）](https://labuladong.online/algo/challenge/)

### [极速入门：数据结构基础](https://labuladong.online/algo/)
  * [本章导读](https://labuladong.online/algo/intro/data-structure-basic/)
  * [学习本站所需的 Java 基础](https://labuladong.online/algo/intro/java-basic/)
  * [手把手带你实现动态数组](https://labuladong.online/algo/)
    * [数组（顺序存储）基本原理](https://labuladong.online/algo/data-structure-basic/array-basic/)
    * [动态数组代码实现](https://labuladong.online/algo/data-structure-basic/array-implement/)
  * [手把手带你实现单/双链表](https://labuladong.online/algo/)
    * [链表（链式存储）基本原理](https://labuladong.online/algo/data-structure-basic/linkedlist-basic/)
    * [链表代码实现](https://labuladong.online/algo/data-structure-basic/linkedlist-implement/)
  * [手把手带你实现队列/栈](https://labuladong.online/algo/)
    * [队列/栈基本原理](https://labuladong.online/algo/data-structure-basic/queue-stack-basic/)
    * [用链表实现队列/栈](https://labuladong.online/algo/data-structure-basic/linked-queue-stack/)
    * [环形数组技巧](https://labuladong.online/algo/data-structure-basic/cycle-array/)
    * [用数组实现队列/栈](https://labuladong.online/algo/data-structure-basic/array-queue-stack/)
    * [双端队列（Deque）原理及实现](https://labuladong.online/algo/data-structure-basic/deque-implement/)
  * [手把手带你实现哈希表](https://labuladong.online/algo/)
    * [哈希表基本原理](https://labuladong.online/algo/data-structure-basic/hashmap-basic/)
    * [用拉链法实现哈希表](https://labuladong.online/algo/data-structure-basic/hashtable-chaining/)
    * [线性探查法的两个难点](https://labuladong.online/algo/data-structure-basic/linear-probing-key-point/)
    * [线性探查法的两种代码实现](https://labuladong.online/algo/data-structure-basic/linear-probing-code/)
  * [手把手带你实现哈希集合](https://labuladong.online/algo/)
    * [哈希集合的原理及代码实现](https://labuladong.online/algo/data-structure-basic/hash-set/)
  * [手写标准库中的二叉树结构](https://labuladong.online/algo/)
    * [二叉树基础及常见类型](https://labuladong.online/algo/data-structure-basic/binary-tree-basic/)
    * [正在更新 ing](https://labuladong.online/algo/intro/updateing/)
  * [手把手带你实现二叉堆](https://labuladong.online/algo/)
    * [二叉堆的基本原理](https://labuladong.online/algo/data-structure-basic/binary-heap-basic/)
    * [二叉堆的代码实现](https://labuladong.online/algo/data-structure-basic/binary-heap-implement/)
  * [正在更新 ing](https://labuladong.online/algo/intro/updateing/)


### [第零章、核心框架汇总](https://labuladong.online/algo/)
  * [本章导读](https://labuladong.online/algo/intro/core-intro/)
  * [学习算法和刷题的框架思维](https://labuladong.online/algo/essential-technique/abstraction-of-algorithm/)
  * [我的刷题心得：算法的本质](https://labuladong.online/algo/essential-technique/algorithm-summary/)
  * [双指针技巧秒杀七道链表题目](https://labuladong.online/algo/essential-technique/linked-list-skills-summary/)
  * [双指针技巧秒杀七道数组题目](https://labuladong.online/algo/essential-technique/array-two-pointers-summary/)
  * [我写了首诗，把滑动窗口算法变成了默写题](https://labuladong.online/algo/essential-technique/sliding-window-framework/)
  * [我写了首诗，把二分搜索算法变成了默写题](https://labuladong.online/algo/essential-technique/binary-search-framework/)
  * [东哥带你刷二叉树（纲领篇）](https://labuladong.online/algo/essential-technique/binary-tree-summary/)
  * [动态规划解题套路框架](https://labuladong.online/algo/essential-technique/dynamic-programming-framework/)
  * [回溯算法解题套路框架](https://labuladong.online/algo/essential-technique/backtrack-framework/)
  * [回溯算法秒杀所有排列/组合/子集问题](https://labuladong.online/algo/essential-technique/permutation-combination-subset-all-in-one/)
  * [球盒模型：回溯算法穷举的两种视角](https://labuladong.online/algo/practice-in-action/two-views-of-backtrack/)
  * [BFS 算法解题套路框架](https://labuladong.online/algo/essential-technique/bfs-framework/)
  * [算法时空复杂度分析实用指南](https://labuladong.online/algo/essential-technique/complexity-analysis/)


### [第一章、手把手刷数据结构](https://labuladong.online/algo/)
  * [手把手刷链表算法](https://labuladong.online/algo/)
    * [双指针技巧秒杀七道链表题目](https://labuladong.online/algo/essential-technique/linked-list-skills-summary/)
    * [【强化练习】链表双指针经典习题](https://labuladong.online/algo/problem-set/linkedlist-two-pointers/)
    * [递归魔法：反转单链表](https://labuladong.online/algo/data-structure/reverse-linked-list-recursion/)
    * [如何 K 个一组反转链表](https://labuladong.online/algo/data-structure/reverse-nodes-in-k-group/)
    * [如何判断回文链表](https://labuladong.online/algo/data-structure/palindrome-linked-list/)

  * [手把手刷数组算法](https://labuladong.online/algo/)
    * [双指针技巧秒杀七道数组题目](https://labuladong.online/algo/essential-technique/array-two-pointers-summary/)
    * [【强化练习】数组双指针经典习题](https://labuladong.online/algo/problem-set/array-two-pointers/)
    * [一个方法团灭 nSum 问题](https://labuladong.online/algo/practice-in-action/nsum/)
    * [小而美的算法技巧：前缀和数组](https://labuladong.online/algo/data-structure/prefix-sum/)
    * [【强化练习】前缀和技巧经典习题](https://labuladong.online/algo/problem-set/perfix-sum/)
    * [小而美的算法技巧：差分数组](https://labuladong.online/algo/data-structure/diff-array/)
    * [二维数组的花式遍历技巧](https://labuladong.online/algo/practice-in-action/2d-array-traversal-summary/)
    * [滑动窗口算法核心代码模板](https://labuladong.online/algo/essential-technique/sliding-window-framework/)
    * [【强化练习】滑动窗口算法经典习题](https://labuladong.online/algo/problem-set/sliding-window/)
    * [滑动窗口算法延伸：Rabin Karp 字符匹配算法](https://labuladong.online/algo/practice-in-action/rabinkarp/)
    * [二分搜索算法核心代码模板](https://labuladong.online/algo/essential-technique/binary-search-framework/)
    * [实际二分搜索时的思维框架](https://labuladong.online/algo/frequency-interview/binary-search-in-action/)
    * [【强化练习】二分搜索算法经典习题](https://labuladong.online/algo/problem-set/binary-search/)
    * [带权重的随机选择算法](https://labuladong.online/algo/frequency-interview/random-pick-with-weight/)
    * [田忌赛马背后的算法决策](https://labuladong.online/algo/practice-in-action/advantage-shuffle/)
    * [常数时间删除/查找数组中的任意元素](https://labuladong.online/algo/data-structure/random-set/)
    * [一道数组去重的算法题把我整不会了](https://labuladong.online/algo/frequency-interview/remove-duplicate-letters/)


  * [手把手刷二叉树算法](https://labuladong.online/algo/)
    * [东哥带你刷二叉树（纲领篇）](https://labuladong.online/algo/essential-technique/binary-tree-summary/)
    * [东哥带你刷二叉树（思路篇）](https://labuladong.online/algo/data-structure/binary-tree-part1/)
    * [东哥带你刷二叉树（构造篇）](https://labuladong.online/algo/data-structure/binary-tree-part2/)
    * [东哥带你刷二叉树（后序篇）](https://labuladong.online/algo/data-structure/binary-tree-part3/)
    * [东哥带你刷二叉树（序列化篇）](https://labuladong.online/algo/data-structure/serialize-and-deserialize-binary-tree/)
    * [归并排序详解及应用](https://labuladong.online/algo/practice-in-action/merge-sort/)
    * [东哥带你刷二叉搜索树（特性篇）](https://labuladong.online/algo/data-structure/bst-part1/)
    * [东哥带你刷二叉搜索树（基操篇）](https://labuladong.online/algo/data-structure/bst-part2/)
    * [东哥带你刷二叉搜索树（构造篇）](https://labuladong.online/algo/data-structure/bst-part3/)
    * [快速排序详解及应用](https://labuladong.online/algo/practice-in-action/quick-sort/)
    * [题目不让我干什么，我偏要干什么](https://labuladong.online/algo/data-structure/flatten-nested-list-iterator/)
    * [Git原理之最近公共祖先](https://labuladong.online/algo/practice-in-action/lowest-common-ancestor-summary/)
    * [如何计算完全二叉树的节点数](https://labuladong.online/algo/data-structure/count-complete-tree-nodes/)
    * [用栈模拟递归迭代遍历二叉树](https://labuladong.online/algo/data-structure/iterative-traversal-binary-tree/)

  * [手把手带你刷 100 道二叉树习题](https://labuladong.online/algo/)
    * [【强化练习】用「遍历」思维解题 I](https://labuladong.online/algo/problem-set/binary-tree-traverse-1/)
    * [【强化练习】用「遍历」思维解题 II](https://labuladong.online/algo/problem-set/binary-tree-traverse-2/)
    * [【强化练习】用「遍历」思维解题 III](https://labuladong.online/algo/problem-set/binary-tree-traverse-3/)
    * [【强化练习】用「分解问题」思维解题 I](https://labuladong.online/algo/problem-set/binary-tree-divide-1/)
    * [【强化练习】用「分解问题」思维解题 II](https://labuladong.online/algo/problem-set/binary-tree-divide-2/)
    * [【强化练习】同时运用两种思维解题](https://labuladong.online/algo/problem-set/binary-tree-combine-two-view/)
    * [【强化练习】利用后序位置解题 I](https://labuladong.online/algo/problem-set/binary-tree-post-order-1/)
    * [【强化练习】利用后序位置解题 II](https://labuladong.online/algo/problem-set/binary-tree-post-order-2/)
    * [【强化练习】利用后序位置解题 III](https://labuladong.online/algo/problem-set/binary-tree-post-order-3/)
    * [【强化练习】运用层序遍历解题 I](https://labuladong.online/algo/problem-set/binary-tree-level-1/)
    * [【强化练习】运用层序遍历解题 II](https://labuladong.online/algo/problem-set/binary-tree-level-2/)
    * [【强化练习】二叉搜索树经典例题 I](https://labuladong.online/algo/problem-set/bst1/)
    * [【强化练习】二叉搜索树经典例题 II](https://labuladong.online/algo/problem-set/bst2/)


  * [手把手设计数据结构](https://labuladong.online/algo/)
    * [队列实现栈以及栈实现队列](https://labuladong.online/algo/data-structure/stack-queue/)
    * [【强化练习】栈的经典习题](https://labuladong.online/algo/problem-set/stack/)
    * [【强化练习】队列的经典习题](https://labuladong.online/algo/problem-set/queue/)
    * [单调栈算法模板解决三道例题](https://labuladong.online/algo/data-structure/monotonic-stack/)
    * [【强化练习】单调栈的几种变体及经典习题](https://labuladong.online/algo/problem-set/monotonic-stack/)
    * [单调队列结构解决滑动窗口问题](https://labuladong.online/algo/data-structure/monotonic-queue/)
    * [【强化练习】单调队列的通用实现及经典习题](https://labuladong.online/algo/problem-set/monotonic-queue/)
    * [算法就像搭乐高：带你手撸 LRU 算法](https://labuladong.online/algo/data-structure/lru-cache/)
    * [算法就像搭乐高：带你手撸 LFU 算法](https://labuladong.online/algo/frequency-interview/lfu/)
    * [【强化练习】哈希表更多习题](https://labuladong.online/algo/problem-set/hash-table/)
    * [二叉堆详解实现优先级队列](https://labuladong.online/algo/data-structure-basic/binary-heap-implement/)
    * [【强化练习】优先级队列经典习题](https://labuladong.online/algo/problem-set/binary-heap/)
    * [一道求中位数的算法题把我整不会了](https://labuladong.online/algo/practice-in-action/find-median-from-data-stream/)
    * [前缀树算法模板秒杀五道算法题](https://labuladong.online/algo/data-structure/trie/)
    * [设计朋友圈时间线功能](https://labuladong.online/algo/data-structure/design-twitter/)
    * [【强化练习】更多经典设计习题](https://labuladong.online/algo/problem-set/ds-design/)


  * [手把手刷图算法](https://labuladong.online/algo/)
    * [图论基础及遍历算法](https://labuladong.online/algo/data-structure/graph-traverse/)
    * [环检测及拓扑排序算法](https://labuladong.online/algo/data-structure/topological-sort/)
    * [众里寻他千百度：名流问题](https://labuladong.online/algo/frequency-interview/find-celebrity/)
    * [二分图判定算法](https://labuladong.online/algo/data-structure/bipartite-graph/)
    * [并查集（Union-Find）算法](https://labuladong.online/algo/data-structure/union-find/)
    * [Kruskal 最小生成树算法](https://labuladong.online/algo/data-structure/kruskal/)
    * [Prim 最小生成树算法](https://labuladong.online/algo/data-structure/prim/)
    * [Dijkstra 算法模板及应用](https://labuladong.online/algo/data-structure/dijkstra/)


### [第二章、手把手刷动态规划](https://labuladong.online/algo/)
  * [动态规划基本技巧](https://labuladong.online/algo/)
    * [动态规划解题套路框架](https://labuladong.online/algo/essential-technique/dynamic-programming-framework/)
    * [动态规划设计：最长递增子序列](https://labuladong.online/algo/dynamic-programming/longest-increasing-subsequence/)
    * [最优子结构原理和 dp 数组遍历方向](https://labuladong.online/algo/dynamic-programming/faq-summary/)
    * [base case 和备忘录的初始值怎么定？](https://labuladong.online/algo/dynamic-programming/memo-fundamental/)
    * [动态规划穷举的两种视角](https://labuladong.online/algo/dynamic-programming/two-views-of-dp/)
    * [动态规划和回溯算法的思维转换](https://labuladong.online/algo/dynamic-programming/word-break/)
    * [对动态规划进行降维打击](https://labuladong.online/algo/dynamic-programming/space-optimization/)

  * [子序列类型问题](https://labuladong.online/algo/)
    * [经典动态规划：编辑距离](https://labuladong.online/algo/dynamic-programming/edit-distance/)
    * [动态规划设计：最长递增子序列](https://labuladong.online/algo/dynamic-programming/longest-increasing-subsequence/)
    * [动态规划设计：最大子数组](https://labuladong.online/algo/dynamic-programming/maximum-subarray/)
    * [经典动态规划：最长公共子序列](https://labuladong.online/algo/dynamic-programming/longest-common-subsequence/)
    * [动态规划之子序列问题解题模板](https://labuladong.online/algo/dynamic-programming/subsequence-problem/)

  * [背包类型问题](https://labuladong.online/algo/)
    * [经典动态规划：0-1 背包问题](https://labuladong.online/algo/dynamic-programming/knapsack1/)
    * [经典动态规划：子集背包问题](https://labuladong.online/algo/dynamic-programming/knapsack2/)
    * [经典动态规划：完全背包问题](https://labuladong.online/algo/dynamic-programming/knapsack3/)
    * [目标和问题：背包问题的变体](https://labuladong.online/algo/dynamic-programming/target-sum/)

  * [用动态规划玩游戏](https://labuladong.online/algo/)
    * [动态规划之最小路径和](https://labuladong.online/algo/dynamic-programming/minimum-path-sum/)
    * [动态规划帮我通关了《魔塔》](https://labuladong.online/algo/dynamic-programming/magic-tower/)
    * [动态规划帮我通关了《辐射4》](https://labuladong.online/algo/dynamic-programming/freedom-trail/)
    * [旅游省钱大法：加权最短路径](https://labuladong.online/algo/dynamic-programming/cheap-travel/)
    * [经典动态规划：正则表达式](https://labuladong.online/algo/dynamic-programming/regular-expression-matching/)
    * [经典动态规划：高楼扔鸡蛋](https://labuladong.online/algo/dynamic-programming/egg-drop/)
    * [经典动态规划：戳气球](https://labuladong.online/algo/dynamic-programming/burst-balloons/)
    * [经典动态规划：博弈问题](https://labuladong.online/algo/dynamic-programming/game-theory/)
    * [经典动态规划：四键键盘](https://labuladong.online/algo/dynamic-programming/four-keyboard/)
    * [一个方法团灭 LeetCode 打家劫舍问题](https://labuladong.online/algo/dynamic-programming/house-robber/)
    * [一个方法团灭 LeetCode 股票买卖问题](https://labuladong.online/algo/dynamic-programming/stock-problem-summary/)

  * [贪心类型问题](https://labuladong.online/algo/)
    * [老司机加油算法](https://labuladong.online/algo/frequency-interview/gas-station-greedy/)
    * [贪心算法之区间调度问题](https://labuladong.online/algo/frequency-interview/interval-scheduling/)
    * [扫描线技巧：安排会议室](https://labuladong.online/algo/frequency-interview/scan-line-technique/)
    * [剪视频剪出一个贪心算法](https://labuladong.online/algo/frequency-interview/cut-video/)
    * [如何运用贪心思想玩跳跃游戏](https://labuladong.online/algo/frequency-interview/jump-game-summary/)

### [第三章、必知必会算法技巧](https://labuladong.online/algo/)
  * [经典暴力搜索算法](https://labuladong.online/algo/)
    * [回溯算法解题套路框架](https://labuladong.online/algo/essential-technique/backtrack-framework/)
    * [回溯算法秒杀所有排列/组合/子集问题](https://labuladong.online/algo/essential-technique/permutation-combination-subset-all-in-one/)
    * [球盒模型：回溯算法穷举的两种视角](https://labuladong.online/algo/practice-in-action/two-views-of-backtrack/)
    * [一文秒杀所有岛屿题目](https://labuladong.online/algo/frequency-interview/island-dfs-summary/)
    * [回溯算法最佳实践：解数独](https://labuladong.online/algo/practice-in-action/sudoku/)
    * [回溯算法最佳实践：括号生成](https://labuladong.online/algo/practice-in-action/generate-parentheses/)
    * [回溯算法最佳实践：集合划分](https://labuladong.online/algo/practice-in-action/partition-to-k-equal-sum-subsets/)
    * [BFS 算法解题套路框架](https://labuladong.online/algo/essential-technique/bfs-framework/)
    * [如何用 BFS 算法秒杀各种智力题](https://labuladong.online/algo/practice-in-action/sliding-puzzle/)

  * [数学运算技巧](https://labuladong.online/algo/)
    * [一行代码就能解决的算法题](https://labuladong.online/algo/frequency-interview/one-line-solutions/)
    * [几个反直觉的概率问题](https://labuladong.online/algo/frequency-interview/probability-problem/)
    * [常用的位操作](https://labuladong.online/algo/frequency-interview/bitwise-operation/)
    * [谈谈游戏中的随机算法](https://labuladong.online/algo/frequency-interview/random-algorithm/)
    * [讲两道常考的阶乘算法题](https://labuladong.online/algo/frequency-interview/factorial-problems/)
    * [如何高效寻找素数](https://labuladong.online/algo/frequency-interview/print-prime-number/)
    * [如何高效进行模幂运算](https://labuladong.online/algo/frequency-interview/quick-power/)
    * [如何同时寻找缺失和重复的元素](https://labuladong.online/algo/frequency-interview/mismatch-set/)

  * [经典面试题](https://labuladong.online/algo/)
    * [算法笔试「骗分」套路](https://labuladong.online/algo/other-skills/tips-in-exam/)
    * [一文秒杀所有丑数系列问题](https://labuladong.online/algo/frequency-interview/ugly-number-summary/)
    * [分治算法详解：运算优先级](https://labuladong.online/algo/practice-in-action/divide-and-conquer/)
    * [一个方法解决三道区间问题](https://labuladong.online/algo/practice-in-action/interval-problem-summary/)
    * [谁能想到，斗地主也能玩出算法](https://labuladong.online/algo/practice-in-action/split-array-into-consecutive-subsequences/)
    * [烧饼排序算法](https://labuladong.online/algo/frequency-interview/pancake-sorting/)
    * [字符串乘法计算](https://labuladong.online/algo/practice-in-action/multiply-strings/)
    * [如何实现一个计算器](https://labuladong.online/algo/data-structure/implement-calculator/)
    * [如何高效解决接雨水问题](https://labuladong.online/algo/frequency-interview/trapping-rain-water/)
    * [如何解决括号相关的问题](https://labuladong.online/algo/frequency-interview/bracket-problems-summary/)
    * [如何判定完美矩形](https://labuladong.online/algo/frequency-interview/perfect-rectangle/)

<!-- table end -->

# 感谢如下大佬参与翻译

按照昵称字典序排名：

[ABCpril](https://github.com/ABCpril), 
[andavid](https://github.com/andavid), 
[bryceustc](https://github.com/bryceustc), 
[build2645](https://github.com/build2645), 
[CarrieOn](https://github.com/CarrieOn), 
[cooker](https://github.com/xiaochuhub), 
[Dong Wang](https://github.com/Coder2Programmer), 
[ExcaliburEX](https://github.com/ExcaliburEX), 
[floatLig](https://github.com/floatLig), 
[ForeverSolar](https://github.com/foreversolar), 
[Fulin Li](https://fulinli.github.io/), 
[Funnyyanne](https://github.com/Funnyyanne), 
[GYHHAHA](https://github.com/GYHHAHA), 
[Hi_archer](https://hiarcher.top/), 
[Iruze](https://github.com/Iruze), 
[Jieyixia](https://github.com/Jieyixia), 
[Justin](https://github.com/Justin-YGG), 
[Kevin](https://github.com/Kevin-free), 
[Lrc123](https://github.com/Lrc123), 
[lriy](https://github.com/lriy), 
[Lyjeeq](https://github.com/Lyjeeq), 
[MasonShu](https://greenwichmt.github.io/), 
[Master-cai](https://github.com/Master-cai), 
[miaoxiaozui2017](https://github.com/miaoxiaozui2017), 
[natsunoyoru97](https://github.com/natsunoyoru97), 
[nettee](https://github.com/nettee), 
[PaperJets](https://github.com/PaperJets), 
[qy-yang](https://github.com/qy-yang), 
[realism0331](https://github.com/realism0331), 
[SCUhzs](https://github.com/brucecat), 
[Seaworth](https://github.com/Seaworth), 
[shazi4399](https://github.com/shazi4399), 
[ShuozheLi](https://github.com/ShuoZheLi/), 
[sinjoywong](https://blog.csdn.net/SinjoyWong), 
[sunqiuming526](https://github.com/sunqiuming526), 
[Tianhao Zhou](https://github.com/tianhaoz95), 
[timmmGZ](https://github.com/timmmGZ), 
[tommytim0515](https://github.com/tommytim0515), 
[ucsk](https://github.com/ucsk), 
[wadegrc](https://github.com/wadegrc), 
[walsvid](https://github.com/walsvid), 
[warmingkkk](https://github.com/warmingkkk), 
[Wonderxie](https://github.com/Wonderxie), 
[wsyzxxxx](https://github.com/wsyzxxxx), 
[xiaodp](https://github.com/xiaodp), 
[youyun](https://github.com/youyun), 
[yx-tan](https://github.com/yx-tan), 
[Zero](https://github.com/Mr2er0), 
[Ziming](https://github.com/ML-ZimingMeng/LeetCode-Python3)

# Donate

如果本仓库对你有帮助，可以请作者喝杯速溶咖啡

<img src="pictures/pay.jpg" width = "200" align=center />
