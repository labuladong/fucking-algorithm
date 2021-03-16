# Framework and thoughts about learning data structure and algorithm

Translator: [ForeverSolar](https://github.com/foreversolar)

Author: [labuladong](https://github.com/labuladong)

This is a revision of an article written a long time ago (titled "Thinking Framework for Learning Data Structures and Algorithms"). Don't worry if you did not read it, as this article will cover all topics presented previously, and will provide more code samples to teach you how to use the thinking framework.

Before we begin, here's a few things I want to get out of the way. The topics presented here are discussing common data structures, we are not participating in algorithmic competitions. I will only solve conventional problems. In addition, I must stress that what you are reading is a summary of my personal experience. No algorithm book will cover these topics, so I urge you, the reader to try and understand from my point of view; and not to dwell too much on the details. The reason for this is because this article aims to provide an overview on how to build a framework for thinking of data structure and algorithms.

This thinking framework will progress from an overall view to specific details, going from the top to the bottom, from the abstract to the concrete. These are universal. Thinking in this way will not only be more effective in learning data structure and algorithms, but also allow you to learn any other knowledge *effectively*.

### 1.Storage Methods of Data Structures

**There are only two ways to store data structures: Array (sequential storage) and Linked List (linked storage)**。

You might be thinking: Wait, what about other data structures, don't we have hash tables, stacks, queues, heaps, trees, graphs... and so on?

When we analyze problems, we must think recursively, from top to bottom, from abstract to concrete. Those data structures listed above are actually 「higher order data structures」, whereas arrays and lists are 「primitive structures」. This is because if you break down each of the data structures above, you will realize that they are all merely special operations done on top of primitive linked lists or arrays. The only difference being: the APIs (Application Programming Interface) that interact on the primitive data structures themselves.

Let's walk through an example for clarity. The「queue」 and 「stack」 data structure can be implemented with both linked lists and arrays:
- If we use an array to implement the queue and stack, we'll need to deal with the problem of expanding capacity when items are added, and shrinking capacity when items are removed. 
- If we instead use a linked list for implementation, then there is no need to do capacity management, rather more memory space is needed to store each node and the pointers to these nodes.

The same can be said for expressing a 「graph」as it can be implemented with both a linked list or an array. 
- An adjacency table is a linked list.
- An adjacency matrix is a two-dimensional array. 

Adjacency matrices are able to find connected components quickly and are able to exploit matrix operations to solve some problems. However, if the graph is spread out (sparse), then it will become very time-consuming. Adjacency tables (the one built with the linked list) are more space-saving, but cannot compete with the adjacency matrix in terms of efficiency for many of the operations.

A「hashtable」 maps keys onto a large array through a hash function. In order to solve a hash conflict when it occurs (>1 key maps to the same array location), 'chaining' is done by leveraging features of a linked list. This is a simple operation, with the downside of requiring extra space to store the pointer; on the other hand, 'linear probing' method leverages a feature of arrays, which is to have continuous allocation. This does not need the additional storage space for pointers, but the operation of linear probing is slightly more complex than chaining.

A「tree implemented with an array is a「heap」. This is because a「heap」 is a complete binary tree, using an array for storage is ideal as it does not need a node pointer, and the operations are simpler on an array; the another very common kind of「tree」is an implementation with a linked list. This is because it is not necessarily a complete binary tree, hence it is not suitable to use an array for storage. For this reason, based on the tree structure of the list, we are able to derive various ingenious designs, such as the binary search tree, AVL tree, red- black tree, interval tree, B tree, etc., to conquer with different problems.

Readers who know about Redis databases may also know that Redis provides lists, strings, collections and other common data structures. However, for each data structure, there are at least two underlying storage methods to facilitate the use of appropriate storage methods according to the actual situation of data storage.

In conclusion, there are many kinds of data structures. Even you can invent your own data structures, but the underlying storage is nothing but arrays or linked lists. **The advantages and disadvantages of the two are as follows:**

**Array** is compact and continuous storage, which can be accessed at random. Searching in an array allows corresponding elements to be found quickly through index, also saves storage space relative to the linked list. However, because of the continuous storage requirement, the memory space must be allocated sufficiently during the initial time, so if the array is to be expanded beyond this allocation, it needs to reallocate a larger space. This requires copying all the data from the previous allocation, hence the time complexity `O(n)`; if you want to insert and delete in the middle of the array, you must move all the data behind each time to maintain the index continuity, resulting in a time complexity of `O(n)`.

As the elements of the **linked list** are not continuous, rather the pointer points to the position of the next element, there is no expansion of the array. If you know the current element's previous and the next elements, manipulating the pointers will allow the deletion of the element or insertion a new element, with time complexity of `O(1)`. However, because the storage space is not continuous, you can't compute the address of the corresponding element according to an index, and so you can't access elements on the list randomly; furthermore, because each element must store a pointer to the location of the front (previous) and back (next) elements, the linked list consume more storage space relative to the array list.


### 2.Basic operations of data structure

For any data structure, its basic operations are no more than traversal + access, and being more concrete, these are: `add`, `delete`, `search` and `modify`.

**There are many kinds of data structures, but their purpose is to add, delete, search and modify them as efficiently as possible** in different application scenarios. Isn't this the sole purpose of data structures?

How to traverse + access? From a high level we can see that traversal and access of various data structures exist in two forms: linear and nonlinear.

Linear is represented by a for / while iteration, and nonlinear is represented by recursion. Furthermore, there are only the following frameworks:

Array traversal framework, typically in a linear iterative structure：

```java
void traverse(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        // iteratively visit arr[i]
    }
}
```

Linked list traversal framework has both iterative and recursive structure：

```java
/* Basic node of the single linked list */
class ListNode {
    int val;
    ListNode next;
}

void traverse(ListNode head) {
    for (ListNode p = head; p != null; p = p.next) {
        // iteratively visit p.val
    }
}

void traverse(ListNode head) {
    // recusively visit head.val
    traverse(head.next)
}
```

Binary tree traversal framework, typical nonlinear recursive traversal structure：

```java
/* Basic node of the binary tree */
class TreeNode {
    int val;
    TreeNode left, right;
}

void traverse(TreeNode root) {
    traverse(root.left)
    traverse(root.right)
}
```

Do you think the recursive traversal of binary tree is similar to that of linked list? Take a look at the binary tree structure and single linked list structure, is it similar? If there are more forks, will you traverse the n-tree?

The binary tree framework can be extended to the n-tree traversal framework：

```java
/* Basic node of the N-tree */
class TreeNode {
    int val;
    TreeNode[] children;
}

void traverse(TreeNode root) {
    for (TreeNode child : root.children)
        traverse(child)
}
```

N-tree traversal can then further be extended to graph traversal, because graph is a combination of several n-tree. You might be thinking: a circle/loop can appear in a graph? This is very easy to solve for. Simply mark a node as visited with a Boolean array. I will leave the code as an exercise to the reader.

**The so-called framework is a trick. Regardless if the operation is add, delete, insert or modify, thes codes can never be separated from the structure. You can take this structure as the general outline, then add code on to your framework according to the specific problem at hand. Let's see some specific examples below.**

### 3.Guidelines of Algorithm Exercises 

First of all, it should be clear that **data structure is a tool, and algorithm is a method to solve specific problems through appropriate tools**. That is to say, before learning algorithms, we need to at least understand the common data structures, along with their characteristics and defects.

So how to practice in Leetcode? This was covered in a previous article [the way to learning algorithm learning](ThewaytoAlgorithmlearning.md), which is to practice by topics, with perseverance. Since it's been almost a year since I last wrote that article, I'll skip the sentiments and get right to the point:  

**Do binary tree exercises first! Do binary tree exercises first! Do binary tree exercises first!** Many might not have interest in articles about data structures, rather putting more focus on topics such as backtracking, divide and conquer. A question might aware: Why should you do binary tree exercises first? **Because binary tree exercises are the easiest to train framework thinking, and most of the algorithm skills are essentially tree traversal problems.**

When practicing binary tree questions, you'll likely encounter questions you'll have no thinking/clue on how to solve for it. According to many readers' questions, the problem isn't that we are without ideas to solve problems, rather we lack an understanding of what we meant by "framework". **Don't look down on following lines of broken code, almost all sets of binary trees questions are solvable with this framework.**

```java
void traverse(TreeNode root) {
    // pre-order traverse
    traverse(root.left)
    // in-order (middle) traverse
    traverse(root.right)
    // post-order traverse
}
```

For example, I attach the solutions of a few problems selected at random. Don't worry about the specific code logic, rather focus and see how the framework works in it.

Leetcode No.124, hard level. This exercise requires to find the maximum sum of paths in the binary tree. The main code is as follows:

```cpp
int ans = INT_MIN;
int oneSideMax(TreeNode* root) {
    if (root == nullptr) return 0;
    int left = max(0, oneSideMax(root->left));
    int right = max(0, oneSideMax(root->right));
    ans = max(ans, left + right + root->val);
    return max(left, right) + root->val;
}
```

You see, this is a post order traversal.

Leetcode No.105, medium level. This exercise requires to rebuild a binary tree according to the results of traversal in the pre order and middle order. It's a classic problem. The main code is as follows:

```java
TreeNode buildTree(int[] preorder, int preStart, int preEnd, 
    int[] inorder, int inStart, int inEnd, Map<Integer, Integer> inMap) {

    if(preStart > preEnd || inStart > inEnd) return null;

    TreeNode root = new TreeNode(preorder[preStart]);
    int inRoot = inMap.get(root.val);
    int numsLeft = inRoot - inStart;

    root.left = buildTree(preorder, preStart + 1, preStart + numsLeft, 
                          inorder, inStart, inRoot - 1, inMap);
    root.right = buildTree(preorder, preStart + numsLeft + 1, preEnd, 
                          inorder, inRoot + 1, inEnd, inMap);
    return root;
}
```

Don't be scared by so many parameters of this function, just to control the array index. In essence, this algorithm is also a preorder traversal.

Leetcode No.99 , hard level. This exercise requires to recover a BST, the main code is as follows：

```cpp
void traverse(TreeNode* node) {
    if (!node) return;
    traverse(node->left);
    if (node->val < prev->val) {
        s = (s == NULL) ? prev : s;
        t = node;
    }
    prev = node;
    traverse(node->right);
}
```

This is just a middle order traversal. There should be no need to explain what it means for a BST middle order traversal.

As you can see, the problem of hard level is not much difficulty, but also so regular. Just write out the framework and add something to the corresponding position. That's the idea.

For a person who understands binary trees, it won't take long to do exercises of a binary tree. So if you can't or are afraid of working out questions, you can start from the binary tree. The first 10 may be a little uncomfortable. If you do another 20 with the framework, you may have some understanding. If you finish that, and then do any backtracking, dynamic programming or divide-and-conquer topic, you will find that **as long as recursion is involved, it's all a tree problem.**

More examples:

[Dynamic programming](../动态规划系列/动态规划详解进阶.md) said that the problem of collecting changes, the brute-force solution is to traverse an n-tree:

![](../pictures/动态规划详解进阶/5.jpg)

```python
def coinChange(coins: List[int], amount: int):

    def dp(n):
        if n == 0: return 0
        if n < 0: return -1

        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            # no solution for sub questions 
            if subproblem == -1: continue
            res = min(res, 1 + subproblem)
        return res if res != float('INF') else -1
    
    return dp(amount)
```

What if I can't understand so much code above? Just directly reference the framework, and you shall see the core idea：

```python
# a traverse problem of n-tree
def dp(n):
    for coin in coins:
        dp(n - coin)
```

In fact, many dynamic planning problems are traversing a tree. If you are familiar with the traversal operation of the tree, you at least know how to transform ideas into code and how to extract the core ideas of other people's solutions.

Look at the backtracking algorithm again. The detailed explanation of the backtracking algorithm in the previous article simply says that the backtracking algorithm is a forward and backward traversal problem of n-tree, without exception.

For example, the main code of N Queen Problem  is as follows:

```java
void backtrack(int[] nums, LinkedList<Integer> track) {
    if (track.size() == nums.length) {
        res.add(new LinkedList(track));
        return;
    }
    
    for (int i = 0; i < nums.length; i++) {
        if (track.contains(nums[i]))
            continue;
        track.add(nums[i]);
        // go to next decision level
        backtrack(nums, track);
        track.removeLast();
    }

/* extract n-tree traverse framework */
void backtrack(int[] nums, LinkedList<Integer> track) {
    for (int i = 0; i < nums.length; i++) {
        backtrack(nums, track);
}
```

**To sum up, for those who are afraid of algorithms, you can do the exercises of the relevant topics of the tree first, try to see the problems from the framework, rather than the details.**

From the perspective of framework, we can extract and expand based on the framework, which can not only understand the core logic quickly when we look at other people's solutions, but also help us find the direction of thinking when we write our solutions.

Of course, if the details are wrong, you can't get the right answer, but as long as there is a framework, you can't be wrong too much, because your direction is right.

However, if you didn't have a framework in mind, there's no way for you to solve the problem. Even if the answer was handed to you, you wouldn't be able to notice this is a tree traversal problem.

This kind of thinking is very important. When I wrote solutions according to the process of finding the state transition equation, (summarized in [Analysis of Dynamic Programming](dynamic_programming/AnalysisOfDynamicProgramming.md)), there have been times where, to be honest, I don't know why it's right. But lo and behold, it's right...

**This is the power of framework, which can ensure that you can still write the right program even when you are sleepy; even if you don't know a single thing, you can be a higher level than others.**

### 4. Summary

The basic storage mode of data structure is sequential (arrays) linked (linked lists). The basic operations are to add, delete, search and modify. The traversal mode is nothing but iteration and recursion.

It is suggested to start practicing from "tree" questions and finish these dozens of questions in combination with framework-based thinking. At this point, your understanding of tree structure should be in place. Then, if you look at the topics of backtracking, dynamic rules, divide and conquer, you may have a deeper understanding of the ideas.