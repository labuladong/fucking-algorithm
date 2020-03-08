# Russian Doll Envelopes

**Translator: [Dong Wang](https://github.com/Coder2Programmer)**

**Author: [labuladong](https://github.com/labuladong)**

Many algorithm problems require sorting skills. The difficulty is not in the sort itself, but ingenious sorting for preprocessing, transforming the algorithm problems, and laying the foundation for subsequent operations.

The russian doll envelopes needs to be sorted according to specific rules, and then converted into a [Longest Incremental Subsequence Problem](../dynamic_programming/LongestIncrementalSubsequence.md). You can use the trick of previous text [Binary Search Detailed Explanation](binarySearch.md) to solve the problem.

### 1. Overview

Russian doll envelopes is a very interesting and often occurring problem in life. Let's look at the problem first:

You have a number of envelopes with widths and heights given as a pair of integers `(w, h)`. One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

<strong>Note:</strong>

Rotation is not allowed.

<strong>Example:</strong>
<pre>
<strong>Input:</strong> [[5,4],[6,4],[6,7],[2,3]]
<strong>Output:</strong> 3 
<strong>Explanation:</strong> The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
</pre>

This question is actually a variant of Longes Increasing Subsequence(LIS), because it is clear that each legal nesting is a large set of small, which is equivalent to finding a longest increasing subsequence , and its length is the maximum number of envelopes that can be nested.

But the difficulty is that the standard LIS algorithm can only find the longest subsequence in the array, and our envelope is represented by a two-dimensional number pair like `(w, h)`. How can we apply the LIS algorithm?

![0](../pictures/%E4%BF%A1%E5%B0%81%E5%B5%8C%E5%A5%97/0.jpg)

The reader may calculate the area by `w × h`, and then perform the standard LIS algorithm on the area. However, if you think about it a little, you will find that this is not possible. For example, `1 × 10` is greater than` 3 × 3`, but obviously such two envelopes cannot be nested inside each other.

### 2. Solution

The solution to this problem is relatively clever:

**First sort the width `w` in ascending order. If you encounter the same situation with` w`, sort in descending order by height `h`. Then use all `h` as an array, and calculate the length of LIS on this array is the answer.**

Draw a picture to understand, first sort these number pairs:

![1](../pictures/%E4%BF%A1%E5%B0%81%E5%B5%8C%E5%A5%97/1.jpg)

Then look for the longest increasing subsequence on `h`:

![2](../pictures/%E4%BF%A1%E5%B0%81%E5%B5%8C%E5%A5%97/2.jpg)

This subsequence is the optimal nesting scheme.

The key to this solution is that for pairs of the same width `w`, the height` h` is sorted in descending order. Because two envelopes of the same width cannot contain each other, reverse ordering guarantees that at most one of the pairs of the same `w` is selected.

The code as follow:

```java
// envelopes = [[w, h], [w, h]...]
public int maxEnvelopes(int[][] envelopes) {
    int n = envelopes.length;
    // sort by ascending width, and sort by descending height if the width are the same
    Arrays.sort(envelopes, new Comparator<int[]>() 
    {
        public int compare(int[] a, int[] b) {
            return a[0] == b[0] ? 
                b[1] - a[1] : a[0] - b[0];
        }
    });
    // find LIS on the height array
    int[] height = new int[n];
    for (int i = 0; i < n; i++)
        height[i] = envelopes[i][1];

    return lengthOfLIS(height);
}
```

Regarding the search method for the longest increasing subsequence, the dynamic programming solution was introduced in detail in the previous article, and the binary search solution was explained using a poker game. This article will not expand and directly apply the algorithm template:

```java
/* returns the length of LIS in nums */
public int lengthOfLIS(int[] nums) {
    int piles = 0, n = nums.length;
    int[] top = new int[n];
    for (int i = 0; i < n; i++) {
        // playing card to process
        int poker = nums[i];
        int left = 0, right = piles;
        // position to insert for binary search
        while (left < right) {
            int mid = (left + right) / 2;
            if (top[mid] >= poker)
                right = mid;
            else
                left = mid + 1;
        }
        if (left == piles) piles++;
        // put this playing cart on top of the pile
        top[left] = poker;
    }
    // the number of cards is the LIS length
    return piles;
}
```
For clarity, I divided the code into two functions. You can also merge them to save space in the `height` array.

The time complexity of this algorithm is *O(NlogN)*, because sorting and calculating LIS each takes *O(NlogN)*.

The space complexity is *O(N)*, because a `top` array is needed in the function to calculate LIS.

### 3. Conclusion

This problem is a hard-level problem, and its difficult lies  in sorting. The problem is transformed into a standard LIS problem after correct sorting, which is easy to solve.

In fact, this problem can also be extended to three dimensions. For example, instead of letting you nest envelopes, you need to nest boxes. Each box has three dimensions: length, width, and height. Can you count how many boxes can be nested?

We may think so, first find the nested sequence according to the idea of envelope nesting in the first two dimensions(length and width), and finally find LIS in the third dimension(height) of this sequence, and we should be able to calculate the answer.

In fact, this idea is wrong. This type of problem is called a *partial order problem*. Ascending to three dimensions will greatly increase the difficulty. An advanced data structure called *Binary Index Tree* is needed, and interested readers can search by themselves.

There are many algorithmic problems that need to be sorted and processed, and author is collating and summarizing. Hope this article is helpful to you.
