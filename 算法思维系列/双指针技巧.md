# 双指针技巧秒杀七道数组题目



![](https://labuladong.online/algo/images/souyisou1.png)

**通知：为满足广大读者的需求，网站上架 [速成目录](https://labuladong.online/algo/intro/quick-learning-plan/)，如有需要可以看下，谢谢大家的支持~另外，建议你在我的 [网站](https://labuladong.online/algo/) 学习文章，体验更好。**



读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| :----: | :----: | :----: |
| [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [167. 两数之和 II - 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/) | 🟠 |
| [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/) | 🟢 |
| [27. Remove Element](https://leetcode.com/problems/remove-element/) | [27. 移除元素](https://leetcode.cn/problems/remove-element/) | 🟢 |
| [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) | [283. 移动零](https://leetcode.cn/problems/move-zeroes/) | 🟢 |
| [344. Reverse String](https://leetcode.com/problems/reverse-string/) | [344. 反转字符串](https://leetcode.cn/problems/reverse-string/) | 🟢 |
| [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | [5. 最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/) | 🟠 |
| [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | [83. 删除排序链表中的重复元素](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/) | 🟢 |
| - | [剑指 Offer 57. 和为s的两个数字](https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/) | 🟢 |
| - | [剑指 Offer II 006. 排序数组中两个数字之和](https://leetcode.cn/problems/kLl5u1/) | 🟢 |

**-----------**



> [!NOTE]
> 阅读本文前，你需要先学习：
> 
> - [数组基础](https://labuladong.online/algo/data-structure-basic/array-basic/)
> - [单链表的六大解题套路](https://labuladong.online/algo/essential-technique/linked-list-skills-summary/)


在处理数组和链表相关问题时，双指针技巧是经常用到的，双指针技巧主要分为两类：**左右指针**和**快慢指针**。

所谓左右指针，就是两个指针相向而行或者相背而行；而所谓快慢指针，就是两个指针同向而行，一快一慢。

对于单链表来说，大部分技巧都属于快慢指针，[单链表的六大解题套路](https://labuladong.online/algo/essential-technique/linked-list-skills-summary/) 都涵盖了，比如链表环判断，倒数第 `K` 个链表节点等问题，它们都是通过一个 `fast` 快指针和一个 `slow` 慢指针配合完成任务。

在数组中并没有真正意义上的指针，但我们可以把索引当做数组中的指针，这样也可以在数组中施展双指针技巧，**本文主要讲数组相关的双指针算法**。

## 一、快慢指针技巧

### 原地修改

**数组问题中比较常见的快慢指针技巧，是让你原地修改数组**。

比如说看下力扣第 26 题「删除有序数组中的重复项」，让你在有序数组去重：

<Problem slug="remove-duplicates-from-sorted-array" />

函数签名如下：

```java
int removeDuplicates(int[] nums);
```

简单解释一下什么是原地修改：

如果不是原地修改的话，我们直接 new 一个 `int[]` 数组，把去重之后的元素放进这个新数组中，然后返回这个新数组即可。

但是现在题目让你原地删除，不允许 new 新数组，只能在原数组上操作，然后返回一个长度，这样就可以通过返回的长度和原始数组得到我们去重后的元素有哪些了。

由于数组已经排序，所以重复的元素一定连在一起，找出它们并不难。但如果毎找到一个重复元素就立即原地删除它，由于数组中删除元素涉及数据搬移，整个时间复杂度是会达到 $O(N^2)$。

高效解决这道题就要用到快慢指针技巧：

我们让慢指针 `slow` 走在后面，快指针 `fast` 走在前面探路，找到一个不重复的元素就赋值给 `slow` 并让 `slow` 前进一步。

这样，就保证了 `nums[0..slow]` 都是无重复的元素，当 `fast` 指针遍历完整个数组 `nums` 后，`nums[0..slow]` 就是整个数组去重之后的结果。

看代码：

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int slow = 0, fast = 0;
        while (fast < nums.length) {
            if (nums[fast] != nums[slow]) {
                slow++;
                // 维护 nums[0..slow] 无重复
                nums[slow] = nums[fast];
            }
            fast++;
        }
        // 数组长度为索引 + 1
        return slow + 1;
    }
}
```

<visual slug='remove-duplicates-from-sorted-array' >

你可以打开下面的可视化面板，多次点击 <code type="click">while (fast < nums.length)</code> 这一行代码，即可看到两个指针维护 `nums[0..slow]` 无重复元素：

</visual>

再简单扩展一下，看看力扣第 83 题「删除排序链表中的重复元素」，如果给你一个有序的单链表，如何去重呢？

其实和数组去重是一模一样的，唯一的区别是把数组赋值操作变成操作指针而已，你对照着之前的代码来看：

```java
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return null;
        ListNode slow = head, fast = head;
        while (fast != null) {
            if (fast.val != slow.val) {
                // nums[slow] = nums[fast];
                slow.next = fast;
                // slow++;
                slow = slow.next;
            }
            // fast++
            fast = fast.next;
        }
        // 断开与后面重复元素的连接
        slow.next = null;
        return head;
    }
}
```

算法执行的过程请看下面这个可视化面板：


<hr/>
<a href="https://labuladong.online/algo-visualize/leetcode/remove-duplicates-from-sorted-list/" target="_blank">
<details style="max-width:90%;max-height:400px">
<summary>
<strong>🥳 代码可视化动画🥳</strong>
</summary>
</details>
</a>
<hr/>

> [!NOTE]
> 这里可能有读者会问，链表中那些重复的元素并没有被删掉，就让这些节点在链表上挂着，合适吗？
> 
> 这就要探讨不同语言的特性了，像 Java/Python 这类带有垃圾回收的语言，可以帮我们自动找到并回收这些「悬空」的链表节点的内存，而像 C++ 这类语言没有自动垃圾回收的机制，确实需要我们编写代码时手动释放掉这些节点的内存。
> 
> 不过话说回来，就算法思维的培养来说，我们只需要知道这种快慢指针技巧即可。

**除了让你在有序数组/链表中去重，题目还可能让你对数组中的某些元素进行「原地删除」**。

比如力扣第 27 题「移除元素」，看下题目：





<Problem slug="remove-element" />

```java
// 函数签名如下
int removeElement(int[] nums, int val);
```

题目要求我们把 `nums` 中所有值为 `val` 的元素原地删除，依然需要使用快慢指针技巧：

如果 `fast` 遇到值为 `val` 的元素，则直接跳过，否则就赋值给 `slow` 指针，并让 `slow` 前进一步。

这和前面说到的数组去重问题解法思路是完全一样的，直接看代码：

```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int fast = 0, slow = 0;
        while (fast < nums.length) {
            if (nums[fast] != val) {
                nums[slow] = nums[fast];
                slow++;
            }
            fast++;
        }
        return slow;
    }
}
```

<visual slug='remove-element' >

你可以打开下面的可视化面板，多次点击 <code type="click">while (fast !== null)</code> 这一行代码，即可看到两个指针维护 `nums[0..slow]` 无重复元素：

</visual>

注意这里和有序数组去重的解法有一个细节差异，我们这里是先给 `nums[slow]` 赋值然后再给 `slow++`，这样可以保证 `nums[0..slow-1]` 是不包含值为 `val` 的元素的，最后的结果数组长度就是 `slow`。

实现了这个 `removeElement` 函数，接下来看看力扣第 283 题「移动零」：

给你输入一个数组 `nums`，请你**原地修改**，将数组中的所有值为 0 的元素移到数组末尾，函数签名如下：

```java
void moveZeroes(int[] nums);
```

比如说给你输入 `nums = [0,1,4,0,2]`，你的算法没有返回值，但是会把 `nums` 数组原地修改成 `[1,4,2,0,0]`。

结合之前说到的几个题目，你是否有已经有了答案呢？

稍微修改上一题中的 `removeElement` 函数就可以完成这道题，或者直接复用 `removeElement` 函数也可以。

题目让我们将所有 0 移到最后，其实就相当于移除 `nums` 中的所有 0，然后再把后面的元素都赋值为 0：

```java
class Solution {
    public void moveZeroes(int[] nums) {
        // 去除 nums 中的所有 0，返回不含 0 的数组长度
        int p = removeElement(nums, 0);
        // 将 nums[p..] 的元素赋值为 0
        for (; p < nums.length; p++) {
            nums[p] = 0;
        }
    }

    public int removeElement(int[] nums, int val) {
        // 见上文代码实现
    }
}
```

<visual slug='move-zeroes' >

你可以点开下面的可视化面板，多次点击 <code type="click">while (fast < nums.length)</code> 这行代码查看快慢指针的运动，然后多次点击 <code type="click">nums[p] = 0;</code> 这行代码将后面的元素都改为 0：

</visual>

到这里，原地修改数组的这些题目就已经差不多了。

### 滑动窗口

数组中另一大类快慢指针的题目就是「滑动窗口算法」。我在另一篇文章 [滑动窗口算法核心框架详解](https://labuladong.online/algo/essential-technique/sliding-window-framework/) 给出了滑动窗口的代码框架：





```java
// 滑动窗口算法框架伪码
int left = 0, right = 0;

while (right < nums.size()) {
    // 增大窗口
    window.addLast(nums[right]);
    right++;
    
    while (window needs shrink) {
        // 缩小窗口
        window.removeFirst(nums[left]);
        left++;
    }
}
```



具体的题目本文就不重复了，这里只强调滑动窗口算法的快慢指针特性：

`left` 指针在后，`right` 指针在前，两个指针中间的部分就是「窗口」，算法通过扩大和缩小「窗口」来解决某些问题。

## 二、左右指针的常用算法

### 二分查找

我在另一篇文章 [二分查找框架详解](https://labuladong.online/algo/essential-technique/binary-search-framework/) 中有详细探讨二分搜索代码的细节问题，这里只写最简单的二分算法，旨在突出它的双指针特性：

```java
int binarySearch(int[] nums, int target) {
    // 一左一右两个指针相向而行
    int left = 0, right = nums.length - 1;
    while(left <= right) {
        int mid = (right + left) / 2;
        if(nums[mid] == target)
            return mid; 
        else if (nums[mid] < target)
            left = mid + 1; 
        else if (nums[mid] > target)
            right = mid - 1;
    }
    return -1;
}
```

### `n` 数之和

看下力扣第 167 题「两数之和 II」：

<Problem slug="two-sum-ii-input-array-is-sorted" />

只要数组有序，就应该想到双指针技巧。这道题的解法有点类似二分查找，通过调节 `left` 和 `right` 就可以调整 `sum` 的大小：

```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // 一左一右两个指针相向而行
        int left = 0, right = numbers.length - 1;
        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum == target) {
                // 题目要求的索引是从 1 开始的
                return new int[]{left + 1, right + 1};
            } else if (sum < target) {
                // 让 sum 大一点
                left++;
            } else if (sum > target) {
                // 让 sum 小一点
                right--;
            }
        }
        return new int[]{-1, -1};
    }
}
```

我在另一篇文章 [一个函数秒杀所有 nSum 问题](https://labuladong.online/algo/practice-in-action/nsum/) 中也运用类似的左右指针技巧给出了 `nSum` 问题的一种通用思路，本质上利用的也是双指针技巧。

### 反转数组

一般编程语言都会提供 `reverse` 函数，其实这个函数的原理非常简单，力扣第 344 题「反转字符串」就是类似的需求，让你反转一个 `char[]` 类型的字符数组，我们直接看代码吧：

```java
void reverseString(char[] s) {
    // 一左一右两个指针相向而行
    int left = 0, right = s.length - 1;
    while (left < right) {
        // 交换 s[left] 和 s[right]
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        left++;
        right--;
    }
}
```

关于数组翻转的更多进阶问题，可以参见 [二维数组的花式遍历](https://labuladong.online/algo/practice-in-action/2d-array-traversal-summary/)。

### 回文串判断

回文串就是正着读和反着读都一样的字符串。比如说字符串 `aba` 和 `abba` 都是回文串，因为它们对称，反过来还是和本身一样；反之，字符串 `abac` 就不是回文串。

现在你应该能感觉到回文串问题和左右指针肯定有密切的联系，比如让你判断一个字符串是不是回文串，你可以写出下面这段代码：

```java
boolean isPalindrome(String s) {
    // 一左一右两个指针相向而行
    int left = 0, right = s.length() - 1;
    while (left < right) {
        if (s.charAt(left) != s.charAt(right)) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
```

那接下来我提升一点难度，给你一个字符串，让你用双指针技巧从中找出最长的回文串，你会做吗？

这就是力扣第 5 题「最长回文子串」：

<Problem slug="longest-palindromic-substring" />

函数签名如下：

```java
String longestPalindrome(String s);
```

找回文串的难点在于，回文串的的长度可能是奇数也可能是偶数，解决该问题的核心是**从中心向两端扩散的双指针技巧**。

如果回文串的长度为奇数，则它有一个中心字符；如果回文串的长度为偶数，则可以认为它有两个中心字符。所以我们可以先实现这样一个函数：

```java
// 在 s 中寻找以 s[l] 和 s[r] 为中心的最长回文串
String palindrome(String s, int l, int r) {
    // 防止索引越界
    while (l >= 0 && r < s.length()
            && s.charAt(l) == s.charAt(r)) {
        // 双指针，向两边展开
        l--; r++;
    }
    // 返回以 s[l] 和 s[r] 为中心的最长回文串
    return s.substring(l + 1, r);
}
```

这样，如果输入相同的 `l` 和 `r`，就相当于寻找长度为奇数的回文串，如果输入相邻的 `l` 和 `r`，则相当于寻找长度为偶数的回文串。

那么回到最长回文串的问题，解法的大致思路就是：

```python
for 0 <= i < len(s):
    找到以 s[i] 为中心的回文串
    找到以 s[i] 和 s[i+1] 为中心的回文串
    更新答案
```

翻译成代码，就可以解决最长回文子串这个问题：

```java
String longestPalindrome(String s) {
    String res = "";
    for (int i = 0; i < s.length(); i++) {
        // 以 s[i] 为中心的最长回文子串
        String s1 = palindrome(s, i, i);
        // 以 s[i] 和 s[i+1] 为中心的最长回文子串
        String s2 = palindrome(s, i, i + 1);
        // res = longest(res, s1, s2)
        res = res.length() > s1.length() ? res : s1;
        res = res.length() > s2.length() ? res : s2;
    }
    return res;
}
```

<visual slug='longest-palindromic-substring' >

你可以点开下面的可视化面板，多次点击 <code type="click">while (l >= 0 && r < s.length && s[l] === s[r])</code> 这一行代码，即可看到 `l, r` 两个指针向两边展开的过程：

</visual>

你应该能发现最长回文子串使用的左右指针和之前题目的左右指针有一些不同：之前的左右指针都是从两端向中间相向而行，而回文子串问题则是让左右指针从中心向两端扩展。不过这种情况也就回文串这类问题会遇到，所以我也把它归为左右指针了。

到这里，数组相关的双指针技巧就全部讲完了，这些技巧的更多扩展延伸见 [更多数组双指针经典高频题](https://labuladong.online/algo/problem-set/array-two-pointers/)。







<hr>
<details class="hint-container details">
<summary><strong>引用本文的文章</strong></summary>

 - [【强化练习】二分搜索算法经典习题](https://labuladong.online/algo/problem-set/binary-search/)
 - [【强化练习】哈希表更多习题](https://labuladong.online/algo/problem-set/hash-table/)
 - [【强化练习】回溯算法经典习题 I](https://labuladong.online/algo/problem-set/backtrack-i/)
 - [【强化练习】回溯算法经典习题 III](https://labuladong.online/algo/problem-set/backtrack-iii/)
 - [【强化练习】数学技巧相关习题](https://labuladong.online/algo/problem-set/math-tricks/)
 - [【强化练习】数组双指针经典习题](https://labuladong.online/algo/problem-set/array-two-pointers/)
 - [【强化练习】更多经典设计习题](https://labuladong.online/algo/problem-set/ds-design/)
 - [【强化练习】链表双指针经典习题](https://labuladong.online/algo/problem-set/linkedlist-two-pointers/)
 - [一个方法团灭 nSum 问题](https://labuladong.online/algo/practice-in-action/nsum/)
 - [二维数组的花式遍历技巧](https://labuladong.online/algo/practice-in-action/2d-array-traversal-summary/)
 - [动态规划之子序列问题解题模板](https://labuladong.online/algo/dynamic-programming/subsequence-problem/)
 - [博采众长：桶排序](https://labuladong.online/algo/data-structure-basic/bucket-sort/)
 - [如何判断回文链表](https://labuladong.online/algo/data-structure/palindrome-linked-list/)
 - [如何高效解决接雨水问题](https://labuladong.online/algo/frequency-interview/trapping-rain-water/)
 - [妙用二叉树前序位置：快速排序](https://labuladong.online/algo/data-structure-basic/quick-sort/)
 - [学习数据结构和算法的框架思维](https://labuladong.online/algo/essential-technique/algorithm-summary/)
 - [扫描线技巧：安排会议室](https://labuladong.online/algo/frequency-interview/scan-line-technique/)
 - [拓展：数组去重问题（困难版）](https://labuladong.online/algo/frequency-interview/remove-duplicate-letters/)
 - [滑动窗口算法核心代码模板](https://labuladong.online/algo/essential-technique/sliding-window-framework/)
 - [用算法打败算法](https://labuladong.online/algo/fname.html?fname=PDF中的算法)
 - [田忌赛马背后的算法决策](https://labuladong.online/algo/practice-in-action/advantage-shuffle/)
 - [算法刷题的重点和坑](https://labuladong.online/algo/intro/how-to-learn-algorithms/)
 - [算法时空复杂度分析实用指南](https://labuladong.online/algo/essential-technique/complexity-analysis/)
 - [算法笔试「骗分」套路](https://labuladong.online/algo/other-skills/tips-in-exam/)

</details><hr>




<hr>
<details class="hint-container details">
<summary><strong>引用本文的题目</strong></summary>

<strong>安装 [我的 Chrome 刷题插件](https://labuladong.online/algo/intro/chrome/) 点开下列题目可直接查看解题思路：</strong>

| LeetCode | 力扣 | 难度 |
| :----: | :----: | :----: |
| [1. Two Sum](https://leetcode.com/problems/two-sum/?show=1) | [1. 两数之和](https://leetcode.cn/problems/two-sum/?show=1) | 🟢 |
| [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/?show=1) | [125. 验证回文串](https://leetcode.cn/problems/valid-palindrome/?show=1) | 🟢 |
| [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/?show=1) | [131. 分割回文串](https://leetcode.cn/problems/palindrome-partitioning/?show=1) | 🟠 |
| [267. Palindrome Permutation II](https://leetcode.com/problems/palindrome-permutation-ii/?show=1)🔒 | [267. 回文排列 II](https://leetcode.cn/problems/palindrome-permutation-ii/?show=1)🔒 | 🟠 |
| [281. Zigzag Iterator](https://leetcode.com/problems/zigzag-iterator/?show=1)🔒 | [281. 锯齿迭代器](https://leetcode.cn/problems/zigzag-iterator/?show=1)🔒 | 🟠 |
| [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/?show=1) | [42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/?show=1) | 🔴 |
| [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/?show=1) | [543. 二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/?show=1) | 🟢 |
| [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/?show=1) | [658. 找到 K 个最接近的元素](https://leetcode.cn/problems/find-k-closest-elements/?show=1) | 🟠 |
| [75. Sort Colors](https://leetcode.com/problems/sort-colors/?show=1) | [75. 颜色分类](https://leetcode.cn/problems/sort-colors/?show=1) | 🟠 |
| [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?show=1) | [80. 删除有序数组中的重复项 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/?show=1) | 🟠 |
| [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/?show=1) | [82. 删除排序链表中的重复元素 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/?show=1) | 🟠 |
| [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/?show=1) | [9. 回文数](https://leetcode.cn/problems/palindrome-number/?show=1) | 🟢 |
| - | [剑指 Offer 21. 调整数组顺序使奇数位于偶数前面](https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/?show=1) | 🟢 |
| - | [剑指 Offer 57. 和为s的两个数字](https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/?show=1) | 🟢 |
| - | [剑指 Offer II 018. 有效的回文](https://leetcode.cn/problems/XltzEq/?show=1) | 🟢 |

</details>
<hr>



**＿＿＿＿＿＿＿＿＿＿＿＿＿**



![](https://labuladong.online/algo/images/souyisou2.png)