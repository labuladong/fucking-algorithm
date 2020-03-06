# Interval Problem (II): Interval Merging

**Translator: [GYHHAHA](https://github.com/GYHHAHA)**

**Author: [labuladong](https://github.com/labuladong)**

In the "Interval Scheduling: Greedy Algorithm", we use greedy algorithm to solve the interval scheduling problem, which means, given a lot of intervals, finding out the maximum subset without any overlapping.

Actually, there are many other relating problems about interval itself. Now, we will talk about the "Merge Interval Problem".

【Leetcode 56】Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

**Example 1:**

```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

**Example 2:**

```
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

**NOTE:** input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

The general thought for solving interval problems is observing regular patterns after the sorting process.

### First Part: Thought

A certain interval can be defined as`[start, end]`, the interval scheduling in the last article states the sorting process need to be done by `end`. But for the merging problem, both sorting with the `end` or `start` are acceptable. For the clear purpose, we choose sorting by `start` .

【Explanations for chinese in the picture】

【按start排序：sorting by start】【索引：index】

![1](../pictures/mergeInterval/1.jpg)

Clearly, for the merging result `x`, `x.start`must have the smallest  `start`  in these intersected intervals, and `x.end` must have the largest  `end` in these intersected intervals as well.

![2](../pictures/mergeInterval/2.jpg)

Since ordered, `x.start` is easy to achieve, and computing  `x.end`  is also not difficult as well, which can take an analogy of searching the max number in a certain array.

```java
int max_ele = arr[0];
for (int i = 1; i < arr.length; i++) 
    max_ele = max(max_ele, arr[i]);
return max_ele;
```

### Second Part: Code

```python
# intervals like [[1,3],[2,6]...]
def merge(intervals):
    if not intervals: return []
    # ascending sorting by start
    intervals.sort(key=lambda intv: intv[0])
    res = []
    res.append(intervals[0])
    
    for i in range(1, len(intervals)):
        curr = intervals[i]
        # quote of the last element in res
        last = res[-1]
        if curr[0] <= last[1]:
            # find the biggest end
            last[1] = max(last[1], curr[1])
        else:
            # address next interval need to be merged
            res.append(curr)
    return res
```

It will be illustrated more clearly by the follow gif.

![3](../pictures/mergeInterval/3.gif)

So far, the Interval Merging Problem have been solved.

The End. Hope this article can help you!
