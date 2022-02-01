# Framework and thoughts about learning data structures and algorithms

Translator: [ForeverSolar](https://github.com/foreversolar)

Author: [labuladong](https://github.com/labuladong)

This is a revision of a long time ago article titled "framework thinking of learning data structure and algorithm". This article will cover all the previous contents, and will give many code examples to teach you how to use framework thinking.

First of all, we are talking about common data structures. I am not engaged in algorithm competitions, so I can only solve conventional problems. In addition, the following is a summary of my personal experience. No algorithm book can cover these things, so please try to understand my point of view and don't dwell on the details, because this article only hopes to build a broad overview of framework thinking for data structures and algorithms.

Framework thinking goes from the whole to the details, from the top to the bottom and from the abstract to the concrete. We believe that thinking in this way can be more effective not only in learning data structures and algorithms, but also in learning any other type of knowledge.

## 1.Storage mode of data structures

**There are only two ways to store data structures: as arrays (sequential storage) or as linked lists (linked storage)**。

Wait... what about other data structures such as hash table, stack, queue, heap, tree, graph and so on?

When we analyze problems, we must keep in mind the idea of recursion, from top to bottom, from abstract to concrete. Those data structures belong to the 「superstructure」, while arrays and lists are the 「structural basis」. All those diverse data structures can be viewed as special operations on linked lists or arrays; they just have different APIs.

For example, 「queue」 and 「stack」 data structures can be implemented with both linked lists and arrays. Using arrays, we need to deal with the problem of expanding and shrinking capacity; using linked lists, there is no such problem, but more memory space is needed to store node pointers.

A graph can be implemented with both linked lists and arrays. An adjacency table is a linked list, and an adjacency matrix is a two-dimensional array. An adjacency matrix can be used to evaluate connectivity quickly and can solve some problems via matrix operations, but if the graph is sparse, this becomes very time-consuming. An adjacency table is more space-saving, but the efficiency of many operations is certainly less than for an adjacency matrix.

Hashtables map keys to a large array by making use of a hash function to solve hash conflicts. Chaining needs linked list features with simple operations, but with the extra space needed to store pointers; linear exploration methods need array features, to address continuously, and does not need the extra storage space for pointers, but the operation is slightly more complex.

The implementation of trees with arrays is a "heap", because a "heap" is a complete binary tree. Heap storage with arrays does not need node pointers and the operation is relatively simple; the implementation with linked list is a very common kind of "tree", because it is not necessarily a complete binary tree, so it is not suitable to use array storage. For this reason, based on the tree structure of the list, various ingenious designs have been derived, such as binary search trees (BST), AVL trees, red-black trees, interval trees, B-trees, etc., to deal with different problems.

In conclusion, there are many kinds of data structures, even you can invent your own data structures, but the underlying storage is nothing but arrays or linked lists. **The advantages and disadvantages of the two are as follows:**

- **Arrays** offer compact and continuous storage, which can be accessed randomly. They make it possible to find elements quickly via index and use storage space efficiently. Because of the need for continuous chunks of memory, sufficient storage space must be allocated at one time. Therefore, if the array has to be expanded, we need to find and reallocate a larger space first, and then copy all the data over; time complexity _O(n)_. And if you want to insert and delete elements in the middle of the array, you must move all the data each time to maintain the continuity; time complexity _O(n)_.

- Because the elements of a **linked list** are not continuous (the pointer points to the position of the next element), linked lists don't share the expansion problem faced by arrays. If you know the parent and child of a node, the operation can delete the element or insert a new element, with time complexity of _O(1)_. But because the storage space is not continuous, you can't calculate the address of the corresponding element according to an index, so you can't access it randomly. Because each element must store a pointer to the location of parent and/or child nodes, it will consume more storage space.


## 2.Basic operations on data structures

For any data structure, its basic operation is no more than traversal + access, and more specific point are: add, delete, search and modify.

**There are many kinds of data structures, but their purpose is to add, delete, search and modify them as efficiently as possible** in different application scenarios. Isn't that the mission of data structure?

How to traverse + access? We still see from the highest level that traversal and access of various data structures are in two forms: linear and nonlinear.

Linear is represented by for / while iteration, and nonlinear is represented by recursion. Furthermore, there are only the following frameworks:

Array traversal framework, typical linear iterative structure：

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
        // iteratively p.val
    }
}

void traverse(ListNode head) {
    // recursively head.val
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

N-tree traversal can be extended to graph traversal, because graph is a combination of several n-tree. Do you think a circle can appear in a graph? This is very easy to do. Just mark it visited with a Boolean array.

**The so-called framework is a trick. No matter add, delete, insert or modify, these codes are never separated from the structure. You can take this structure as the outline and add code on the framework according to specific problems. The following will give specific examples.**

## 3.Guidelines of Algorithm Exercises 

First of all, it should be clear that **data structures are tools, and algorithms are methods to solve specific problems with appropriate tools**. That is to say, before learning algorithms, at a minimum we need to understand common data structures and their characteristics and defects.

So how to practice in leetcode? **Do binary tree exercises first! Do binary tree exercises first! Do binary tree exercises first!** Because binary tree exercises are the easiest to train framework thinking and most of the algorithm skills are essentially tree traversal problems.

If the many readers' questions we have received are any measure, we are not without ideas to solve problems, but most of these ideas lack an understanding of what we mean by "framework". **Don't look down on the following lines of code, almost all the topics of binary trees are a set of this framework:**

```java
void traverse(TreeNode root) {
    // pre-order traversal
    traverse(root.left)
    // middle-order traversal
    traverse(root.right)
    // post-order traversal
}
```

As an example, I can show the solution to a few problems at random, regardless of the specific code logic, just to see how they fit into this framework.

Leetcode No.124 , hard level. This exercise requires to find the maximum sum of paths in the binary tree. The main code is as follows:

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

You see, this is a post-order traversal.

Leetcode No.105, medium level. This exercise asks us to rebuild a binary tree according to the results of traversal in the pre-order and middle-order traversals. It's a classic problem. The main code is as follows

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

Don't be scared by the many parameters of this function, they're only purpose is to control the array index. In essence, this algorithm is also a pre-order traversal.

Leetcode No.99 , hard level. The exercise is to recover a BST, the main code is as follows：

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

This is just a middle-order traversal. There should be no need to explain what is meant by a BST middle-order traversal.

As you can see, with this framework in mind, even hard level problems don't offer much difficulty. Just write out the framework and add something to the corresponding position. That's the idea.

For a person who understands binary trees, it won't take long to do binary tree exercises. So if you can't or are afraid of working out questions, you can start from the binary trees. The first 10 may be a little uncomfortable. If you do another 20 with the framework, you may gain some understanding. If you finish that, and then do any backtracking, dynamic programming or divide-and-conquer topic, you will find that **as long as recursion is involved, it's all a tree problem.**

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

What if I can't read so much code? Extract the framework, so you can see the core idea：

```python
# a traversal problem of an n-tree
def dp(n):
    for coin in coins:
        dp(n - coin)
```

In fact, many dynamic planning problems are traversing a tree. If you are familiar with the traversal operations of the tree, you at least know how to transform ideas into code and how to extract the core ideas of other peoples' solutions.

Look at the backtracking algorithm again. The detailed explanation of the backtracking algorithm in the previous article simply says that the backtracking algorithm is a forward and backward traversal problem of n-tree, without exception.

For example, the main code of the N-Queen Problem  is as follows:

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

**To sum up, for those who are afraid of algorithms, you can do the exercises of the relevant topics of trees first. Try to see the problems in relation to the framework, rather than by focusing on details.**

From the perspective of framework we can extract and expand based on the framework. This can not only allow us to quickly understand the core logic of other people's solutions, but also help us find the correct direction of thinking when working on our own solutions.

Of course, if the details are wrong, you can't get the right answer. But as long as there is a framework, you can't be too wrong, because your direction is right.

This kind of thinking is very important. Sometimes I write the solution according to the process of finding the state transition equation summarized in the dynamic planning explanation. To be honest, I don't know why it's right. Anyway, it's right...

**This is the power of a framework. It can ensure that you can still write the right program even when you are sleepy; even if you can't do anything, you can be at a higher level than others.**


## 4.Summary

The basic storage mode of data structures is chain and order. The basic operation is to add, delete, search and modify. The traversal mode is nothing but iteration and recursion.

It is suggested to start from "tree" and finish these dozens of questions in combination with framework thinking. The understanding of tree structures should be solid. If you then look at the topics of backtracking, dynamic rules, divide and conquer, you may have a deeper understanding of the ideas involved.
