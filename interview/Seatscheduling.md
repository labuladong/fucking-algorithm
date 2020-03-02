# How to arrange candidates' seats

**Translator: [SCUhzs](https://github.com/HuangZiSheng001)**

**Author: [labuladong](https://github.com/labuladong)**



This is no.885 question in LeetCode, interesting and skillful.  Solving such problems is not as IQ-cost as dynamic programming,  but rather depends on  understanding of common data structures and  capacity to write code. As far as I'm concerned, it deserves our attention and study.

By the way, I'd like to say something. Many readers ask me, how to sum up  framework of  algorithm. But  in fact, that's not really like that. The framework is slowly extracted from the details. I hope,  after you read our articles, you'd better take some time to try solving more similar problems by yourself.  As it said, "Practice goes deeper than theoretic knowledge."

Let me first describe the subject: "suppose there is an examination room, with a row of `N` seats,  respectively, their indexes are  `[0.. n-1]`.  The Candidates, will  **successively** enter the room, will probably leave at **any time**."

As an examiner, you should arrange the seats for students,  so as to meet those requirements:  **whenever a student enters,  maximize the distance between him and the nearest other students; if there are more than one such seats, arrange him to the seat with the smallest index.** This is a real situation in life as we known.

That is, you need to implement a class like this:

```java
class ExamRoom {
    // constructor, receive the N which means total number of seats  
    public ExamRoom(int N);
    // when a candidate comes, return to the seat assigned for him
    public int seat();
    // The candidate in the position P now left
    // It can be considered that there must be a candidate in the position P
    public void leave(int p);
}
```

For example, there are five seats in the  room, which are `[0..4]`:

When the candidate 1 enters  (call `seat()`), it is OK for him to sit in any position, but you should arrange the  position with lowest index for him, that is, return position 0.

When the candidate 2 enters (call `seat()`), he should keep away from candidates nearby as possible, that is, return to position 4.

When the candidate 3 enters, he should keep away from candidates nearby as possible, so he need to sit in the middle, that is, seat 2.

If another candidate enters, he can sit in seat 1 or seat 3. Take the smaller one, index 1.

And so on.

In the situation just mentioned, the function `leave`  doesn't be called. However, readers can definitely find the following regular:

**If we regard every two adjacent candidates as the two endpoints of a line segment, the new arrangement is that, find the longest line segment,  let this candidate  「dichotomy」 the line segment in middle, and then the middle point is the seat  assigned to him.  Actually, `Leave (P) ` is  to remove the end point `p`, so as to merge two adjacent segments into one.**

It's not hard to think about it, actually, this question wants to examine your understanding of data structure. To implement the above logic, which data structure should be selected ?



### 1. Thinking analysis

According to the above idea, first of all, we need to abstract the students sitting in the classroom into line segments, which can be simply represented by an array of 2 size .

In addition, the idea requires us to find the 「longest」 line segment,  removing or adding the line segment  both are needed.

**If we face with such a requirement that need to get the most value in the dynamic process, the ordered data structure should be used. Binary heap and balanced binary search tree is  what we use most often.** The priority queue, which implemented by binary heap,  its time complexity of getting most value  is O (logN), but only the maximum value can be deleted. Balanced binary tree can not only get the most value, but also modify or delete any value, and the time complexity of them both are O (logn).

In summary, binary heap can't finish the operation of `leave` , so balanced binary tree should be chose. And  we will use a structure named `TreeSet`, which used in JAVA. It is an ordered data structure, and  its bottom layer  is implemented by red black tree.

By the way, when it comes to Set or Map, some readers may take it for granted that it is a HashSet or a HashMap. There is something wrong with that.

Because the bottom layer of Hash_Set/Map is implemented by the hash function and the array, it has the feature: its traversal order is not fixed while its operation efficiency is high, and its time complexity is O (1).

Meanwhile, the Set/Map can also rely on other underlying data structures, The Red Black Tree (a balanced binary search tree) is the common one, which has a feature that maintaining the order of elements automatically and its efficiency is O (logn). This is commonly referred to 「ordered Set/Map」.

The `TreeSet` we use just is an ordered set. Its purpose is to maintain the order of line length, quickly find the longest line, and quickly delete and insert.



### 2. Simplify the problem

Firstly, if there are multiple optional seats, you should choose the seat with the lowest index. **Let's simplify the problem first, this is, ignore this requirement for the moment** , and put the implement of above idea ahead.

Another common programming trick used in this problem is to use a 「virtual line segment」, so as to let the algorithm start properly, the same as the reason why the algorithms which related to linked list algorithms need a 「virtual header」.     

```java
// Map endpoint p to the segment with P as the left endpoint
private Map<Integer, int[]> startMap;
// Map endpoint p to the segment with P as the right endpoint
private Map<Integer, int[]> endMap;
// According to their length, store all line segments from small to large 
private TreeSet<int[]> pq;
private int N;

public ExamRoom(int N) {
    this.N = N;
    startMap = new HashMap<>();
    endMap = new HashMap<>();
    pq = new TreeSet<>((a, b) -> {
        // Calculate the length of two line segments
        int distA = distance(a);
        int distB = distance(b);
        // Longer means it is bigger, and put it back
        return distA - distB;
    });
    // Firstly, put a virtual segment in the ordered set
    addInterval(new int[] {-1, N});
}

/* Remove a line segment */
private void removeInterval(int[] intv) {
    pq.remove(intv);
    startMap.remove(intv[0]);
    endMap.remove(intv[1]);
}

/* Add a line segment */
private void addInterval(int[] intv) {
    pq.add(intv);
    startMap.put(intv[0], intv);
    endMap.put(intv[1], intv);
}

/* Calculate the length of a line segment */
private int distance(int[] intv) {
    return intv[1] - intv[0] - 1;
}
```

「Virtual line segment 」is to represent all seats as one line segment:

![](../pictures/seat_scheduling/9.png)



With the foreshadowing, the main API `seat` and `leave` could be written:



```java
public int seat() {
    // Take the longest line from the ordered set
    int[] longest = pq.last();
    int x = longest[0];
    int y = longest[1];
    int seat;
    if (x == -1) { // case 1
        seat = 0;
    } else if (y == N) { // case 2
        seat = N - 1;
    } else { // case 3
        seat = (y - x) / 2 + x;
    }
    // Divide the longest line segment into two segments
    int[] left = new int[] {x, seat};
    int[] right = new int[] {seat, y};
    removeInterval(longest);
    addInterval(left);
    addInterval(right);
    return seat;
}

public void leave(int p) {
    // Find out the lines around p
    int[] right = startMap.get(p);
    int[] left = endMap.get(p);
    // Merge two segments into one
    int[] merged = new int[] {left[0], right[1]};
    removeInterval(left);
    removeInterval(right);
    addInterval(merged);
}
```

![three contidions](../pictures/seat_scheduling/8.png)



At this point, this algorithm is basically implemented. Although a lot of code, in fact it's not difficult to think: find the longest line segment, divide it into two segments from the middle, and the midpoint is the return value of `seat()`; find the left and right line segments of `p`  , merge them into one segment. Those is the logic of `leave (P)`.



### 3. Advanced problem

However, when the topic requires multiple choices, we should choose the seat with the smallest index. We just ignored that. For example, the following situation may cause errors:![](../pictures/seat_scheduling/3.jpg)

Now there are line segments `[0,4]` and  `[4,9]` in the ordered set, the longest line segment `longest` is the latter one. According to the logic of `seat`, it will split the `[4,9]`, that is, return to seat 6. However, the correct answer should be seat 2. Because both 2 and 6 meet the condition of maximizing the distance between adjacent candidates, and the smaller one should be taken.

![](../pictures/seat_scheduling/4.jpg)

**The solution to such requirements is to modify the sorting method of ordered data structure.** In this problem, is that,  modify the logic of `treemap`'s comparison function:

```java
pq = new TreeSet<>((a, b) -> {
    int distA = distance(a);
    int distB = distance(b);
    // If the lengths are equal, compare the indexes
    if (distA == distB)
        return b[0] - a[0];
    return distA - distB;
});
```

Beside that, we also need to change the `distance` function. Instead of  calculating the length between two endpoints of a line segment, we need to let it calculate the length between the midpoint and endpoint of the line segment.

```java
private int distance(int[] intv) {
    int x = intv[0];
    int y = intv[1];
    if (x == -1) return y;
    if (y == N) return N - 1 - x;
    // Length between midpoint and endpoint
    return (y - x) / 2;
}
```

![](../pictures/seat_scheduling/5.jpg)

In this way, the values of `distance` , `[0,4]` and `[4,9]` are equal. The algorithm will compare the indexes of the two, and take smaller line segments for segmentation. So far, this algorithm problem has been solved perfectly.

### 4. Final summary

​	The problem mentioned in this article is not so difficult, although it seems that there is a lot of code. The core issue is to examine the understanding and use of ordered data structures

​	To deal with dynamic problems, we usually use ordered data structures, such as balanced binary search tree and binary heap, which have similar time complexity. But the former supports more operations.

​	Since balanced binary search tree is so easy to use, why use binary heap?  The reason given by me, is that, the bottom layer of binary heap is array, which is easier to implement. See the old article 「detailed explanation of binary heap」 to learn more detail.  Try to make a Red Black Tree? It not only has more complex operation, but also costs more space. Of course, to solve the specific problems, we should choose the appropriate data structure with specific analysis.

​	I hope this article can be helpful for you.



