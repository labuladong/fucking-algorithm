# 如何k个一组反转链表

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
| [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [25. K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/) | 🔴

**-----------**

之前的文章「递归反转链表的一部分」讲了如何递归地反转一部分链表，有读者就问如何迭代地反转链表，这篇文章解决的问题也需要反转链表的函数，我们不妨就用迭代方式来解决。

本文要解决力扣第 25 题「K 个一组翻转链表」，题目不难理解：

![](https://labuladong.github.io/algo/images/kgroup/title.png)

这个问题经常在面经中看到，而且力扣上难度是 Hard，它真的有那么难吗？

对于基本数据结构的算法问题其实都不难，只要结合特点一点点拆解分析，一般都没啥难点。下面我们就来拆解一下这个问题。

### 一、分析问题

首先，前文 [学习数据结构的框架思维](https://labuladong.github.io/article/fname.html?fname=学习数据结构和算法的高效方法) 提到过，链表是一种兼具递归和迭代性质的数据结构，认真思考一下可以发现**这个问题具有递归性质**。

什么叫递归性质？直接上图理解，比如说我们对这个链表调用 `reverseKGroup(head, 2)`，即以 2 个节点为一组反转链表：

![](https://labuladong.github.io/algo/images/kgroup/1.jpg)

如果我设法把前 2 个节点反转，那么后面的那些节点怎么处理？后面的这些节点也是一条链表，而且规模（长度）比原来这条链表小，这就叫**子问题**。

![](https://labuladong.github.io/algo/images/kgroup/2.jpg)

我们可以把原先的 `head` 指针移动到后面这一段链表的开头，然后继续递归调用 `reverseKGroup(head, 2)`，因为子问题（后面这部分链表）和原问题（整条链表）的结构完全相同，这就是所谓的递归性质。

发现了递归性质，就可以得到大致的算法流程：

**1、先反转以 `head` 开头的 `k` 个元素**。

![](https://labuladong.github.io/algo/images/kgroup/3.jpg)

**2、将第 `k + 1` 个元素作为 `head` 递归调用 `reverseKGroup` 函数**。

![](https://labuladong.github.io/algo/images/kgroup/4.jpg)

**3、将上述两个过程的结果连接起来**。

![](https://labuladong.github.io/algo/images/kgroup/5.jpg)

整体思路就是这样了，最后一点值得注意的是，递归函数都有个 base case，对于这个问题是什么呢？

题目说了，如果最后的元素不足 `k` 个，就保持不变。这就是 base case，待会会在代码里体现。

### 二、代码实现

首先，我们要实现一个 `reverse` 函数反转一个区间之内的元素。在此之前我们再简化一下，给定链表头结点，如何反转整个链表？

```java
// 反转以 a 为头结点的链表
ListNode reverse(ListNode a) {
    ListNode pre, cur, nxt;
    pre = null; cur = a; nxt = a;
    while (cur != null) {
        nxt = cur.next;
        // 逐个结点反转
        cur.next = pre;
        // 更新指针位置
        pre = cur;
        cur = nxt;
    }
    // 返回反转后的头结点
    return pre;
}
```

算法执行的过程如下 GIF 所示：：

![](https://labuladong.github.io/algo/images/kgroup/8.gif)

这次使用迭代思路来实现的，借助动画理解应该很容易。

「反转以 `a` 为头结点的链表」其实就是「反转 `a` 到 null 之间的结点」，那么如果让你「反转 `a` 到 `b` 之间的结点」，你会不会？

只要更改函数签名，并把上面的代码中 `null` 改成 `b` 即可：

```java
/** 反转区间 [a, b) 的元素，注意是左闭右开 */
ListNode reverse(ListNode a, ListNode b) {
    ListNode pre, cur, nxt;
    pre = null; cur = a; nxt = a;
    // while 终止的条件改一下就行了
    while (cur != b) {
        nxt = cur.next;
        cur.next = pre;
        pre = cur;
        cur = nxt;
    }
    // 返回反转后的头结点
    return pre;
}
```

现在我们迭代实现了反转部分链表的功能，接下来就按照之前的逻辑编写 `reverseKGroup` 函数即可：

```java
ListNode reverseKGroup(ListNode head, int k) {
    if (head == null) return null;
    // 区间 [a, b) 包含 k 个待反转元素
    ListNode a, b;
    a = b = head;
    for (int i = 0; i < k; i++) {
        // 不足 k 个，不需要反转，base case
        if (b == null) return head;
        b = b.next;
    }
    // 反转前 k 个元素
    ListNode newHead = reverse(a, b);
    // 递归反转后续链表并连接起来
    a.next = reverseKGroup(b, k);
    return newHead;
}
```

解释一下 `for` 循环之后的几句代码，注意 `reverse` 函数是反转区间 `[a, b)`，所以情形是这样的：

![](https://labuladong.github.io/algo/images/kgroup/6.jpg)

递归部分就不展开了，整个函数递归完成之后就是这个结果，完全符合题意：

![](https://labuladong.github.io/algo/images/kgroup/7.jpg)

### 三、最后说两句

从阅读量上看，基本数据结构相关的算法文章看的人都不多，我想说这是要吃亏的。

大家喜欢看动态规划相关的问题，可能因为面试很常见，但就我个人理解，很多算法思想都是源于数据结构的。我们公众号的成名之作之一，[学习数据结构的框架思维](https://labuladong.github.io/article/fname.html?fname=学习数据结构和算法的高效方法) 就提过，什么动规、回溯、分治算法，其实都是树的遍历，树这种结构它不就是个多叉链表吗？你能处理基本数据结构的问题，解决一般的算法问题应该也不会太费事。

那么如何分解问题、发现递归性质呢？这个只能多练习，我在数据结构精品课中讲解了 [单链表的递归实现](https://aep.h5.xeknow.com/s/1RQzXc)，应该能够让你进一步加深对递归的理解。



<hr>
<details>
<summary><strong>引用本文的文章</strong></summary>

 - [东哥带你刷二叉树（思路篇）](https://labuladong.github.io/article/fname.html?fname=二叉树系列1)
 - [算法笔试「骗分」套路](https://labuladong.github.io/article/fname.html?fname=刷题技巧)

</details><hr>




<hr>
<details>
<summary><strong>引用本文的题目</strong></summary>

<strong>安装 [我的 Chrome 刷题插件](https://mp.weixin.qq.com/s/X-fE9sR4BLi6T9pn7xP4pg) 点开下列题目可直接查看解题思路：</strong>

| LeetCode | 力扣 |
| :----: | :----: |
| [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/?show=1) | [24. 两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/?show=1) |

</details>



**＿＿＿＿＿＿＿＿＿＿＿＿＿**

**《labuladong 的算法小抄》已经出版，关注公众号查看详情；后台回复关键词「**进群**」可加入算法群；回复「**全家桶**」可下载配套 PDF 和刷题全家桶**：

![](https://labuladong.github.io/algo/images/souyisou2.png)


======其他语言代码======

[25.K个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group)

### javascript

```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */


// 示例一：反转以a为头结点的链表
let reverse = function (a) {
    let pre, cur, nxt;
    pre = null;
    cur = a;
    nxt = a;
    while (cur != null) {
        nxt = cur.next;
        // 逐个结点反转
        cur.next = pre;
        // 更新指针位置
        pre = cur;
        cur = nxt;
    }
    // 返回反转后的头结点
    return pre;
}

/** 反转区间 [a, b) 的元素，注意是左闭右开 */
let reverse = (a, b) => {
    let pre, cur, nxt;
    pre = null;
    cur = a;
    nxt = a;
    // while 终止的条件改一下就行了
    while (cur !== b) {
        nxt = cur.next;
        cur.next = pre;
        pre = cur;
        cur = nxt;
    }
    // 返回反转后的头结点
    return pre;
}


/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
let reverseKGroup = (head, k) => {
    if (head == null) return null;
    // 区间 [a, b) 包含 k 个待反转元素
    let a, b;
    a = b = head;
    for (let i = 0; i < k; i++) {
        // 不足k个，不需反转，base case
        if(b==null) return head;
        b = b.next;
    }

    // 反转前k个元素
    let newHead = reverse(a,b);

    // 递归反转后续链表并连接起来
    a.next = reverseKGroup(b,k);
    return newHead;
}
```

