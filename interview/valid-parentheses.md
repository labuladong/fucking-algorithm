# Valid Parentheses

**Translator: [andavid](https://github.com/andavid)**

**Author: [labuladong](https://github.com/labuladong)**

The valid of parentheses is a very common and practical problem. For example, the editor and the compiler would check the code we wrote whether the parentheses were correctly closed. As our code might contain the characters '(', ')', '{', '}', '[' and ']', it's a little bit difficult to determine.

This article is on an algorithm problem about valid parentheses. I believe it will help you to come to a better understanding of stack.

The problem is very simple. Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

```text
Input: "()[]{}"
Output: true

Input: "([)]"
Output: false

Input: "{[]}"
Output: true
```

Before solving this problem, let's lower the difficulty. If the given string contains only parentheses, i.e. '(' and ')', how to check if the string is valid?

## deal with parentheses

As the string contains only parentheses, if the string is valid we must make sure:

**every `)`'s left must have a corresponding `(`**.

For example: `()))((`, the two right parenthesis in the middle have no corresponding left parenthesis, so this string is not valid.

We can write out the algorithm according to this thought.

```cpp
bool isValid(string str) {
    // the number of left parenthesis to be matched
    int left = 0;
    for (char c : str) {
        if (c == '(')
            left++;
        else // encounter right parenthesis
            left--;

        if (left < 0)
            return false;
    }
    return left == 0;
}
```

If the string contains only one parentheses, the algorithm above will work. As for the case with three kind of parentheses, At first I imitate this thought, define three variables `left1`, `left2` and `left3`, each handle one parentheses. Although we need to write a lot of if-else branches, it seems to solve the problem.

But actually, it doesn't work. For example, `(())` is valid in the case with one parentheses, while `[(])` is not valid in the case with multiple parentheses.

Only recording the number of times that left parenthesis occurs is not enough to make the right judgments. We need to increase the information we stored. We can use stack to imitate similar thoughts.

## deal with multiple parentheses

Stack is a FILO(first in last out) data structure. It's very useful in dealing with parentheses.

In this problem, we use a `left` stack instead of the `left` variable before. **Having left parenthesis into stack, as for right parenthesis, find the recent left parenthesis in the stack, and then check if matched.**.

```cpp
bool isValid(string str) {
    stack<char> left;
    for (char c : str) {
        if (c == '(' || c == '{' || c == '[')
            left.push(c);
        else // character c is right parenthesis
            if (!left.empty() && leftOf(c) == left.top())
                left.pop();
            else
                // not match with recent left parenthesis
                return false;
    }
    // whether all left parenthesis are matched
    return left.empty();
}

char leftOf(char c) {
    if (c == '}') return '{';
    if (c == ')') return '(';
    return '[';
}
```
