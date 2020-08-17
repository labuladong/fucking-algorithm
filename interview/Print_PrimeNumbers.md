# How to find prime Numbers efficiently

**Translator: [shazi4399](https://github.com/shazi4399)**

**Author: [labuladong](https://github.com/labuladong)**

The definition of a prime number seems simple,which is said to be prime number if it can be divided by 1 and itself.

However,don't think that the definition of prime numbers is simple. I am afraid that few people can write a prime-related algorithm that works really efficiently. Let's say you write a function like this:

```java
// Returns several primes in the interval [2, n) 
int countPrimes(int n)

// E.g. countPrimes (10) returns 4
// Because 2,3,5,7 is prime numbers
```

How would you program this function? I think you maybe write like this:

```java
int countPrimes(int n) {
    int count = 0;
    for (int i = 2; i < n; i++)
        if (isPrim(i)) count++;
    return count;
}

// Determines whether integer n is prime
boolean isPrime(int n) {
    for (int i = 2; i < n; i++)
        if (n % i == 0)
            // There are other divisibility factors
            return false;
    return true;
}
```

The time complexity is O (n ^ 2), which is a big problem.**First of all, the idea of using the isPrime function to assist is not efficient; and even if you want to use the isPrime function, there is computational redundancy in writing the algorithm**.

Let's briefly talk about **how to write an algorithm if you want to determine whether a number is prime or not**. Just slightly modify the for loop condition in the isPrim code above:

```java
boolean isPrime(int n) {
    for (int i = 2; i * i <= n; i++)
        ...
}
```

In other words, `i` does not need to traverse to` n`, but only to `sqrt (n)`. Why? let's take an example, suppose `n = 12`.

```java
12 = 2 × 6
12 = 3 × 4
12 = sqrt(12) × sqrt(12)
12 = 4 × 3
12 = 6 × 2
```

As you can see, the last two products are the reverse of the previous two, and the critical point of inversion is at `sqrt (n)`.

In other words, if no divisible factor is found within the interval `[[2, sqrt (n)]`, you can directly conclude that `n` is a prime number, because in the interval `[[sqrt (n), n] ` Nor will you find a divisible factor.

Now, the time complexity of the `isPrime` function is reduced to O (sqrt (N)), ** but we don't actually need this function to implement the` countPrimes` function. The above just hope that readers understand the meaning of `sqrt (n)`, because it will be used again later.


### Efficient implementation `countPrimes`

The core idea of efficiently solving this problem is to reverse the conventional idea above:

First from 2, we know that 2 is a prime number, then 2 × 2 = 4, 3 × 2 = 6, 4 × 2 = 8 ... all are not prime numbers.

Then we found that 3 is also a prime number, so 3 × 2 = 6, 3 × 3 = 9, 3 × 4 = 12 ... are also impossible to be prime numbers.

Seeing this, do you understand the logic of this exclusion method a bit? First look at our first version of the code:

```java
int countPrimes(int n) {
    boolean[] isPrim = new boolean[n];
    // Initialize the arrays to true
    Arrays.fill(isPrim, true);

    for (int i = 2; i < n; i++) 
        if (isPrim[i]) 
            // Multiples of i cannot be prime
            for (int j = 2 * i; j < n; j += i) 
                    isPrim[j] = false;
    
    int count = 0;
    for (int i = 2; i < n; i++)
        if (isPrim[i]) count++;
    
    return count;
}
```

If you can understand the above code, then you have mastered the overall idea, but there are two subtle areas that can be optimized.

First of all, recall the `isPrime` function that just judges whether a number is prime. Due to the symmetry of the factors, the for loop only needs to traverse` [2, sqrt (n)] `. Here is similar, our outer for loop only needs to traverse to `sqrt (n)`:

```java
for (int i = 2; i * i < n; i++) 
    if (isPrim[i]) 
        ...
```

In addition, it is difficult to notice that the inner for loop can also be optimized. Our previous approach was:

```java
for (int j = 2 * i; j < n; j += i) 
    isPrim[j] = false;
```

This can mark all integer multiples of `i` as` false`, but there is still computational redundancy.

For example, when `n = 25` and` i = 4`, the algorithm will mark numbers such as 4 × 2 = 8, 4 × 3 = 12, and so on, but these two numbers have been marked by 2 × 4 and 3 × 4 that is `i = 2` and` i = 3`.

We can optimize it slightly so that `j` traverses from the square of` i` instead of starting from `2 * i`:

```java
for (int j = i * i; j < n; j += i) 
    isPrim[j] = false;
```

In this way, the algorithm for counting prime numbers is efficiently implemented. In fact, this algorithm has a name, which called Sieve of Eratosthenes. Take a look at the complete final code:

```java
int countPrimes(int n) {
    boolean[] isPrim = new boolean[n];
    Arrays.fill(isPrim, true);
    for (int i = 2; i * i < n; i++) 
        if (isPrim[i]) 
            for (int j = i * i; j < n; j += i) 
                isPrim[j] = false;
    
    int count = 0;
    for (int i = 2; i < n; i++)
        if (isPrim[i]) count++;
    
    return count;
}
```

**The time complexity of this algorithm is difficult to calculate**.It is obvious that the time is related to these two nested for loops. The operands should be:

  n/2 + n/3 + n/5 + n/7 + ...
= n × (1/2 + 1/3 + 1/5 + 1/7...)

In parentheses, ther is the inverse of the prime number .The final result is  O(N * loglogN),and readers interested in this can refer to the time complexity of the algorithm

That is all about how to find prime Numbers.The seemingly simple problem does has a lot of details to polish
