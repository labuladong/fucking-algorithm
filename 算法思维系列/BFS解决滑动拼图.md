# BFS 算法秒杀各种益智游戏

<p align='center'>
<a href="https://github.com/labuladong/fucking-algorithm" target="view_window"><img alt="GitHub" src="https://img.shields.io/github/stars/labuladong/fucking-algorithm?label=Stars&style=flat-square&logo=GitHub"></a>
<a href="https://appktavsiei5995.pc.xiaoe-tech.com/index" target="_blank"><img class="my_header_icon" src="https://img.shields.io/static/v1?label=精品课程&message=查看&color=pink&style=flat"></a>
<a href="https://www.zhihu.com/people/labuladong"><img src="https://img.shields.io/badge/%E7%9F%A5%E4%B9%8E-@labuladong-000000.svg?style=flat-square&logo=Zhihu"></a>
<a href="https://space.bilibili.com/14089380"><img src="https://img.shields.io/badge/B站-@labuladong-000000.svg?style=flat-square&logo=Bilibili"></a>
</p>

![](https://labuladong.github.io/algo/images/souyisou1.png)

**通知：[数据结构精品课](https://aep.h5.xeknow.com/s/1XJHEO) 已更新到 V2.0；[第 12 期刷题打卡](https://mp.weixin.qq.com/s/eUG2OOzY3k_ZTz-CFvtv5Q) 最后一天报名；点击这里体验 [刷题全家桶](https://labuladong.gitee.io/algo/images/others/%E5%85%A8%E5%AE%B6%E6%A1%B6.jpg)。另外，建议你在我的 [网站](https://labuladong.gitee.io/algo/) 学习文章，体验更好。**



读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| :----: | :----: | :----: |
| [773. Sliding Puzzle](https://leetcode.com/problems/sliding-puzzle/) | [773. 滑动谜题](https://leetcode.cn/problems/sliding-puzzle/) | 🔴

**-----------**

滑动拼图游戏大家应该都玩过，下图是一个 4x4 的滑动拼图：

![](https://labuladong.github.io/algo/images/sliding_puzzle/1.jpeg)

拼图中有一个格子是空的，可以利用这个空着的格子移动其他数字。你需要通过移动这些数字，得到某个特定排列顺序，这样就算赢了。

我小时候还玩过一款叫做「华容道」的益智游戏，也和滑动拼图比较类似：

![](https://labuladong.github.io/algo/images/sliding_puzzle/2.jpeg)

实际上，滑动拼图游戏也叫数字华容道，你看它俩挺相似的。

那么这种游戏怎么玩呢？我记得是有一些套路的，类似于魔方还原公式。但是我们今天不来研究让人头秃的技巧，**这些益智游戏通通可以用暴力搜索算法解决，所以今天我们就学以致用，用 BFS 算法框架来秒杀这些游戏**。

### 一、题目解析

力扣第 773 题「滑动谜题」就是这个问题，题目的要求如下：

给你一个 2x3 的滑动拼图，用一个 2x3 的数组 `board` 表示。拼图中有数字 0~5 六个数，其中**数字 0 就表示那个空着的格子**，你可以移动其中的数字，当 `board` 变为 `[[1,2,3],[4,5,0]]` 时，赢得游戏。

请你写一个算法，计算赢得游戏需要的最少移动次数，如果不能赢得游戏，返回 -1。

比如说输入的二维数组 `board = [[4,1,2],[5,0,3]]`，算法应该返回 5：

![](https://labuladong.github.io/algo/images/sliding_puzzle/5.jpeg)

如果输入的是 `board = [[1,2,3],[5,4,0]]`，则算法返回 -1，因为这种局面下无论如何都不能赢得游戏。

### 二、思路分析

对于这种计算最小步数的问题，我们就要敏感地想到 BFS 算法。

这个题目转化成 BFS 问题是有一些技巧的，我们面临如下问题：

1、一般的 BFS 算法，是从一个起点 `start` 开始，向终点 `target` 进行寻路，但是拼图问题不是在寻路，而是在不断交换数字，这应该怎么转化成 BFS 算法问题呢？

2、即便这个问题能够转化成 BFS 问题，如何处理起点 `start` 和终点 `target`？它们都是数组哎，把数组放进队列，套 BFS 框架，想想就比较麻烦且低效。

首先回答第一个问题，**BFS 算法并不只是一个寻路算法，而是一种暴力搜索算法**，只要涉及暴力穷举的问题，BFS 就可以用，而且可以最快地找到答案。

你想想计算机怎么解决问题的？哪有那么多奇技淫巧，本质上就是把所有可行解暴力穷举出来，然后从中找到一个最优解罢了。

明白了这个道理，我们的问题就转化成了：**如何穷举出 `board` 当前局面下可能衍生出的所有局面**？这就简单了，看数字 0 的位置呗，和上下左右的数字进行交换就行了：

![](https://labuladong.github.io/algo/images/sliding_puzzle/3.jpeg)

这样其实就是一个 BFS 问题，每次先找到数字 0，然后和周围的数字进行交换，形成新的局面加入队列…… 当第一次到达 `target` 时，就得到了赢得游戏的最少步数。

对于第二个问题，我们这里的 `board` 仅仅是 2x3 的二维数组，所以可以压缩成一个一维字符串。**其中比较有技巧性的点在于，二维数组有「上下左右」的概念，压缩成一维后，如何得到某一个索引上下左右的索引**？

对于这道题，题目说输入的数组大小都是 2 x 3，所以我们可以直接手动写出来这个映射：

```java
// 记录一维字符串的相邻索引
int[][] neighbor = new int[][]{
        {1, 3},
        {0, 4, 2},
        {1, 5},
        {0, 4},
        {3, 1, 5},
        {4, 2}
};
```

**这个含义就是，在一维字符串中，索引 `i` 在二维数组中的的相邻索引为 `neighbor[i]`**：

![](https://labuladong.github.io/algo/images/sliding_puzzle/4.jpeg)

那么对于一个 `m x n` 的二维数组，手写它的一维索引映射肯定不现实了，如何用代码生成它的一维索引映射呢？

观察上图就能发现，如果二维数组中的某个元素 `e` 在一维数组中的索引为 `i`，那么 `e` 的左右相邻元素在一维数组中的索引就是 `i - 1` 和 `i + 1`，而 `e` 的上下相邻元素在一维数组中的索引就是 `i - n` 和 `i + n`，其中 `n` 为二维数组的列数。

这样，对于 `m x n` 的二维数组，我们可以写一个函数来生成它的 `neighbor` 索引映射，篇幅所限，我这里就不写了。

至此，我们就把这个问题完全转化成标准的 BFS 问题了，借助前文 [BFS 算法框架](https://labuladong.github.io/article/fname.html?fname=BFS框架) 的代码框架，直接就可以套出解法代码了：

```java
public int slidingPuzzle(int[][] board) {
    int m = 2, n = 3;
    StringBuilder sb = new StringBuilder();
    String target = "123450";
    // 将 2x3 的数组转化成字符串作为 BFS 的起点
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            sb.append(board[i][j]);
        }
    }
    String start = sb.toString();

    // 记录一维字符串的相邻索引
    int[][] neighbor = new int[][]{
            {1, 3},
            {0, 4, 2},
            {1, 5},
            {0, 4},
            {3, 1, 5},
            {4, 2}
    };

    /******* BFS 算法框架开始 *******/
    Queue<String> q = new LinkedList<>();
    HashSet<String> visited = new HashSet<>();
    // 从起点开始 BFS 搜索
    q.offer(start);
    visited.add(start);

    int step = 0;
    while (!q.isEmpty()) {
        int sz = q.size();
        for (int i = 0; i < sz; i++) {
            String cur = q.poll();
            // 判断是否达到目标局面
            if (target.equals(cur)) {
                return step;
            }
            // 找到数字 0 的索引
            int idx = 0;
            for (; cur.charAt(idx) != '0'; idx++) ;
            // 将数字 0 和相邻的数字交换位置
            for (int adj : neighbor[idx]) {
                String new_board = swap(cur.toCharArray(), adj, idx);
                // 防止走回头路
                if (!visited.contains(new_board)) {
                    q.offer(new_board);
                    visited.add(new_board);
                }
            }
        }
        step++;
    }
    /******* BFS 算法框架结束 *******/
    return -1;
}

private String swap(char[] chars, int i, int j) {
    char temp = chars[i];
    chars[i] = chars[j];
    chars[j] = temp;
    return new String(chars);
}
```

至此，这道题目就解决了，其实框架完全没有变，套路都是一样的，我们只是花了比较多的时间将滑动拼图游戏转化成 BFS 算法。

很多益智游戏都是这样，虽然看起来特别巧妙，但都架不住暴力穷举，常用的算法就是回溯算法或者 BFS 算法。​



<hr>
<details>
<summary><strong>引用本文的文章</strong></summary>

 - [BFS 算法解题套路框架](https://labuladong.github.io/article/fname.html?fname=BFS框架)

</details><hr>





**＿＿＿＿＿＿＿＿＿＿＿＿＿**

**《labuladong 的算法小抄》已经出版，关注公众号查看详情；后台回复关键词「**进群**」可加入算法群；回复「**全家桶**」可下载配套 PDF 和刷题全家桶**：

![](https://labuladong.github.io/algo/images/souyisou2.png)