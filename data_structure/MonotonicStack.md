### How to use Monotonic Stack to solve problems[](#如何使用单调栈解题)

> 原文地址：[https://github.com/labuladong/fucking-algorithm/blob/master/数据结构系列/单调栈.md](https://github.com/labuladong/fucking-algorithm/blob/master/数据结构系列/单调栈.md)


Stack is a very simple data structure. The logical sequence of first in and last out conforms to the characteristics of some problems, such as function call stack.      

Monotone stack is actually a stack. It just uses some ingenious logic to keep the elements in the stack orderly (monotone increasing or monotone decreasing) after each new element is put into the stack.      

Sounds like a heap? No, monotone stack is not widely used. It only deals with one typical problem, which is called next greater element. In this paper, the algorithm template of monotone queue is used to solve this kind of problem, and the strategy of dealing with "cyclic array" is discussed.          

First, explain the original problem of next greater number: give you an array, return an array of equal length, the corresponding index stores the next larger element, if there is no larger element, store - 1. It's not easy to explain clearly in words. Let's take a direct example:     

Give you an array [2,1,2,4,3], you return the array [4,2,4,-1,-1].      

Explanation: the number that is larger than 2 after the first 2 is 4; the number that is larger than 1 after the first 1 is 2; the number that is larger than 2 after the second 2 is 4; there is no number that is larger than 4 after the fourth, fill - 1; there is no number that is larger than 3 after the third, fill - 1.   

It's a good idea for the violent solution of this problem to scan the back of each element to find the first larger element. But the time complexity of violent solution is O (n^2).         

This problem can be thought abstractly: think of the elements of the array as people standing side by side, and the size of the elements as the height of an adult. These people stand in line with you. How to find the next greater number of element "2"? Very simply, if you can see the element "2", then the first person you can see behind him is the next greater number of "2". Because the element smaller than "2" is not tall enough, it is blocked by "2". The first one is the answer. 


![ink-image](../pictures/%E5%8D%95%E8%B0%83%E6%A0%88/1.png)

Is this a very understandable situation? With this abstract scenario in mind, let's look at the code first. 

```cpp
vector<int> nextGreaterElement(vector<int>& nums) {
    vector<int> ans(nums.size()); // array to store answer
    stack<int> s;
    for (int i = nums.size() - 1; i >= 0; i--) { // put it into the stack back to front
        while (!s.empty() && s.top() <= nums[i]) { // determine by height
            s.pop(); // short one go away while blocked
        }
        ans[i] = s.empty() ? -1 : s.top(); // the first tall behind this element
        s.push(nums[i]); // get into the queue and wait for later height determination
    }
    return ans;
}
```

This is the template for monotone queue problem solving. The for loop scans elements from the back to the front, because we use the stack structure to enter the stack upside down, but we are actually going to exit the stack. The while loop is to exclude the elements between the two "high" elements. Because their existence has no meaning, there is a "higher" element in front of them, so they cannot be used as the next great number of the subsequent elements.        

The time complexity of this algorithm is not so intuitive. If you see for loop nesting while loop, you may think that the complexity of this algorithm is O (n ^ 2), but in fact, the complexity of this algorithm is only O (n).   

To analyze its time complexity, we need to look at it as a whole: there are n elements in total, each element is pushed into the stack once, and at most it will be pop once, without any redundant operation. So the total calculation scale is proportional to the element scale n, which is the complexity of O (n).     

Now that you have mastered the technique of using monotone stack, take a simple transformation to deepen your understanding.            I'll give you an array t = [73, 74, 75, 71, 69, 72, 76, 73], which stores the weather temperature in recent days? No, it's in Fahrenheit. You return an array to calculate: for each day, how many days do you have to wait for a warmer temperature; if you can't wait for that day, fill in 0.            

For example: give you t = [73, 74, 75, 71, 69, 72, 76, 73], and you return [1, 1, 4, 2, 1, 1, 0, 0].          

Explanation: the first day is 73 degrees Fahrenheit, and the next day is 74 degrees Fahrenheit, which is larger than 73 degrees Fahrenheit, so for the first day, you can wait for a warmer temperature just one day. The same goes for the latter.            

You are already sensitive to the next greater number type problem. In essence, this problem is also to find the next greater number. But now, instead of asking you what the next greater number is, you just need to ask you the current distance from the next greater number.            
For the same type of problem, the same idea, directly call the algorithm template of monotone stack, with a little change, directly go to the code. 

```cpp
vector<int> dailyTemperatures(vector<int>& T) {
    vector<int> ans(T.size());
    stack<int> s; // here for element index，not element
    for (int i = T.size() - 1; i >= 0; i--) {
        while (!s.empty() && T[s.top()] <= T[i]) {
            s.pop();
        }
        ans[i] = s.empty() ? 0 : (s.top() - i); // get index spacing
        s.push(i); // add index，not element
    }
    return ans;
}
```

The monotone stack is explained. Let's start with another important point: how to deal with "circular array".      

It's also next greater number. Now suppose the array given to you is a ring. How to deal with it?   

Give you an array [2,1,2,4,3], you return the array [4,2,4,-1,4]. With the ring attribute, the last element 3 goes around and finds the element 4 larger than itself. 

![ink-image](../pictures/%E5%8D%95%E8%B0%83%E6%A0%88/2.png)

First of all, the memory of the computer is linear, and there is no real ring array. However, we can simulate the effect of ring array. Generally, we use the% operator to calculate the modulus (remainder) to get the ring effect: 

```java
int[] arr = {1,2,3,4,5};
int n = arr.length, index = 0;
while (true) {
    print(arr[index % n]);
    index++;
}
```

Back to the problem of next greater number, after adding the ring attribute, the difficulty lies in that the meaning of next is not only the right side of the current element, but also the left side of the current element (as shown in the above example).   

If we are clear about the problem, it will be half solved. We can think about this idea: to "double" the original array is to connect another original array at the back. In this way, according to the previous "height comparison" process, each element can not only compare the elements on its right, but also the elements on the left. 

![ink-image (2)](../pictures/%E5%8D%95%E8%B0%83%E6%A0%88/3.png)

How to achieve it? Of course, you can construct this double length array and apply the algorithm template. However, instead of constructing a new array, we can use the technique of loop array to simulate. Just look at the code: 

```cpp
vector<int> nextGreaterElements(vector<int>& nums) {
    int n = nums.size();
    vector<int> res(n); // store result
    stack<int> s;
    // pretend that this array is twice the length
    for (int i = 2 * n - 1; i >= 0; i--) {
        while (!s.empty() && s.top() <= nums[i % n])
            s.pop();
        res[i % n] = s.empty() ? -1 : s.top();
        s.push(nums[i % n]);
    }
    return res;
}
```

Till now,you have caught up with the design method and code template for Monotonic Stack，learned to solve the problem of Next Greater Number ,can deal with cyclic array.
