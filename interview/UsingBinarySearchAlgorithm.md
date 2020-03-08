# How to use a binary search algorithm

**Translator: [Dong Wang](https://github.com/Coder2Programmer)**

**Author: [labuladong](https://github.com/labuladong)**

In what scenarios can binary search be used？

The most common example is in textbook, that is, searching for the index of a given target value in **an ordered array**. Moreover, if the target values is duplicated, the modified binary search can return the left boundary or right boundary index of the target value.

PS: The three binary search algorithms mentioned above are explained in detail in the previous [Binary Search Detailed Explanation](../think_like_computer/BinarySearch.md). It is strongly recommended if you haven't read it.

Putting aside the boring ordered array, how can binary search be applied to practical algorithm problems? When the search space is in order, you can perform *pruning* through binary search, greatly improving efficiency.

Talk is cheap, show you the specific *Koko eating banana* problem.

### 1. Problem analysis

Koko loves to eat bananas. There are `N` piles of bananas, the `i`-th pile has `piles[i]` bananas.  The guards have gone and will come back in `H` hours.

Koko can decide her bananas-per-hour eating speed of `K`. Each hour, she chooses some pile of bananas, and eats `K` bananas from that pile. If the pile has less than `K` bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer `K` such that she can eat all the bananas within `H` hours.

<p><strong>Example 1:</strong></p>
<pre>
<strong>Input:</strong> piles = [3,6,7,11], H = 8
<strong>Output:</strong> 4
</pre>

<p><strong>Example 2:</strong></p>
<pre>
<strong>Input:</strong> piles = [30,11,23,4,20], H = 5
<strong>Output:</strong> 30
</pre>

In other words, Koko eats up to a bunch of bananas every hour. 
1. If she can't, she can eat them until the next hour. 
2. If she has an appetite after eating this bunch, she will only eat the next bunch until the next hour.

Under this condition, let us determine **the minimum speed** Koko eats bananas.

Given this scenario directly, can you think of where you can use the binary search algorithm? If you haven't seen a similar problem, it's hard to associate this problem with binary search.

So let's put aside the binary search algorithm and think about how to solve the problem violently?

First of all, the algorithm requires *minimum speed of eating bananas in `H` hours*. We might as well call it `speed`. What is the maximum possible `speed`? What is the minimum possible `speed`?

Obviously the minimum is 1 and the maximum is `max(piles)`, because you can only eat a bunch of bananas in an hour. Then the brute force solution is very simple. As long as it starts from 1 and exhausts to `max(piles)`, once it is found that a certain value can eat all bananas in `H` hours, this value is the minimum speed.

```java
int minEatingSpeed(int[] piles, int H) {
	// the maximum value of piles
    int max = getMax(piles);
    for (int speed = 1; speed < max; speed++) {
    	// wherher can finish eating banana in H hours at speed
        if (canFinish(piles, speed, H))
            return speed;
    }
    return max;
}
```

Note that this for loop is a linear search in **continuous space, which is the flag that binary search can work**. Because we require the minimum speed, we can use a **binary search algorithm to find out the left boundary** to replace the linear search to improve efficiency.

```java
int minEatingSpeed(int[] piles, int H) {
    // apply the algorithms framework for searching the left boundary
    int left = 1, right = getMax(piles) + 1;
    while (left < right) {
        // prevent overflow
        int mid = left + (right - left) / 2;
        if (canFinish(piles, mid, H)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}
```

PS: If you have questions about the details of this binary search algorithm, it is recommended to look at the algorithm template on the left boundary of the search for [Binary Search Detailed Explanation](../think_like_computer/BinarySearch.md) in the previous article.

The remaining helper functions are also very simple and can be disassembled step by step.


```java
// Time complexity O(N)
boolean canFinish(int[] piles, int speed, int H) {
    int time = 0;
    for (int n : piles) {
        time += timeOf(n, speed);
    }
    return time <= H;
}

int timeOf(int n, int speed) {
    return (n / speed) + ((n % speed > 0) ? 1 : 0);
}

int getMax(int[] piles) {
    int max = 0;
    for (int n : piles)
        max = Math.max(n, max);
    return max;
}
```

So far, with the help of the binary search, the time complexity of the algorithm is O(NlogN).

### 2. Extension

Similarly, look at a transportation problem again.

The `i`-th package on the conveyor belt has a weight of `weights[i]`.  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `D` days.

<p><strong>Example 1:</strong></p>
<pre>
<strong>Input:</strong> weights = [1,2,3,4,5,6,7,8,9,10], D = 5
<strong>Output:</strong> 15
<strong>Explanation:</strong> 
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 
</pre>

To transport all the goods within `D` days, the goods are inseparable. How to determine the minimum load for transportation(hereinafter referred to as `cap`)?

In fact, it is essentially the same problem as Koko eating bananas. First, determine the minimum and maximum values of `cap` as `max(weights)` and `sum(weights)`.

We require **minimum load**, so a binary search algorithm that searches the left boundary can be used to optimize the linear search.

```java
// find the left boundary using binary search
int shipWithinDays(int[] weights, int D) {
	// minimum possible load
    int left = getMax(weights);
	// maximum possible load + 1
    int right = getSum(weights) + 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (canFinish(weights, D, mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return left;
}

// If the load is cap, can I ship the goods within D days？
boolean canFinish(int[] w, int D, int cap) {
    int i = 0;
    for (int day = 0; day < D; day++) {
        int maxCap = cap;
        while ((maxCap -= w[i]) >= 0) {
            i++;
            if (i == w.length)
                return true;
        }
    }
    return false;
}
```

Through these two examples, do you understand the application of binary search in practical problems？

```java
for (int i = 0; i < n; i++)
    if (isOK(i))
        return ans;
```
