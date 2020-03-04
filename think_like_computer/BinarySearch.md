# Binary Search

Translator: [sinjoywong](https://blog.csdn.net/SinjoyWong)

Author: [labuladong](https://github.com/labuladong)


Here is a joke:

One day Mr.Don went to library and borrowed N books. When he left the library, the alarm rang, so the security stopped Mr.Don to check if there are any book haven't been registered.

Mr.Don was about to check every book under the alertor, which was despised by the security, and he said: Don't you even know binary search? And the security split books in two parts, then put the first part under the alertor, it rang. So he split the first part books in to two parts again ..., finaly, after checked logN times, the security found the book which is not been registered, and he smiled sardonically. Then let Mr.Don took remainning books out of the library.

Since then, the library lost N - 1 books.

Is Binary search really a simple algorighm? Not really. Let's see what Knuth(the one who invented KMP algorithm) said:

> Although the basic idea of binary search is comparatively straightforward, the details can be surprisingly trickey...

This article is going to discuss several the most commonly used binary search scenes: to find a number, to find its left boundary, to find its right boundary.
And that we are going to discuss details, such as if inequality sign should with the equal sign, if mid should plus one, etc. 
After analysing the difference of these details and the reason why them come out, you can write binary search code flexibly and accuratly.

### Part zero: The Framework of Binary Search

```java
int binarySearch(int[] nums,int target){
    int left = 0,right = ...;
    while(...){
        int mid = (right + left) / 2;
        if(nums[mid] == target){
            ...
        }else if(nums[mid] < target){
            left = ...
        }else if(nums[mid] > target){
            right = ...
        }
    }
    return ...;
}
```

**A technique to analize binary search is: use `else if`, rather than using `else`, then we can manage all the details.**

In order to make it more simplier to understand, this article will use `else if` all along, you can optimize it after you truly understand it.

Hint: the `...` part is where we need focus to. When you implement binary search, pay attention to these parts firstly. We are going to analyze how it changes under sepecific circumastance.

Noted: when we calculate `mid`, we need to prevent it overflowing. You can see previous article, and here we assume you can handle it.

### 1. Find a number (Basic Binary Search)

This is the simpliest scene, we are going to search a number in a array. If it exists, return its index, otherwise return `-1`.

```java
int binarySearch(int[] nums,int target){
    int left = 0;
    int right = nums.length - 1; //pay attention!

    while(left <= right){
        int mid = (right + left) / 2;
        if(nums[mid] == target){
            return mid;
        }else if(nums[mid] < target){
            left = mid + 1;
        }else if(nums[mid] > target){
            right = mid - 1;
        }
    }
    return -1;
}
```

#### Q1.Why using `<=` in `while` loop rather than `<`?

>A1: Because when we initialize `right`, we set it to `nums.length - 1`, which is index of the last element, not `nums.length`.

Both of them may show up in different binary search implementions, here is diffenences: With the former, both ends are closed, like `[left,right]`, and the later is left open right close interval, like `[left,right)`, so when we use index `nums.length`, it will out of bounds.

We will use the former `[left,right]` implemention, which both ends are closed. **This is actually the interval we search every time**.

So when we should stop searching? 

Of course we can stop when we find the target number in the array:

```java
    if(nums[mid] == target){
        return mid;
    }
```

But if we havn't find it, we'll need to terminate `while` loop and return `-1`. 
So when we should terminal `while` loop? That's simple, **when the search inverval is empty, we should stop searching**, which means we have search all items and have nothing left, we just can't find target number in the array.

The terminal condition of `while(left <= right)` is `left == right + 1`, we can write it as inverval `[right + 1,right]`, or we can just put a specific number into it, like `[3,2]`. It's obvious that **the inverval is empty**, since there is no number which is larger than 3 and less-and-equal to 2. So we should terminate `while` loop and return -1;

The terminal condition of `while(wlft < right)` is `left == right`, we can write is as interval `[left,right]`, or we can also put a specific number into it, like `[2,2]`, **the interval is NOT empty**, there is still a number `2`, but the `while` loop is terminated, which means the interval `[2,2]` is missed, index 2 is not been searched, it's wrong when we return -1 directly.

It is allright if you want to use `while(left < right)` anyway. Since we know how the mistake occurred, we can fix it with a patch:

```java
    //...
    while(left < right){
        //...
    }
    return nums[left] == target ? left : -1;
```

#### Q2: Why we implement it as `left = mid + 1`,`right = mid - 1`? I read others' code and they are implenting it as `right = mid` or `left = mid`, there is not so plus or minus, what's the difference?

>A2: This is also a difficulty of Binary Search implemention. But you can handle it if you can understand previous content.

We are aware of the concept of 'Search Interval' now, and in our implementation, the search intarval is both end closed, like `[left, right]`. So when we find index `mid` isn't the `target` we want, how to determine next search interval?

It is obviously that we will use `[left,mid - 1]` or `[mid + 1, right]`: we have just searched `mid`, so it should be removed from search interval.

#### Q3: What's the defects of this algorithm?

>A3: Since then, you should have already mastered all details of Binary Search, along with the reason why it works that way. However, there are some defects still.

For example, there is a sorted array `nums = [1,2,2,2,3]`, `targe = 2`, after processed with Binary Search Algorithm, we will get result `index = 2`. But if we want to get left boundary of `target`, which is `index = 1`, or if we want to get right boundary of `target`, which is `index = 3`, we cannot handle it with this algorithm.

It's a quite normal demand. Perhaps you would say, can't I find a target, then I search it from target to left(or right)? Sure you can, but it's not so good, since we cannt guarantee the time complexity with O(logn).

Here we will discuss this two kind of Binary Search Alghrithm.

### Part 2. Binary Search to look for left border
 
See codes below, and pay attention to marked details:

```java
int left_bound(int[] nums,int target){
    if(nums.lengh == 0) return -1;
    int left = 0;
    int right = nums.length; // Attention!

    while(left < right){ // Attention
        int mid = (left + right) / 2;
        if(nums[mid] == target){
            right = mid;
        }else if(nums[mid] < target){
            left = mid + 1;
        }else if(nums[mid] > target){
            right = mid; // Attention
        }
    }
    return left;
}
```
#### Q1: Why we use `while(left < right)`, rather than `<=`?

>A1: Analyze in the same way, since `right = nums.length` rather than `nums.length - 1`, the search interval is `[left, right)`, which is left closed right open.

>The terminal condition of `while(left < right)` is `left == right`. At this time search interval `[left,right)` is empty, so it can be terminated correctly.

#### Q2: Why there is no `return -1`? what if there is no `target` in `nums`?

>A2: Before this, let's think about what's meaning of `left border` is:

![](../pictures/binarySearch/binarySearch1.png)

For this array, the algorithm will get result `1`. The result `1` can be interpreted this way: there is 1 element in `nums` which element is less than 2.

For example, a sorted array `nums = [2,3,5,7]`, `target = 1`, the alghrithm will return 0, which means there is 0 element in `nums` which element is less than 1.

For example, we have same sorted array as described above, and this time we have `target = 8`, the algorithm will get result `4`, which means there is 4 element in `nums` which element is less than `8`.

In summary, we can see the interval of return value using the alghrithm (which is the value of `left`) is closed interval `[0,nums.length]`, so we can simply add two line of codes to get `-1` result in proper time.

```java
while(left < right){
    //...
}
//target is larger than all nums
if(left == nums.length) return -1;
//just like the way previously implenented
return nums[left] == target ? left : -1;
```

#### Q1: Why `left = mid + 1, right = mid`? It's kind of different with previous implement.

>A1: It's easy to explain. Since our search interval is [left,right), which is left closed right open, so when `nums[mid]` has been detected, in then next move, the search interval should remove `mid` and slit it to two intervals, which is `[left,mid)` and `[mid + 1, right)`.

#### Q4: Why this algorithm can be used for search left border?

>A4: The key is the solution when we meet `nums[mid] == target`:
```java
    if (nums[mid] == target){
        right = mid;
    }
```

>It's obviously that we don't return it immediatly when we find `target`, in the further we continuly search in interval `[left,mid)`, which is search towarding left and contract, then we can get left border.

#### Q5: Why return `left`, rather than `right`?

>A5: It's same way, because the terminal condition of `while` is `left == right`.

### Part Three: BINARY SEARCH TO FIND RIGHT BORDER

It's almost same with part two: binary search to find left border, there is only two differences, which is marked below:

```java
int right_bound(int[] nums,int target){
    if(nums.length == 0) return -1;
    int left = 0, right = nums.length;

    while(left < right){
        int mid = (left + right) / 2;
        if(nums[mid] == target){
            left = mid + 1; // Attention!
        }else if(nums[mid] < target){
            left = mid + 1;
        }else if(nums[mid] > target){
            right = mid;
        }
    }
    return left - 1; //Attention!
}
```

#### Q1: Why this alghrithm can be used to find right border?

>A1: Similarly, key point is:

```java
    if(nums[mid] == target){
        left = mid + 1;
    }
```

>When `nums[mid] == target`, we don't return immediately. On the contrary we enlarge the lower bound of search interval, to make serach interval move to right rapidlly, and finally we can get right border.

#### Q2: Why we return `left -1`, unlike when we process with left border algorithm and return `left`? In addition I think since we are searching right border, shouldn't we return `right` instead?

>A2: First of all, the terminal condition of `while` loop is `left == right`, so it's right to use both of them. You can return `right - 1` if you want to reflect `right`.

>As for why we should minus `1` here, it's a special point, let's see the condition judgement:

```java
    if(nums[mid] == target){
        left = mid + 1;
        //Thinking this way: mid = left - 1
    }
```
![](../pictures/binarySearch/binarySearch2.png)

When we update the value of `left`, we must do it this way: `left = mid + 1`, which means when `while` is terminated, `nums[left]` must not equal to `target`, but `nums[left-1]` could be equal to `target`.

As for why `left = mid + 1`, it's same as part two.

#### Q3: Why there is no `return -1`? what if there is no `target` in `nums`?

>A3: Like left border search, because the terminal condition of `while` is `left == right`, which means value interval of `left` is `[0,nums.length]`, so we can add some codes and `return -1` apprapoly:

```java
while(left < right){
    // ...
}
if (lef == 0) return -1;
return nums[left -1] == target ? (left -1) : -1;
```

### Part Four: Summary

Let's tease out the causal logic of these detailed differences.

#### Firstly, we implement a basic binary search alghrithm:

Because we initialize `right = nums.length - 1`, it decided our search interval is `[left,right]`, and it also decided `left = mid + 1` and `right = mid - 1`.

Since we only need to find a index of `target`, so when `nums[mid] == target`, we can return immediately.

#### Secondly, we implement binary search to find left border:

Because we initialize `right = nums.length`, it decided our search interval is `[left,right)`, and it also decided `while (left < right)` ,and `left = mid + 1` and `right = mid`.

Since we need to find the left border, so when `nums[mid] == target`, we shouldn't return immediately, we need to tighten the right border to lock the left border.

#### Thirdly, we implement binary search to find right border:

Because we initialize `right = nums.length`, it decided our search interval is `[left,right)`, 

it also decided `while(left < right)`, 
`left = mid + 1` and `right  = mid`.

Since we need to find the left border, so when `nums[mid] == target`, we shouldn't return immediately, we need to tighten the left border to lock the right border.

For further consideration, we must set `left = mid + 1` when we tighten left border, so no matter we return `left` or `right`, we must `minus 1` with the result.

If you can understand all above, then congratulations,  binary search alghrithm won't borther you any more!

According to this article, you will learn:

1. When we write binary search code, we don't use `else`, we will use `else if` instead to make our mind clear.

2. Pay attention to search interval and terminal condition of `while`. If there are any element missed, check it before we return the result.

3. If we need to search left/right border, we can get proper result when `nums[mid] == target`, and when we search right border, we should minus 1 to get result.

4. If we close both sides of border, we can only change the code in `nums[mid] == target` and return logic to get right answer. **Put it on your notes, it can be a template for binary search implementation!**
