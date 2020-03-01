# The key to resolving Two Sum problems

**Translator**: [Fulin Li](https://fulinli.github.io/)

**Author**:[labuladong](https://github.com/labuladong)

There are a series of problems with Two Sum in LeetCode, and this article will pick out some representative problems to demonstrate how to resolve the Two Sum problems.

### TwoSum I

**The most basic form** of Two Sum problems is like this: Given an array of integers `nums`, and a specific integer `target`. Return indices of the two numbers such that they add up to `target`. You may assume that each input would have **exactly** one solution. 

For example, given `nums = [3,1,3,6], target = 6`, the program should return an array `[0,2]` because 3 + 3 = 6.

So, how to solve this problem? First, the simplest method, of course, is the exhaustive search.

```java
int[] twoSum(int[] nums, int target) {

    for (int i = 0; i < nums.length; i++) 
        for (int j = i + 1; j < nums.length; j++) 
            if (nums[j] == target - nums[i]) 
                return new int[] { i, j };

    // If no such two numbers exists
    return new int[] {-1, -1};
}
```

This method is straightforward. The time complexity is O(n^2)​ and space complexity is O(1)​.

We can use a hash table to reduce the time complexity:

```java
int[] twoSum(int[] nums, int target) {
    int n = nums.length;
    index<Integer, Integer> index = new HashMap<>();
    // Constructing a hash table: Elements are mapped to their corresponding indices
    for (int i = 0; i < n; i++)
        index.put(nums[i], i);
    
    for (int i = 0; i < n; i++) {
        int other = target - nums[i];
        // IF 'other' exists and it is not nums[i].
        if (index.containsKey(other) && index.get(other) != i)
            return new int[] {i, index.get(other)};
    }
    
    return new int[] {-1, -1};
}
```

In this way, because the query time of a hash table is O(1), the time complexity of the algorithm is reduced to O(N). However, the space complexity is increased to O(N) for storing the hash table. Generally, it is more efficient than the exhaustive search method.

**I think the objective of the two sum problems is to tell us how to use the hash table.** Let's go on to the next.

### TwoSum II

We can modify the last script slightly to design a class with two functions:

```java
class TwoSum {
    // Add a 'number' to data structure
    public void add(int number);
    // Find out whether there exist two numbers and their sum is equal to 'value'.
    public boolean find(int value);
}
```

So how to implement these two functions? We can follow the last problem and use a hash table to realize the 'find' function.

```java
class TwoSum {
    Map<Integer, Integer> freq = new HashMap<>();

    public void add(int number) {
        // Recording the number of times that number has occurred
        freq.put(number, freq.getOrDefault(number, 0) + 1);
    }
    
    public boolean find(int value) {
        for (Integer key : freq.keySet()) {
            int other = value - key;
            // Situation 1
            if (other == key && freq.get(key) > 1)
                return true;
            // Situation 2
            if (other != key && freq.containsKey(other))
                return true;
        }
        return false;
    }
}
```

When diving into `find` function, there are two situations, for example:

Situation 1: After `[3,3,2,5]` is inputted in `add` function, `find(6)` is executed. There are two `3` exists and 3 + 3 = 6, thus, it will return true.

Situation 2: After `[3,3,2,5]` is inputted in `add` function, `find(7)` is executed. Only when `key` is equal to 2 and `other` is equal to 5, it will return true.

Except for the two situations mentioned above, `find` function will only return false.

What's the time complexity of this algorithm? The time complexity of `add` function and `find` function is O(1) and O(N) respectively. The space complexity is O(N), which is similar to the last problem.

**However, we should take realities of the situation into account in API design.** For example, in our class, the function `find` is used very frequently, and each time it requires O(N) times. It is a massive waste of time. Can we optimize the algorithm given in this situation?

Of course, we can optimize the algorithm when `find` function is used frequently. We can refer to the brute force method in the last problem and utilize a hash set to optimize `find` function pertinently.

```java
class TwoSum {
    Set<Integer> sum = new HashSet<>();
    List<Integer> nums = new ArrayList<>();

    public void add(int number) {
        // Recording all possible sum of two numbers
        for (int n : nums)
            sum.add(n + number);
        nums.add(number);
    }
    
    public boolean find(int value) {
        return sum.contains(value);
    }
}
```

In this way, all possible sum of two numbers is stored in `sum`. Every time `find` function takes O(1) time to search whether the target exists in the collection. Obviously, it is very suitable for frequent use of find function. 

### Summary

For TwoSum problems, one of the difficulties is that the given array is **unordered**. For an unordered array, it seems that we don't have any efficient methods, and an exhaustive search method may be the only way.

**In ordinary circumstances, we will sort the unordered array first and then consider applying the dual-pointer method.**  TwoSum problems make us aware that HashMap or HashSet could help us to resolve unordered array problems.

Remarkably, the essence of such method is to trade time for space, using different data structures to improve the algorithm performance pertinently.

Finally, if the given array in TwoSum I is ordered, how do we design the algorithm? It's very easy and you can refer to the previous article「Summary of usage of dual-pointer」:

```java
int[] twoSum(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left < right) {
        int sum = nums[left] + nums[right];
        if (sum == target) {
            return new int[]{left, right};
        } else if (sum < target) {
            left++; // Make sum bigger
        } else if (sum > target) {
            right--; // Make sum smaller
        }
    }
    // If no such two numbers exists
    return new int[]{-1, -1};
}
```

**Mission**: Stick to original high-quality articles, and work hard to make algorithmic problems clear. Welcome to subscribe my Wechat public account `ID:labuladong` for latest articles.