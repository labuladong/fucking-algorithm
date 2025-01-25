# 二维数组的花式遍历技巧



![](https://labuladong.online/algo/images/souyisou1.png)

**通知：为满足广大读者的需求，网站上架 [速成目录](https://labuladong.online/algo/intro/quick-learning-plan/)，如有需要可以看下，谢谢大家的支持~另外，建议你在我的 [网站](https://labuladong.online/algo/) 学习文章，体验更好。**



读完本文，你不仅学会了算法套路，还可以顺便解决如下题目：

| LeetCode | 力扣 | 难度 |
| :----: | :----: | :----: |
| [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) | [151. 反转字符串中的单词](https://leetcode.cn/problems/reverse-words-in-a-string/) | 🟠 |
| [48. Rotate Image](https://leetcode.com/problems/rotate-image/) | [48. 旋转图像](https://leetcode.cn/problems/rotate-image/) | 🟠 |
| [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | [54. 螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/) | 🟠 |
| [59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/) | [59. 螺旋矩阵 II](https://leetcode.cn/problems/spiral-matrix-ii/) | 🟠 |
| [61. Rotate List](https://leetcode.com/problems/rotate-list/) | [61. 旋转链表](https://leetcode.cn/problems/rotate-list/) | 🟠 |
| - | [剑指 Offer 29. 顺时针打印矩阵](https://leetcode.cn/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/) | 🟢 |

**-----------**



> [!NOTE]
> 阅读本文前，你需要先学习：
> 
> - [数组基础](https://labuladong.online/algo/data-structure-basic/array-basic/)

有些读者说，看了本站的很多文章，掌握了框架思维，可以解决大部分有套路框架可循的题目。

但是框架思维也不是万能的，有一些特定技巧呢，属于会者不难，难者不会的类型，只能通过多刷题进行总结和积累。

那么本文我分享一些巧妙的二维数组的花式操作，你只要有个印象，以后遇到类似题目就不会懵圈了。

## 顺/逆时针旋转矩阵

对二维数组进行旋转是常见的笔试题，力扣第 48 题「旋转图像」就是很经典的一道：

<Problem slug="rotate-image" />

题目很好理解，就是让你将一个二维矩阵顺时针旋转 90 度，**难点在于要「原地」修改**，函数签名如下：

```java
void rotate(int[][] matrix)
```

如何「原地」旋转二维矩阵？稍想一下，感觉操作起来非常复杂，可能要设置巧妙的算法机制来「一圈一圈」旋转矩阵：

![](https://labuladong.online/algo/images/2d-array/1.png)

**但实际上，这道题不能走寻常路**，在讲巧妙解法之前，我们先看另一道谷歌曾经考过的算法题热热身：

给你一个包含若干单词和空格的字符串 `s`，请你写一个算法，**原地**反转所有单词的顺序。

比如说，给你输入这样一个字符串：

```shell
s = "hello world labuladong"
```

你的算法需要**原地**反转这个字符串中的单词顺序：

```shell
s = "labuladong world hello"
```

常规的方式是把 `s` 按空格 `split` 成若干单词，然后 `reverse` 这些单词的顺序，最后把这些单词 `join` 成句子。但这种方式使用了额外的空间，并不是「原地反转」单词。

**正确的做法是，先将整个字符串 `s` 反转**：

```shell
s = "gnodalubal dlrow olleh"
```

**然后将每个单词分别反转**：

```shell
s = "labuladong world hello"
```







这样，就实现了原地反转所有单词顺序的目的。力扣第 151 题「颠倒字符串中的单词」就是类似的问题，你可以顺便去做一下。

上面这个小技巧还可以再包装包装，比如说你可以去看一下力扣第 61 题「旋转链表」：给你一个单链表，让你旋转链表，将链表每个节点向右移动 `k` 个位置。

比如说输入单链表 `1 -> 2 -> 3 -> 4 -> 5`，`k = 2`，你的算法需要返回 `4 -> 5 -> 1 -> 2 -> 3`，即将链表每个节点向右移动 2 个位置。

这个题，不要真傻乎乎地一个一个去移动链表节点，我给你翻译翻译，其实就是将链表的后 `k` 个节点移动到链表的头部嘛，反应过来没有？

还没反应过来，那再提示一下，把后 `k` 个节点移动到链表的头部，其实就是让你把链表的前 `n - k` 个节点和后 `k` 个节点原地翻转，对不对？

这样，是不是和前面说的原地翻转字符串中的单词是一样的道理呢？你只需要先将整个链表反转，然后将前 `n - k` 个节点和后 `k` 个节点分别反转，就得到了结果。

当然，这个题有一些小细节，比如这个 `k` 可能大于链表的长度，那么你需要先求出链表的长度 `n`，然后取模 `k = k % n`，这样 `k` 就不会大于链表的长度，且最后得到的结果也是正确的。

有时间的话自己去做一下这个题吧，比较简单，我这里就不贴代码了。

我讲上面这两道题的目的是什么呢？

**旨在说明，有时候咱们拍脑袋的常规思维，在计算机看来可能并不是最优雅的；但是计算机觉得最优雅的思维，对咱们来说却不那么直观**。也许这就是算法的魅力所在吧。







回到之前说的顺时针旋转二维矩阵的问题，常规的思路就是去寻找原始坐标和旋转后坐标的映射规律，但我们是否可以让思维跳跃跳跃，尝试把矩阵进行反转、镜像对称等操作，可能会出现新的突破口。

**我们可以先将 `n x n` 矩阵 `matrix` 按照左上到右下的对角线进行镜像对称**：

![](https://labuladong.online/algo/images/2d-array/2.jpeg)

**然后再对矩阵的每一行进行反转**：

![](https://labuladong.online/algo/images/2d-array/3.jpeg)

**发现结果就是 `matrix` 顺时针旋转 90 度的结果**：

![](https://labuladong.online/algo/images/2d-array/4.jpeg)

将上述思路翻译成代码，即可解决本题：

```java
class Solution {
    // 将二维矩阵原地顺时针旋转 90 度
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        // 先沿对角线镜像对称二维矩阵
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                // swap(matrix[i][j], matrix[j][i]);
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        // 然后反转二维矩阵的每一行
        for (int[] row : matrix) {
            reverse(row);
        }
    }

    // 反转一维数组
    void reverse(int[] arr) {
        int i = 0, j = arr.length - 1;
        while (j > i) {
            // swap(arr[i], arr[j]);
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }
}
```

<visual slug='rotate-image'>

你可以打开下面的可视化面板，多次点击 <code type="click">let temp = matrix[i][j]</code> 这行代码，即可看到对角线翻转的过程；然后再多次点击 <code type="click">reverse(row)</code> 这行代码，即可看到每一行被反转，得到最终答案：

</visual>

肯定有读者会问，如果没有做过这道题，怎么可能想到这种思路呢？

是的，没做过这类题目，确实不好想到这种思路，但你这不是做过了么？所谓会者不难难者不会，你这辈子估计都忘不掉了。

**既然说道这里，我们可以发散一下，如何将矩阵逆时针旋转 90 度呢**？

思路是类似的，只要通过另一条对角线镜像对称矩阵，然后再反转每一行，就得到了逆时针旋转矩阵的结果：

![](https://labuladong.online/algo/images/2d-array/5.jpeg)

翻译成代码如下：

```java
class Solution {

    // 将二维矩阵原地逆时针旋转 90 度
    public void rotate2(int[][] matrix) {
        int n = matrix.length;
        // 沿左下到右上的对角线镜像对称二维矩阵
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i; j++) {
                // swap(matrix[i][j], matrix[n-j-1][n-i-1])
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n - j - 1][n - i - 1];
                matrix[n - j - 1][n - i - 1] = temp;
            }
        }
        // 然后反转二维矩阵的每一行
        for (int[] row : matrix) {
            reverse(row);
        }
    }

    void reverse(int[] arr) {
        // 见上文
    }
}
```

至此，旋转矩阵的问题就解决了。

## 矩阵的螺旋遍历

接下来我们讲一下力扣第 54 题「螺旋矩阵」，看一看二维矩阵可以如何花式遍历：





<Problem slug="spiral-matrix" />

```java
// 函数签名如下
List<Integer> spiralOrder(int[][] matrix)
```

**解题的核心思路是按照右、下、左、上的顺序遍历数组，并使用四个变量圈定未遍历元素的边界**：

![](https://labuladong.online/algo/images/2d-array/6.png)

随着螺旋遍历，相应的边界会收缩，直到螺旋遍历完整个数组：

![](https://labuladong.online/algo/images/2d-array/7.png)

只要有了这个思路，翻译出代码就很容易了：

```java
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int upper_bound = 0, lower_bound = m - 1;
        int left_bound = 0, right_bound = n - 1;
        List<Integer> res = new LinkedList<>();
        // res.size() == m * n 则遍历完整个数组
        while (res.size() < m * n) {
            if (upper_bound <= lower_bound) {
                // 在顶部从左向右遍历
                for (int j = left_bound; j <= right_bound; j++) {
                    res.add(matrix[upper_bound][j]);
                }
                // 上边界下移
                upper_bound++;
            }
            
            if (left_bound <= right_bound) {
                // 在右侧从上向下遍历
                for (int i = upper_bound; i <= lower_bound; i++) {
                    res.add(matrix[i][right_bound]);
                }
                // 右边界左移
                right_bound--;
            }
            
            if (upper_bound <= lower_bound) {
                // 在底部从右向左遍历
                for (int j = right_bound; j >= left_bound; j--) {
                    res.add(matrix[lower_bound][j]);
                }
                // 下边界上移
                lower_bound--;
            }
            
            if (left_bound <= right_bound) {
                // 在左侧从下向上遍历
                for (int i = lower_bound; i >= upper_bound; i--) {
                    res.add(matrix[i][left_bound]);
                }
                // 左边界右移
                left_bound++;
            }
        }
        return res;
    }
}
```

<visual slug='spiral-matrix' >

你可以打开下面的可视化面板，多次点击 <code type="click">while (res.length < m * n)</code> 这行代码，即可看到由外向内螺旋遍历的过程：

</visual>

力扣第 59 题「螺旋矩阵 II」也是类似的题目，只不过是反过来，让你按照螺旋的顺序生成矩阵：





<Problem slug="spiral-matrix-ii" />

```java
// 函数签名如下
int[][] generateMatrix(int n)
```

有了上面的铺垫，稍微改一下代码即可完成这道题：

```java
class Solution {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        int upper_bound = 0, lower_bound = n - 1;
        int left_bound = 0, right_bound = n - 1;
        // 需要填入矩阵的数字
        int num = 1;
        
        while (num <= n * n) {
            if (upper_bound <= lower_bound) {
                // 在顶部从左向右遍历
                for (int j = left_bound; j <= right_bound; j++) {
                    matrix[upper_bound][j] = num++;
                }
                // 上边界下移
                upper_bound++;
            }
            
            if (left_bound <= right_bound) {
                // 在右侧从上向下遍历
                for (int i = upper_bound; i <= lower_bound; i++) {
                    matrix[i][right_bound] = num++;
                }
                // 右边界左移
                right_bound--;
            }
            
            if (upper_bound <= lower_bound) {
                // 在底部从右向左遍历
                for (int j = right_bound; j >= left_bound; j--) {
                    matrix[lower_bound][j] = num++;
                }
                // 下边界上移
                lower_bound--;
            }
            
            if (left_bound <= right_bound) {
                // 在左侧从下向上遍历
                for (int i = lower_bound; i >= upper_bound; i--) {
                    matrix[i][left_bound] = num++;
                }
                // 左边界右移
                left_bound++;
            }
        }
        return matrix;
    }
}
```

<visual slug='spiral-matrix-ii' >

你可以打开下面的可视化面板，多次点击 <code type="click">while (num <= n * n)</code> 这行代码，即可看到生成螺旋矩阵的过程：

</visual>

至此，两道螺旋矩阵的题目也解决了。

以上就是遍历二维数组的一些技巧，其他数组技巧可参见之前的文章 [前缀和数组](https://labuladong.online/algo/data-structure/prefix-sum/)，[差分数组](https://labuladong.online/algo/data-structure/diff-array/)，[数组双指针算法集合](https://labuladong.online/algo/essential-technique/array-two-pointers-summary/)，链表相关技巧可参见 [单链表六大算法技巧汇总](https://labuladong.online/algo/essential-technique/linked-list-skills-summary/)。 









<hr>
<details class="hint-container details">
<summary><strong>引用本文的文章</strong></summary>

 - [【强化练习】数组双指针经典习题](https://labuladong.online/algo/problem-set/array-two-pointers/)
 - [双指针技巧秒杀七道数组题目](https://labuladong.online/algo/essential-technique/array-two-pointers-summary/)

</details><hr>




<hr>
<details class="hint-container details">
<summary><strong>引用本文的题目</strong></summary>

<strong>安装 [我的 Chrome 刷题插件](https://labuladong.online/algo/intro/chrome/) 点开下列题目可直接查看解题思路：</strong>

| LeetCode | 力扣 | 难度 |
| :----: | :----: | :----: |
| [1260. Shift 2D Grid](https://leetcode.com/problems/shift-2d-grid/?show=1) | [1260. 二维网格迁移](https://leetcode.cn/problems/shift-2d-grid/?show=1) | 🟢 |
| [1329. Sort the Matrix Diagonally](https://leetcode.com/problems/sort-the-matrix-diagonally/?show=1) | [1329. 将矩阵按对角线排序](https://leetcode.cn/problems/sort-the-matrix-diagonally/?show=1) | 🟠 |
| [867. Transpose Matrix](https://leetcode.com/problems/transpose-matrix/?show=1) | [867. 转置矩阵](https://leetcode.cn/problems/transpose-matrix/?show=1) | 🟢 |
| - | [剑指 Offer 58 - I. 翻转单词顺序](https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof/?show=1) | 🟢 |

</details>
<hr>



**＿＿＿＿＿＿＿＿＿＿＿＿＿**



![](https://labuladong.online/algo/images/souyisou2.png)