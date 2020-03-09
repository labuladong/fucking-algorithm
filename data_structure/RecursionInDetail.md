# Clarify the concept of recursion

**Translator: [MasonShu](https://greenwichmt.github.io/)**

**Author: [labuladong](https://github.com/labuladong)**

What's the difference and connections between recursion, divide-and-conquer algorithm, dynamic programming, and greedy algorithm? If you haven't made it clear. Doesn't matter! I would give you a brief introduction to kick off this section.

Recursion is a programming technique. It's a way of thinking about solving problems. There're two algorithmic ideas to solve specific problems: divide-and-conquer algorithm and dynamic programming. They're largely based on recursive thinking (although the final version of dynamic programming is rarely recursive, the problem-solving idea is still inseparable from recursion). There's also an algorithmic idea called greedy algorithm which can efficiently solve some more special problems. And it's a subset of dynamic programming algorithms.

The divide-and-conquer algorithm will be explained in this section. Taking the most classic merge sort as an example, it continuously divides the unsorted array into smaller sub-problems. This is the origin of the word **divide and conquer**. Obviously, the sub-problems decomposed by the ranking problem are non-repeating. If some of the sub-problems after decomposition are duplicated (the nature of overlapping sub-problems), then the dynamic programming algorithm is used to solve them!

## Recursion in detail

Before introducing divide and conquer algorithm, we must first understand the concept of recursion.

The basic idea of recursion is that a function calls itself directly or indirectly, which transforms the solution of the original problem into many smaller sub-problems of the same nature. All we need is to focus on how to divide the original problem into qualified sub-problems, rather than study how this sub-problem is solved. The difference between recursion and enumeration is that enumeration divides the problem horizontally and then solves the sub-problems one by one, but recursion divides the problem vertically and then solves the sub-problems hierarchily.

The following illustrates my understanding of recursion. **If you don't want to read, please just remember how to answer these questions:**

1. How to sort a bunch of numbers? Answer: Divided into two halves, first align the left half, then the right half, and finally merge. As for how to arrange the left and right half, please read this sentence again.
2. How many hairs does Monkey King have? Answer: One plus the rest.
3. How old are you this year? Answer: One year plus my age of last year, I was born in 1999.

Two of the most important characteristics of recursive code: **end conditions and self-invocation**. Self-invocation is aimed at solving sub-problems, and the end condition defines the answer to the simplest sub-problem.


```c++
int func(How old are you this year) {
    // simplest sub-problem, end condition
    if (this year equals 1999) return my age 0;
    // self-calling to decompose problem
    return func(How old are you last year) + 1;   
}
```

Actually think about it, **what is the most successful application of recursion? I think it's mathematical induction**. Most of us learned mathematical induction in high school. The usage scenario is probably: we can't figure out a summation formula, but we tried a few small numbers which seemed containing a kinda law, and then we compiled a formula. We ourselves think it shall be the correct answer. However, mathematics is very rigorous. Even if you've tried 10,000 cases which are correct, can you guarantee the 10001th correct? This requires mathematical induction to exert its power. Assuming that the formula we compiled is true at the kth number, furthermore if it is proved correct at the k + 1th, then the formula we have compiled is verified correct.

So what is the connection between mathematical induction and recursion? We just said that the recursive code must have an end condition. If not, it will fall into endless self-calling hell until the memory exhausted. The difficulty of mathematical proof is that you can try to have a finite number of cases, but it is difficult to extend your conclusion to infinity. Here you can see the connection-infinite.

The essence of recursive code is to call itself to solve smaller sub-problems until the end condition is reached. The reason why mathematical induction is useful is to continuously increase our guess by one, and expand the size of the conclusion, without end condition. So by extending the conclusion to infinity, the proof of the correctness of the guess is completed.

### Why learn recursion

First to train the ability to think reversely. Recursive thinking is the thinking of normal people, always looking at the problems in front of them and thinking about solutions, and the solution is the future tense; Recursive thinking forces us to think reversely, see the end of the problem, and treat the problem-solving process as the past tense.

Second, practice analyzing the structure of the problem. When the problem can be broken down into sub problems of the same structure, you can acutely find this feature, and then solve it efficiently.

Third, go beyond the details and look at the problem as a whole. Let's talk about merge and sort. In fact, you can divide the left and right areas without recursion, but the cost is that the code is extremely difficult to understand. Take a look at the code below (merge sorting will be described later. You can understand the meaning here, and appreciate the beauty of recursion).

```java
void sort(Comparable[] a){    
    int N = a.length;
    // So complicated! It shows disrespect for sorting. I refuse to study such code.
    for (int sz = 1; sz < N; sz = sz + sz)
        for (int lo = 0; lo < N - sz; lo += sz + sz)
            merge(a, lo, lo + sz - 1, Math.min(lo + sz + sz - 1, N - 1));
}

/* I prefer recursion, simple and beautiful */
void sort(Comparable[] a, int lo, int hi) {
    if (lo >= hi) return;
    int mid = lo + (hi - lo) / 2;
    sort(a, lo, mid); // soft left part
    sort(a, mid + 1, hi); // soft right part
    merge(a, lo, mid, hi); // merge the two sides
}

```

Looks simple and beautiful is one aspect, the key is **very interpretable**: sort the left half, sort the right half, and finally merge the two sides. The non-recursive version looks unintelligible, full of various incomprehensible boundary calculation details, is particularly prone to bugs and difficult to debug. Life is short, i prefer the recursive version.

Obviously, sometimes recursive processing is efficient, such as merge sort, **sometimes inefficient**, such as counting the hair of Monkey King, because the stack consumes extra space but simple inference does not consume space. Example below gives a linked list header and calculate its length:

```java
/* Typical recursive traversal framework requires extra space O(1) */
public int size(Node head) {
    int size = 0;
    for (Node p = head; p != null; p = p.next) size++;
    return size;
}
/* I insist on recursion facing every problem. I need extra space O(N) */
public int size(Node head) {
    if (head == null) return 0;
    return size(head.next) + 1;
}
```

### Tips for writing recursion

My point of view: **Understand what a function does and believe it can accomplish this task. Don't try to jump into the details.** Do not jump into this function to try to explore more details, otherwise you will fall into infinite details and cannot extricate yourself. The human brain carries tiny sized stack!

Let's start with the simplest example: traversing a binary tree.

```cpp
void traverse(TreeNode* root) {
    if (root == nullptr) return;
    traverse(root->left);
    traverse(root->right);
}
```

Above few lines of code are enough to wipe out any binary tree. What I want to say is that for the recursive function `traverse (root)`, we just need to believe: give it a root node `root`, and it can traverse the whole tree. Since this function is written for this specific purpose, so we just need to dump the left and right nodes of this node to this function, because I believe it can surely complete the task. What about traversing an N-fork tree? It's too simple, exactly the same as a binary tree!

```cpp
void traverse(TreeNode* root) {
    if (root == nullptr) return;
    for (child : root->children)
        traverse(child);
}
```

As for pre-order, mid-order, post-order traversal, they are all obvious. For N-fork tree, there is obviously no in-order traversal.


The following **explains a problem from LeetCode in detail**: Given a binary tree and a target value, the values in every node is positive or negative, return the number of paths in the tree that are equal to the target value, let you write the pathSum function:

```
/* from LeetCode PathSum III： https://leetcode.com/problems/path-sum-iii/ */
root = [10,5,-3,3,2,null,11,3,-2,null,1],
sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
```

```cpp
/* It doesn’t matter if you don’t understand, there is a more detailed analysis version below, which highlights the conciseness and beauty of recursion. */
int pathSum(TreeNode root, int sum) {
    if (root == null) return 0;
    return count(root, sum) + 
        pathSum(root.left, sum) + pathSum(root.right, sum);
}
int count(TreeNode node, int sum) {
    if (node == null) return 0;
    return (node.val == sum) + 
        count(node.left, sum - node.val) + count(node.right, sum - node.val);
}
```

The problem may seem complicated, but the code is extremely concise, which is the charm of recursion. Let me briefly summarize the **solution process** of this problem:

First of all, it is clear that to solve the problem of recursive tree, you must traverse the entire tree. So the traversal framework of the binary tree (recursively calling the function itself on the left and right children) must appear in the main function pathSum. And then, what should they do for each node? They should see how many eligible paths they and their little children have under their feet. Well, this question is clear.

According to the techniques mentioned earlier, define what each recursive function should do based on the analysis just now:

PathSum function: Give it a node and a target value. It returns the total number of paths in the tree rooted at this node and the target value.

Count function: Give it a node and a target value. It returns a tree rooted at this node, and can make up the total number of paths starting with the node and the target value.

```cpp
/* With above tips, comment out the code in detail */
int pathSum(TreeNode root, int sum) {
    if (root == null) return 0;
    int pathImLeading = count(root, sum); // Number of paths beginning with itself
    int leftPathSum = pathSum(root.left, sum); // The total number of paths on the left (Believe he can figure it out)
    int rightPathSum = pathSum(root.right, sum); // The total number of paths on the right (Believe he can figure it out)
    return leftPathSum + rightPathSum + pathImLeading;
}
int count(TreeNode node, int sum) {
    if (node == null) return 0;
    // Can I stand on my own as a separate path?
    int isMe = (node.val == sum) ? 1 : 0;
    // Left brother, how many sum-node.val can you put together?
    int leftBrother = count(node.left, sum - node.val); 
    // Right brother, how many sum-node.val can you put together?
    int rightBrother = count(node.right, sum - node.val);
    return  isMe + leftBrother + rightBrother; // all count i can make up
}
```

Again, understand what each function can do and trust that they can do it.

In summary, the binary tree traversal framework provided by the PathSum function calls the count function for each node during the traversal. Can you see the pre-order traversal (the order is the same for this question)? The count function is also a binary tree traversal, used to find the target value path starting with this node. Understand it deeply!

## Divide and conquer algorithm

**Merge and sort**, typical divide-and-conquer algorithm; divide-and-conquer, typical recursive structure.

The divide-and-conquer algorithm can go in three steps: decomposition-> solve-> merge

1. Decompose the original problem into sub-problems with the same structure.
2. After decomposing to an easy-to-solve boundary, perform a recursive solution.
3. Combine the solutions of the subproblems into the solutions of the original problem.

To merge and sort, let's call this function `merge_sort`. According to what we said above, we must clarify the responsibility of the function, that is, **sort an incoming array**. OK, can this problem be solved? Of course! Sorting an array is just the same to sorting the two halves of the array separately, and then merging the two halves.

```cpp
void merge_sort(an array) {
    if (some tiny array easy to solve) return;
    merge_sort(left half array);
    merge_sort(right half array);
    merge(left half array, right half array);
}
```

Well, this algorithm is like this, there is no difficulty at all. Remember what I said before, believe in the function's ability, and pass it to him half of the array, then the half of the array is already sorted. Have you found it's a binary tree traversal template? Why it is postorder traversal? Because the routine of our divide-and-conquer algorithm is **decomposition-> solve (bottom)-> merge (backtracking)** Ah, first left and right decomposition, and then processing merge, backtracking is popping stack, which is equivalent to post-order traversal. As for the `merge` function, referring to the merging of two ordered linked lists, they are exactly the same, and the code is directly posted below.

Let's refer to the Java code in book `Algorithm 4` below, which is pretty. This shows that not only algorithmic thinking is important, but coding skills are also very important! Think more and imitate more.

```java
public class Merge {
    // Do not construct new arrays in the merge function, because the merge function will be called multiple times, affecting performance.Construct a large enough array directly at once, concise and efficient.
    private static Comparable[] aux;

     public static void sort(Comparable[] a) {
        aux = new Comparable[a.length];
        sort(a, 0, a.length - 1);
    }

    private static void sort(Comparable[] a, int lo, int hi) {
        if (lo >= hi) return;
        int mid = lo + (hi - lo) / 2;
        sort(a, lo, mid);
        sort(a, mid + 1, hi);
        merge(a, lo, mid, hi);
    }

    private static void merge(Comparable[] a, int lo, int mid, int hi) {
        int i = lo, j = mid + 1;
        for (int k = lo; k <= hi; k++)
            aux[k] = a[k];
        for (int k = lo; k <= hi; k++) {
            if      (i > mid)              { a[k] = aux[j++]; }
            else if (j > hi)               { a[k] = aux[i++]; }
            else if (less(aux[j], aux[i])) { a[k] = aux[j++]; }
            else                           { a[k] = aux[i++]; }
        }
    }

    private static boolean less(Comparable v, Comparable w) {
        return v.compareTo(w) < 0;
    }
}
```

LeetCode has a special exercise of the divide-and-conquer algorithm. Copy the link below to web browser and have a try:

https://leetcode.com/tag/divide-and-conquer/

