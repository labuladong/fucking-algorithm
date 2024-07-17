# 我写了一个模板，把 Dijkstra 算法变成了默写题

<p align='center'>
<a href="https://github.com/labuladong/fucking-algorithm" target="view_window"><img alt="GitHub" src="https://img.shields.io/github/stars/labuladong/fucking-algorithm?label=Stars&style=flat-square&logo=GitHub"></a>
<a href="https://labuladong.online/algo/" target="_blank"><img class="my_header_icon" src="https://img.shields.io/static/v1?label=精品课程&message=查看&color=pink&style=flat"></a>
<a href="https://www.zhihu.com/people/labuladong"><img src="https://img.shields.io/badge/%E7%9F%A5%E4%B9%8E-@labuladong-000000.svg?style=flat-square&logo=Zhihu"></a>
<a href="https://space.bilibili.com/14089380"><img src="https://img.shields.io/badge/B站-@labuladong-000000.svg?style=flat-square&logo=Bilibili"></a>
</p>

![](https://labuladong.online/algo/images/souyisou1.png)

**通知：[新版网站会员](https://labuladong.online/algo/intro/site-vip/) 即将涨价；已支持老用户续费~另外，建议你在我的 [网站](https://labuladong.online/algo/) 学习文章，体验更好。**



读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| :----: | :----: | :----: |
| [1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) | [1514. 概率最大的路径](https://leetcode.cn/problems/path-with-maximum-probability/) | 🟠
| [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | [1631. 最小体力消耗路径](https://leetcode.cn/problems/path-with-minimum-effort/) | 🟠
| [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) | [743. 网络延迟时间](https://leetcode.cn/problems/network-delay-time/) | 🟠

**-----------**

其实，很多算法的底层原理异常简单，无非就是一步一步延伸，变得**看起来**好像特别复杂，特别牛逼。

但如果你看过历史文章，应该可以对算法形成自己的理解，就会发现很多算法都是换汤不换药，毫无新意，非常枯燥。

比如，[东哥手把手带你刷二叉树（总纲）](https://labuladong.online/algo/essential-technique/binary-tree-summary/) 中说二叉树非常重要，你把这个结构掌握了，就会发现 [动态规划](https://labuladong.online/algo/essential-technique/dynamic-programming-framework/)，[分治算法](https://labuladong.online/algo/practice-in-action/divide-and-conquer/)，[回溯（DFS）算法](https://labuladong.online/algo/essential-technique/backtrack-framework/)，[BFS 算法框架](https://labuladong.online/algo/essential-technique/bfs-framework/)，[Union-Find 并查集算法](https://labuladong.online/algo/data-structure/union-find/)，[二叉堆实现优先级队列](https://labuladong.online/algo/data-structure-basic/binary-heap-implement/) 就是把二叉树翻来覆去的运用。

那么本文又要告诉你，Dijkstra 算法（一般音译成迪杰斯特拉算法）无非就是一个 BFS 算法的加强版，它们都是从二叉树的层序遍历衍生出来的。

这也是为什么我在 [学习数据结构和算法的框架思维](https://labuladong.online/algo/essential-technique/abstraction-of-algorithm/) 中这么强调二叉树的原因。

**下面我们由浅入深，从二叉树的层序遍历聊到 Dijkstra 算法，给出 Dijkstra 算法的代码框架，顺手秒杀几道运用 Dijkstra 算法的题目**。

### 图的抽象

前文 [图论第一期：遍历基础](https://labuladong.online/algo/data-structure/graph-traverse/) 说过「图」这种数据结构的基本实现，图中的节点一般就抽象成一个数字（索引），图的具体实现一般是「邻接矩阵」或者「邻接表」。

![](https://labuladong.online/algo/images/图/0.jpg)

比如上图这幅图用邻接表和邻接矩阵的存储方式如下：

![](https://labuladong.online/algo/images/图/2.jpeg)

前文 [图论第二期：拓扑排序](https://labuladong.online/algo/data-structure/topological-sort/) 告诉你，我们用邻接表的场景更多，结合上图，一幅图可以用如下 Java 代码表示：

<!-- muliti_language -->
```java
// graph[s] 存储节点 s 指向的节点（出度）
List<Integer>[] graph;
```

**如果你想把一个问题抽象成「图」的问题，那么首先要实现一个 API `adj`**：

<!-- muliti_language -->
```java
// 输入节点 s 返回 s 的相邻节点
List<Integer> adj(int s);
```

类似多叉树节点中的 `children` 字段记录当前节点的所有子节点，`adj(s)` 就是计算一个节点 `s` 的相邻节点。

比如上面说的用邻接表表示「图」的方式，`adj` 函数就可以这样表示：

<!-- muliti_language -->
```java
List<Integer>[] graph;

// 输入节点 s，返回 s 的相邻节点
List<Integer> adj(int s) {
    return graph[s];
}
```

当然，对于「加权图」，我们需要知道两个节点之间的边权重是多少，所以还可以抽象出一个 `weight` 方法：

<!-- muliti_language -->
```java
// 返回节点 from 到节点 to 之间的边的权重
int weight(int from, int to);
```

这个 `weight` 方法可以根据实际情况而定，因为不同的算法题，题目给的「权重」含义可能不一样，我们存储权重的方式也不一样。

有了上述基础知识，就可以搞定 Dijkstra 算法了，下面我给你从二叉树的层序遍历开始推演出 Dijkstra 算法的实现。

### 二叉树层级遍历和 BFS 算法

我们之前说过二叉树的层级遍历框架：

<!-- muliti_language -->
```java
// 输入一棵二叉树的根节点，层序遍历这棵二叉树
void levelTraverse(TreeNode root) {
    if (root == null) return 0;
    Queue<TreeNode> q = new LinkedList<>();
    q.offer(root);

    int depth = 1;
    // 从上到下遍历二叉树的每一层
    while (!q.isEmpty()) {
        int sz = q.size();
        // 从左到右遍历每一层的每个节点
        for (int i = 0; i < sz; i++) {
            TreeNode cur = q.poll();
            printf("节点 %s 在第 %s 层", cur, depth);

            // 将下一层节点放入队列
            if (cur.left != null) {
                q.offer(cur.left);
            }
            if (cur.right != null) {
                q.offer(cur.right);
            }
        }
        depth++;
    }
}
```

我们先来思考一个问题，注意二叉树的层级遍历 `while` 循环里面还套了个 `for` 循环，为什么要这样？

`while` 循环和 `for` 循环的配合正是这个遍历框架设计的巧妙之处：

![](https://labuladong.online/algo/images/dijkstra/1.jpeg)

**`while` 循环控制一层一层往下走，`for` 循环利用 `sz` 变量控制从左到右遍历每一层二叉树节点**。

注意我们代码框架中的 `depth` 变量，其实就记录了当前遍历到的层数。换句话说，每当我们遍历到一个节点 `cur`，都知道这个节点属于第几层。

算法题经常会问二叉树的最大深度呀，最小深度呀，层序遍历结果呀，等等问题，所以记录下来这个深度 `depth` 是有必要的。

基于二叉树的遍历框架，我们又可以扩展出多叉树的层序遍历框架：

<!-- muliti_language -->
```java
// 输入一棵多叉树的根节点，层序遍历这棵多叉树
void levelTraverse(TreeNode root) {
    if (root == null) return;
    Queue<TreeNode> q = new LinkedList<>();
    q.offer(root);

    int depth = 1;
    // 从上到下遍历多叉树的每一层
    while (!q.isEmpty()) {
        int sz = q.size();
        // 从左到右遍历每一层的每个节点
        for (int i = 0; i < sz; i++) {
            TreeNode cur = q.poll();
            printf("节点 %s 在第 %s 层", cur, depth);

            // 将下一层节点放入队列
            for (TreeNode child : cur.children) {
                q.offer(child);
            }
        }
        depth++;
    }
}
```

基于多叉树的遍历框架，我们又可以扩展出 BFS（广度优先搜索）的算法框架：

<!-- muliti_language -->
```java
// 输入起点，进行 BFS 搜索
int BFS(Node start) {
    Queue<Node> q; // 核心数据结构
    Set<Node> visited; // 避免走回头路
    
    q.offer(start); // 将起点加入队列
    visited.add(start);

    int step = 0; // 记录搜索的步数
    while (q not empty) {
        int sz = q.size();
        /* 将当前队列中的所有节点向四周扩散一步 */
        for (int i = 0; i < sz; i++) {
            Node cur = q.poll();
            printf("从 %s 到 %s 的最短距离是 %s", start, cur, step);

            /* 将 cur 的相邻节点加入队列 */
            for (Node x : cur.adj()) {
                if (x not in visited) {
                    q.offer(x);
                    visited.add(x);
                }
            }
        }
        step++;
    }
}
```

如果对 BFS 算法不熟悉，可以看前文 [BFS 算法框架](https://labuladong.online/algo/essential-technique/bfs-framework/)，这里只是为了让你做个对比，所谓 BFS 算法，就是把算法问题抽象成一幅「无权图」，然后继续玩二叉树层级遍历那一套罢了。

**注意，我们的 BFS 算法框架也是 `while` 循环嵌套 `for` 循环的形式，也用了一个 `step` 变量记录 `for` 循环执行的次数，无非就是多用了一个 `visited` 集合记录走过的节点，防止走回头路罢了**。

为什么这样呢？

所谓「无权图」，与其说每条「边」没有权重，不如说每条「边」的权重都是 1，从起点 `start` 到任意一个节点之间的路径权重就是它们之间「边」的条数，那可不就是 `step` 变量记录的值么？

再加上 BFS 算法利用 `for` 循环一层一层向外扩散的逻辑和 `visited` 集合防止走回头路的逻辑，当你每次从队列中拿出节点 `cur` 的时候，从 `start` 到 `cur` 的最短权重就是 `step` 记录的步数。

但是，到了「加权图」的场景，事情就没有这么简单了，因为你不能默认每条边的「权重」都是 1 了，这个权重可以是任意正数（Dijkstra 算法要求不能存在负权重边），比如下图的例子：

![](https://labuladong.online/algo/images/dijkstra/2.jpeg)

如果沿用 BFS 算法中的 `step` 变量记录「步数」，显然红色路径一步就可以走到终点，但是这一步的权重很大；正确的最小权重路径应该是绿色的路径，虽然需要走很多步，但是路径权重依然很小。

其实 Dijkstra 和 BFS 算法差不多，不过在讲解 Dijkstra 算法框架之前，我们首先需要对之前的框架进行如下改造：

**想办法去掉 `while` 循环里面的 `for` 循环**。

为什么？有了刚才的铺垫，这个不难理解，刚才说 `for` 循环是干什么用的来着？

是为了让二叉树一层一层往下遍历，让 BFS 算法一步一步向外扩散，因为这个层数 `depth`，或者这个步数 `step`，在之前的场景中有用。

但现在我们想解决「加权图」中的最短路径问题，「步数」已经没有参考意义了，「路径的权重之和」才有意义，所以这个 `for` 循环可以被去掉。

怎么去掉？就拿二叉树的层级遍历来说，其实你可以直接去掉 `for` 循环相关的代码：

<!-- muliti_language -->
```java
// 输入一棵二叉树的根节点，遍历这棵二叉树所有节点
void levelTraverse(TreeNode root) {
    if (root == null) return 0;
    Queue<TreeNode> q = new LinkedList<>();
    q.offer(root);

    // 遍历二叉树的每一个节点
    while (!q.isEmpty()) {
        TreeNode cur = q.poll();
        printf("我不知道节点 %s 在第几层", cur);

        // 将子节点放入队列
        if (cur.left != null) {
            q.offer(cur.left);
        }
        if (cur.right != null) {
            q.offer(cur.right);
        }
    }
}
```

但问题是，没有 `for` 循环，你也没办法维护 `depth` 变量了。

如果你想同时维护 `depth` 变量，让每个节点 `cur` 知道自己在第几层，可以想其他办法，比如新建一个 `State` 类，记录每个节点所在的层数：

<!-- muliti_language -->
```java
class State {
    // 记录 node 节点的深度
    int depth;
    TreeNode node;

    State(TreeNode node, int depth) {
        this.depth = depth;
        this.node = node;
    }
}

// 输入一棵二叉树的根节点，遍历这棵二叉树所有节点
void levelTraverse(TreeNode root) {
    if (root == null) return 0;
    Queue<State> q = new LinkedList<>();
    q.offer(new State(root, 1));

    // 遍历二叉树的每一个节点
    while (!q.isEmpty()) {
        State cur = q.poll();
        TreeNode cur_node = cur.node;
        int cur_depth = cur.depth;
        printf("节点 %s 在第 %s 层", cur_node, cur_depth);

        // 将子节点放入队列
        if (cur_node.left != null) {
            q.offer(new State(cur_node.left, cur_depth + 1));
        }
        if (cur_node.right != null) {
            q.offer(new State(cur_node.right, cur_depth + 1));
        }
    }
}
```

这样，我们就可以不使用 `for` 循环也确切地知道每个二叉树节点的深度了。

**如果你能够理解上面这段代码，我们就可以来看 Dijkstra 算法的代码框架了**。



<hr>
<details class="hint-container details">
<summary><strong>引用本文的文章</strong></summary>

 - [BFS 算法解题套路框架](https://labuladong.online/algo/essential-technique/bfs-framework/)
 - [Kruskal 最小生成树算法](https://labuladong.online/algo/data-structure/kruskal/)
 - [Prim 最小生成树算法](https://labuladong.online/algo/data-structure/prim/)
 - [东哥带你刷二叉树（纲领篇）](https://labuladong.online/algo/essential-technique/binary-tree-summary/)
 - [二分图判定算法](https://labuladong.online/algo/data-structure/bipartite-graph/)
 - [图论基础及遍历算法](https://labuladong.online/algo/data-structure/graph-traverse/)
 - [并查集（Union-Find）算法](https://labuladong.online/algo/data-structure/union-find/)
 - [我的刷题心得：算法的本质](https://labuladong.online/algo/essential-technique/algorithm-summary/)
 - [旅游省钱大法：加权最短路径](https://labuladong.online/algo/dynamic-programming/cheap-travel/)
 - [环检测及拓扑排序算法](https://labuladong.online/algo/data-structure/topological-sort/)

</details><hr>




<hr>
<details class="hint-container details">
<summary><strong>引用本文的题目</strong></summary>

<strong>安装 [我的 Chrome 刷题插件](https://labuladong.online/algo/intro/chrome/) 点开下列题目可直接查看解题思路：</strong>

| LeetCode | 力扣 |
| :----: | :----: |
| [286. Walls and Gates](https://leetcode.com/problems/walls-and-gates/?show=1)🔒 | [286. 墙与门](https://leetcode.cn/problems/walls-and-gates/?show=1)🔒 |
| [310. Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/?show=1) | [310. 最小高度树](https://leetcode.cn/problems/minimum-height-trees/?show=1) |
| [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/?show=1) | [329. 矩阵中的最长递增路径](https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/?show=1) |
| [505. The Maze II](https://leetcode.com/problems/the-maze-ii/?show=1)🔒 | [505. 迷宫 II](https://leetcode.cn/problems/the-maze-ii/?show=1)🔒 |
| [542. 01 Matrix](https://leetcode.com/problems/01-matrix/?show=1) | [542. 01 矩阵](https://leetcode.cn/problems/01-matrix/?show=1) |

</details>
<hr>



**＿＿＿＿＿＿＿＿＿＿＿＿＿**

本文为会员内容，请扫码关注公众号或 [点这里](https://labuladong.online/algo/data-structure/dijkstra/) 查看：

![](https://labuladong.online/algo/images/qrcode.jpg)