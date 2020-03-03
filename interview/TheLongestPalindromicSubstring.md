Author: [labuladong](https://github.com/labuladong)

Translator: [joketion](https://github.com/jokertion)
 
# Longest Palindrom Substring

The palindrom substring is a problem often encountered in interviews (although the question itself has no meaning), this article tells you the core idea of ​​the palindrom substring problem.

First of all, make it clear: ** palindrom string is string that read the same when reading forward and backward **.

For example, the strings `aba` and` abba` are both palindrom strings, because they are symmetrical, and in turn are the same as themselves. Conversely, the string `abac` is not a palindrom string.

It can be seen that the length of the palindrom string may be odd or even, which adds to the difficulty of the palindrom problem. The core of solving this type of problem is the ** double pointer **. Let's figure out the palindrom problem through a question of the longest palindrom substring:

```cpp
string longestPalindrome(string s) {}
```

### 一、Thinking

The first thing we should think about this is, given a string `s`, how do we find a palindrome in` s`?

There is an interesting idea: Since the palindrome is a string that reads the same in both directions, if we reverse the `s`, we call it` s'`, then in `s` and `s'`.Then find the ** longest common substring **, so you should be able to find the longest palindrome substring.

For example, the string `abacd`, which in turn is `dcaba`, and its longest common substring is `aba`, which is the longest palindrome substring.

However, this idea is wrong, for example, the string `aacxycaa`, which in turn is `aacyxcaa`, the longest common substring is `aac`, but the longest palindrome substring should be `aa`.

Although this idea is not correct, ** this kind of thinking that transforms the problem into other forms of thinking is very worth advocating **.

Next, let's talk about the correct idea using double pointers.

** The core idea of ​​the problem of finding palindrome string is: from the middle to the two sides to judge the palindrome string **. For the longest palindrome substring, this means:

```python
for 0 <= i < len(s):
	Find a palindrome centered on s [i]
    Updated answer
```

However, we also said just now that the length of the palindrome string may be odd or even. If it is the case of `abba`, there is no center character, and the above algorithm is okay. So we can modify it:


```python
for 0 <= i < len(s):
	Find a palindrome centered on s [i]
    Find palindrome strings centered on s [i] and s [i + 1]
    Updated answer
```

PS: The reader may find that the index here will be out of bounds and will be processed later.

### Second, code implementation

According to the above idea, we must first implement a function to find the longest palindrome string. This function is a bit tricky:

```cpp
string palindrome (string & s, int l, int r) {
     // avoid outOfIndex error
    while (l> = 0 && r <s.size ()
            && s [l] == s [r]) {
        // expand to both sides
        l--; r ++;
    }
    // return the longest palindrome string centered on s [l] and s [r]
    return s.substr (l + 1, r - l - 1);
}
```

Why pass in two pointers `l` and` r`? ** Because this implementation can handle the case where the length of the palindrome is odd and even **:


```python
for 0 <= i <len (s):
    # Find a palindrome centered on s [i]
    palindrome (s, i, i)
    # Find palindromes centered on s [i] and s [i + 1]
    palindrome (s, i, i + 1)
    Updated answer
```

Take a look at the full code of `longestPalindrome`:


```cpp
string longestPalindrome (string s) {
    string res;
    for (int i = 0; i <s.size (); i ++) {
        // longest palindrome subgroup centered on s [i]
        string s1 = palindrome (s, i, i);
        // Longest palindrome substring centered on s [i] and s [i + 1]
        string s2 = palindrome (s, i, i + 1);
        // res = longest (res, s1, s2)
        res = res.size ()> s1.size ()? res: s1;
        res = res.size ()> s2.size ()? res: s2;
    }
    return res;
}
```

At this point, the problem of this longest palindrome substring has been solved.
with Time complexity is O(N^2) and Space complexity is O(1).

It is worth mentioning that this problem can be solved by dynamic programming method, the time complexity is the same, but we need at least O(N^2) Space complexity to store the DP table. Thus, in this problem, dp approach is not the best solution.

In addition, there is a clever solution to this problem. The time complexity only requires O(N), but the solution is more complicated. I personally don't think it is necessary to master it. The algorithm is called Manacher's Algorithm, and interested readers can search for it by themselves.

Stick to original high-quality articles, and strive to make clear the algorithm problems. Welcome to follow my Wechat official account "labuladong" for the latest articles.

! [labuladong] (../pictures/labuladong.png)