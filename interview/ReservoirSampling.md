# Reservoir Sampling algorithm

**Author: [labuladong](https://github.com/labuladong)**

**Translator: [wsyzxxxx](https://github.com/wsyzxxxx)**

Recently I met with two interesting questions on LeetCode, LC382 and LC398. They are about Reservoir Sampling algorithm which basically is one kind of random possibility algorithm. If you understnd it, then such kind of questions will not be difficult. Otherwise, it may confuse you a lot.

The first time I met with such kind of algorithm questions is from an interview question of Google.

Given a linked **which length is unknown**, and you need design an algorithm to return one node from the linked list with **traversaling the linked list only once**.

Here the meaning of random is uniform random, which means that the possibility of selecting each element is `1/n` if there are `n` elements in total. There should be no statistical deviation.

The simple idea is to firstly traversal the whole linked list and then get the total length `n`. After that, generate an index from the random number in range `[1, n]`. Finding the corresponding node of the index means we have found the randomly selected node.

However, the requirement is, **traversaling the linked list only once**, but such kind of ideas would not fulfill it. The question could be more general. For example, given an unknown-length sequence, how can we select `k` elements randomly from it?

If you want to solve such kind of questions, then you need to learn the Reservoir Sampling algorithm.



### Algorithm Implementation

**First, we should try to solve the problem of selecting only one element.** The difficult point is random selection is actually **dynamic**. For example, if you have 5 elements now, and you have selected element `a` as the result, but now a new element `b` is added to the pool, what should you do? You may keep selecting `a` or changing to the new element `b` as the result. However, what strategy should be applied here to select `a` or `b`, and how should we prove the selection strategy is totally fair?



**I'll give the conclusion first. If you met the `i-th` element, the possibility to select that element should be `1/i` and the possibility to keep the original choice is `1 - 1/i`**.

The below code would make it easier to understand the idea:

```java
/* return the value of a random node from the linked list */
int getRandom(ListNode head) {
    Random r = new Random();
    int i = 0, res = 0;
    ListNode p = head;
    // while iterate through the linked list
    while (p != null) {
        // generate an integer in range [0, i) 
        // the possibility of the integer equals to 0 is 1/i
        if (r.nextInt(++i) == 0) {
            res = p.val;
        }
        p = p.next;
    }
    return res;
}
```

As for random algorithms, the codes are usually short, but the key problem is how to prove the algorithm is correct. Why is it uniform random when we updating the result with the possibility of `1/i`?

**Proof:** Assume there are `n` elements in total. Our purpose is to make the possibility of selecting each element is `1/n`. Then for the `i-th` element, the possibility for it to be selected is:
$$
\begin{aligned}
    &\frac{1}{i} \times (1 - \frac{1}{i+1}) \times (1 - \frac{1}{i+2}) \times ... \times (1 - \frac{1}{n}) \\
    = &\frac{1}{i} \times \frac{i}{i+1} \times \frac{i+1}{i+2} \times ... \times \frac{n-1}{n} \\
    = &\frac{1}{n}
\end{aligned}
$$

At the `i-th` position, the possibility of `i-th` element to be selected is `1/i`. At the `i+1-th` position, the possibility of `i-th` element not to be replaced is `1 - 1/(i+1)`. And similarly, the products of all the possibilities until the `n-th` position should be the final possibility of the `i-th` element is chosen. The result is `1/n`.

Hence the logic of the algorithm is correct.

**Similarly, if we need to select `k` elements randomly. The only thing we need to do is to keep the possibility of selecting `i-th` element at the `i-th` position `k/i`, and make the possibility of keeping the original selection `1 - k/i`**. Below is the code:

```java
/* return the values of k random nodes from the linked list */
int[] getRandom(ListNode head, int k) {
    Random r = new Random();
    int[] res = new int[k];
    ListNode p = head;

    // select first k elements by default
    for (int j = 0; j < k && p != null; j++) {
        res[j] = p.val;
        p = p.next;
    }

    int i = k;
    // while iterate the linked list
    while (p != null) {
        // generate an integer in range [0, i) 
        int j = r.nextInt(++i);
        // the possibility of the integer less than k is k/i
        if (j < k) {
            res[j] = p.val;
        }
        p = p.next;
    }
    return res;
}
```

The maths proof is nearly the same as the above one:
$$
\begin{aligned}
    &\frac{k}{i} \times (1 - \frac{k}{i+1} \times \frac{1}{k}) \times (1 - \frac{k}{i+2} \times \frac{1}{k}) \times ... \times (1 - \frac{k}{n} \times \frac{1}{k}) \\
    = &\frac{k}{i} \times (1 - \frac{1}{i+1}) \times (1 - \frac{1}{i+2}) \times ... \times (1 - \frac{1}{n}) \\
    = &\frac{k}{i} \times \frac{i}{i+1} \times \frac{i+1}{i+2} \times ... \times \frac{n-1}{n} \\
    = &\frac{k}{n}
\end{aligned}
$$

Although, every time the possibility of updating the selection increased by k times, for the distinct i-th element, the possibility should be multiplied by `1/k`, which comes back to the last reduction.



### Further Readings

The time complexity of above sampling algorithm is `O(n)`, but it's not the most optimized method. The better algorithm is based on geometric distribution. The time complexity is `O(k + klog(n/k))`. Since it requires a lot of maths knowledge, I won't list them here. You can search by yourself if interested.

There is another idea based on "*Fisher–Yates* shuffle". Selecting `k` elements randomly is equivlent to shuffling all the elements and selecting the first `k` elements. However, shuffling algorithm requires the random access to all the elements, so it can only be applied to the data structures supporting random access such as arrays.

Another idea is also instructive: make each element related to a random number, and then insert each element into a binary heap(priority queue) with the capacity of `k`. Sort the heap by the related random number, then the rest `k` elements are also randomized.

This method seems not very efficient, because inserting into the heap requires the time complexity of `O(logk)`. Then the whole process requires the time complexity of `O(nlogk)`. This is even not good as the most simple algorithm. However, this idea can help us to solve **the sampling probelms with weights**. Higher weight means the higher possibility of being selected. This kind of problem is very common in the real life. For example, if you don't charge money to the games, then you may never get the prizes from the lottery draw.



At last, I want to add that there are not too many random algorithms, but they are really full of special skills. You may consider two very common questions which appear pretty simple.

1.How could you carry out weighted random sampling for samples with weight? For example, given an array `w` and every elements `w[i]` representing the weight. Can you write an algorithm to select the index with the corresponding weight. When `w = [1,99]`, you should make the possibility to select index `0` becoome `1%` and the possibility to select index `1` become `99%`.

2.Implement a generator class, and a very long array would be parsed into the constructor. Can you implement the `randomGet` method, which makes sure that every time when called, it returns one element of the array randomly and it can't return the same element in multiple callings. Besides, the array could not be modified in any form, and the time complexity should be `O(1)`.

These two questions are relatively difficult. I would write some articles about them in my future spare time.



Stick to original high-quality articles, and strive to make clear the algorithm problems. Welcome to follow my Wechat official account "labuladong" for the latest articles.

![labuladong](../pictures/labuladong.jpg)
