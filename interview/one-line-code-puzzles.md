# One-line Code Puzzles

**Translator: [tommytim0515](https://github.com/tommytim0515)**

**Author: [labuladong](https://github.com/labuladong)**

This is my summary of three interesting "brain teaser" puzzles from the problems I solved on LeetCode. They can all be solved by algorithmic programming. However, if you think a bit more, you may find the laws of them and figure them out directly.

### 1. Nim Game

The game rule is that there is a heap of stones on the table for you and friends to remove. Each of you takes turns to remove the stones and can take at least one and at most three each time. The one who takes the last stone will win the game. See more on [LeetCode page](https://leetcode.com/problems/nim-game/) and [Wikipedia](https://en.wikipedia.org/wiki/Nim).

Suppose both of you are very clever and have optimal strategies for the game, and you are the first one to take the stone. Write an algorithm to determine whether you can win the game given the number of stones in the heap. (Input a positive integer n, output true or false depending on whether you can win the game).

For instance, there are 4 stones in total, and the output should be false. Because no matter how many stones you take (1, 2, or 3), the opponent can always take the remaining at once including the last one. You are guaranteed to lose the game.

First of all, dynamic programming (DP) can be implemented into this problem, because you can find the repeated sub-problems. However, this method would be very complicated as it involves games played between you and your opponent, who are both clever.

**We usually use contrarian thinking to find a solution of this kind of problems**：

If I win the game, I need to take the remaining stones (1\\~3 stones) at once.

How to make this situation come into being? If there are 4 stones remaining when your opponent takes the chance to pick the stones, no matter how he takes the stones, you can always win the game because there will always be 1\~3 stones remaining.

And how to force your opponent to face the situation when there are 4 stones left? If there are 5\~7 stones remaining by the time you take your turn, you can let your opponent face 4-stone situation.

Then how to get into a 5\~7 stones situation when you are picking? Let your opponent face 8 stones. No matter how he plans to take the stones, we can win the game because of the remaining 5\~7 stones.

And so on, we can find out that if n is a multiple of 4, you will fall into the trap and can never win the game. The solution to this problem is very simple:

```cpp
bool canWinNim(int n) {
    // If n is a multiple of 4, then return false
    // Otherwise, return true
    return n % 4 != 0;
}
```

### 2. Stone Game

The game rule is that you and your friend play a game with piles of stones. The piles of stone are represented by an array, ```piles```. ```pile[i]``` refers to the number of stones in the ith pile. Each turn, a player takes the entire pile of stones from either the beginning or the end of the row. And the winner is the one who gets more stones in the end. See more on [LeetCode page](https://leetcode.com/problems/stone-game/).

**Suppose both of you are very clever and have optimal strategies for the game**, and you start first. Write an algorithm to determine whether you can win the game given the number of stones in the heap. (Input an array, pile, output true or false depending on whether you can win the game).

Please pay attention that the number of piles of stones should be even. So both of you get the same number of piles of stones. However, the total amount of stones is odd. So you are not able to get the same number of stones and there must be a winner.

For instance, `piles=[2, 1, 9, 5]`, you take first, you can choose 2 or 5 and you choose 2.

`piles=[1, 9, 5]`, your opponent's turn, he or she can choose 1 or 5, and he or she chooses 5.

`piles=[1, 9]`, your turn, you pick 9.

Finally, your opponent has no choice but choosing 1.

In summary, you get `2 + 9 = 11` stones in total, your opponents gets `5 + 1 = 6` stones. You win, the return value is true. 

As you can see that it is not always correct to choose the one with larger number of stones. Why you should choose 2 rather than 5 at the first time? Because 9 is behind 5. You will lose the game for giving the pile of 9 stones to the opponent for chasing a moment's gain.

And that is why we need to emphasize that both the players are clever. The algorithm is also to determine whether you can win with best decisions.

The problem also involves playing a game by the two players. It is very complicated to use "brute force" method like dynamic programming (DP). And if we think a bit deeper we will find out that

```java
boolean stoneGame(int[] piles) {
    return true;
}
```

Why we can write like this? There are two important conditions about the problem: the number of the pile of stones is even, while the total number of the stone is odd. These two conditions seem to increase the fairness of the game, while they indeed let it become a "leet-cutting" game. For instance, suppose the indexes of piles of stones are 1, 2, 3, 4 from start to end sequentially when `pile=[2, 1, 9, 5]`.

If we divide these four piles of stones into two groups according to whether the index is even or not, which equals 1, 3 in a group and 2, 4 in another group. The numbers of stones of these two groups are different as the total number of stones is odd.

As the first one to take the stones, you can decide to take all the even group or all the odd group at once.

In the beginning, you can choose the 1st pile or the 4th pile. If you want an even group, you can take the 4th pile. So that your opponent can only choose the 1st one or the 3rd one. No matter how he takes, you can choose the 2nd pile after that. Similarly, if you choose the 1st pile which is in the odd group, your opponent can only choose 2nd or 4th pile, no matter how he chooses, you can get the 3rd pile.

In other words, you can observe all the strategies at the first try. You can win the game by observing which group of stones is more, even or odd. Knowing this loophole, you can play a trick on your friend who doesn't know this.

### 3. Bulb Switcher

The description of the problem: there are n bulbs in a room and they are initially turned off. Now we need to do n operations:

1. Flip all the lights.

2. Flip lights with even numbers.

3. Flip the bulb whose number is a multiple of 3 (e.g. 3, 6, 9, ... and 3 is off while 6 is on).

For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb.

You need to find how many bulbs are on after n rounds. See more on [LeetCode page](https://leetcode.com/problems/bulb-switcher/).

We can simulate the condition with a boolean array, then count the result. However, this method is not smart enough. The best solution is as follows:

```java
int bulbSwitch(int n) {
    return (int)Math.sqrt(n);
}
```

What? What does this have to do with square roots? It's actually a pretty neat solution, and it's hard to figure out if nobody tells you how to do it.

First, because the lights are always off at the beginning, a certain light must be flipped an odd number of times if it is turned on at the end.

Let's say we only have six lights, and we're only looking at the sixth light and it's going to take six turns, right? How many times is the switch going to be pressed for the sixth light? It's not difficult to see that its switch will be pressed at the 1st, 2nd, 3rd and 6th round.

Why the light will be flipped at these rounds? Because `6=1*6=2*3`. In general, the factors come in pairs, which means that the number of times the switch is pressed is usually even, but in a special case, if there are 16 lights, how many times will the 16th light be flipped?

`16=1*16=2*8=4*4`

The factor 4 repeats, so the 16th light will be flipped 5 times which is odd, and now you understand the relationships to the square root, right?

But, we're going to figure out how many lights are on at the end, and what does that mean by square root? Just think about it a little bit.

Suppose we have 16 lights, and we take the square root of 16, which is equal to 4, and that means we're going to end up with 4 lights on. The lights are `1*1=1`, `2*2=4`, `3*3=9`, and `4*4=16`.

Some square root of n turns out to be a decimal. However, converting them to integers is the same thing as getting all the integers smaller than a certain integer upper bound, and the square roots of these numbers are the index of the lights on at last. so just turn the square root into an integer, that's the answer to the question.

