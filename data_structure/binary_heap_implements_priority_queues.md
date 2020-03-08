# Binary heap detail implements priority queues

**Translator: [build2645](https://github.com/build2645)**

**Author: [labuladong](https://github.com/labuladong)**

There is nothing mysterious about binary heap, and its properties are simpler than binary search tree BST.The main operations are 'sink' and 'swim' to maintain the binary heap properties.There are two main applications, the first is a sorting method "heap sort", the second is a very useful data structure "priority queue".

This article takes implementing a Priority Queue as an example，using pictures and human language to describe how binary heap works.

### 1、Binary heap overview

First of all, what does a binary heap have to do with a binary tree? Why do people always draw binary trees as binary heap?

Because a binary heap is a special kind of binary tree (complete binary tree) that is stored in an array.In a general linked list binary tree, we manipulate Pointers to nodes, whereas in an array, we use an array index as a pointer:

```java
// the index of the parent node
int parent(int root) {
    return root / 2;
}
// index of left child
int left(int root) {
    return root * 2;
}
// index of right child
int right(int root) {
    return root * 2 + 1;
}
```

Draw a picture and you'll understand immediately. Notice that the first index of the array 0 is left blank

![1](../pictures/heap/1.png)

PS：Because array indexes are Numbers, characters are treated as array indexes for convenience.

As you can see, with arr[1] as the root of the whole tree, the parent node of each node and the indexes of the left and right children can be obtained by simple calculation, which is a clever part of binary heap design.And for the sake of simplicity, I'm going to draw all of these binary tree structures, so I'm sure you can match a tree to an array.`

Binary heap is also divided into maximum heap and minimum heap.**The properties of the maximum heap are: each node is greater than or equal to its two children.** Similarly, the properties of the minimum heap are：each node is less than or equal to its children.

Both heap cores have the same idea, and this article takes maximum heap as an example.

For a maximum heap, by its nature, it is obvious that the top of the heap, arr[1], must be the largest element of all.

### 2、Priority queue overview

A useful feature of priority queues is that when you insert or delete elements, the elements are sorted automatically, and the underlying principle is binary heap operations.

The function of data structure is nothing more than adding and deleting，Priority queues have two main API, to insert an element and to remove the largest element（If the bottom uses the minimum heap，it will be `delMin`）.

Let's implement a simplified priority queue, starting with the code framework：

PS：For clarity, Java generics are used here，`Key` can be any data type of comparable value，You can think of it as int, char, etc

```java
public class MaxPQ
    <Key extends Comparable<Key>> {
    // An array of storage elements
    private Key[] pq;
    // Number of elements in the current Priority Queue
    private int N = 0;

    public MaxPQ(int cap) {
        // Index 0 is not used, so allocate one more space
        pq = (Key[]) new Comparable[cap + 1];
    }

    /* Returns the largest element in the current queue */
    public Key max() {
        return pq[1];
    }

    /* Insert element e */
    public void insert(Key e) {...}

    /* Removes and returns the largest element in the current queue */
    public Key delMax() {...}

    /* swim the KTH element to maintain the maximum heap properties */
    private void swim(int k) {...}

    /* Sink the KTH element to maintain maximum heap properties */
    private void sink(int k) {...}

    /* Swap the two elements of the array */
    private void exch(int i, int j) {
        Key temp = pq[i];
        pq[i] = pq[j];
        pq[j] = temp;
    }

    /* Is pq[i] less than pq[j]？ */
    private boolean less(int i, int j) {
        return pq[i].compareTo(pq[j]) < 0;
    }

    /* and left, right, parent methods */
}
```

The four methods that are left open are the mystery of binary heap and priority queue, which are illustrated below.

### 3、Implement swim and sink

Why swim up and sink? To maintain the heap structure!

We're talking about a maximum heap, where each node is larger than its two children, but when you insert and delete elements, you break the nature of the heap, which requires both operations to restore the nature of the heap.

For a maximum heap, there are two cases where the nature of the heap is destroyed:

1. If some node A is smaller than its children, then A doesn't deserve to be the parent node, so it should go down, and the larger node down here comes up as the parent node, and that's  **sink** on A。

2. If some node A is bigger than its parent, then A should not be the child node, but the parent node should be replaced and the parent node should be the parent node itself, which is the **swim** of A。

Of course, the misaligned node A may have to rise (or sink) many times before it reaches the correct location and restores the nature of the heap. So there must be a  `while`  loop in the code.

The observant reader may ask, aren't these two operations reciprocal, so the operation of floating up must be accomplished by sinking down, why should I bother to write two methods?

Yes, the operations are inversely equivalent, but in the end we will only operate at the bottom and the top of the heap (we'll see why), and obviously the "misaligned" elements at the bottom of the heap need to float up, and the "misaligned" elements at the top of the heap need to sink.

This is the code to implement the `swim` API:

```java
private void swim(int k) {
    // If you float to the top of the heap, you can't float any higher
    while (k > 1 && less(parent(k), k)) {
        // If the KTH element is larger than the top
        // replace k
        exch(parent(k), k);
        k = parent(k);
    }
}
```

Draw a GIF to help you understand：

![2](../pictures/heap/swim.gif)

**Sinking code implementation：**

Sinking is slightly more complicated than floating up, because floating up A node A only requires A to compare the value with its parent node; However, to sink node A, we need to compare the value of A with its **two child nodes** If A is not the largest, we need to adjust the position and exchange the larger child node with A.

```java
private void sink(int k) {
    // Sink to the bottom and stop
    while (left(k) <= N) {
        // Let's assume that the left node is larger
        int older = left(k);
        // If the right node exists, compare the value
        if (right(k) <= N && less(older, right(k)))
            older = right(k);
        // Node k is bigger than both of the children, so you don't have to sink
        if (less(older, k)) break;
        // Otherwise, it doesn't fit the maximum heap structure, sinking k nodes
        exch(k, older);
        k = older;
    }
}
```

Draw a GIF to help you understand：

![3](../pictures/heap/sink.gif)

So far, I've covered the main operations of binary heap, which is not difficult at all, and only adds up to ten lines of code. Now that you understand the behavior of `sink` and `swim` ，you are ready to implement the priority queue

These two methods are built on `swim` and `sink` .

**The `insert` method first adds the element to be inserted to the bottom of the heap and then floats it up to the correct position**

![4](../pictures/heap/insert.gif)

```java
public void insert(Key e) {
    N++;
    // add the new element to the end
    pq[N] = e;
    // Let it swim to the right place
    swim(N);
}
```

**`delMax`  first swap top element A with bottom element B, then delete A, and finally let B sink to the correct position。**

```java
public Key delMax() {
    // the top of the largest heap is the largest element
    Key max = pq[1];
    //Change the maximum element to the end and delete it
    exch(1, N);
    pq[N] = null;
    N--;
    // Let the pq[i] sink to the correct position
    sink(1);
    return max;
}
```

![5](../pictures/heap/delete.gif)

At this point, a priority queue is implemented.The time complexity of inserting and deleting elements is $O(logK)$，$K$ s the total number of elements in the current binary heap (priority queue).Because our time complexity is mainly spent 'sink' or 'swim', whether floating up or down, is at most the height of the tree (heap), which is the log level.


### 5、sum up

A binary heap is a complete binary tree, so it is suitable for storing in an array, and the binary heap has some special properties.

Binary heap operation is very simple, mainly floating up and down, to maintain the nature of the heap (heap order), the core code is only 10 lines.

Priority queues are implemented based on binary heap, with the main operations being insert and delete. Insert is to insert to the end first and then float up to the correct position; Deletion is to reverse the position and then delete, and then sink to the correct position. The core code is only ten lines.

Perhaps this is the power of data structure, simple operation can achieve clever functions, really admire the invention of binary heap algorithm people!

Addition, here is an elegant implementation of Heap with python lambda from [vancanhuit](https://github.com/labuladong/fucking-algorithm/issues/157#issue-576237519).