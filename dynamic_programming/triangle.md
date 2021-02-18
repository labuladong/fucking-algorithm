# Triangle
### Problem Link: https://leetcode.com/problems/triangle/
This is a conventional DP problem.
## Problem Statement
```
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, 
you may move to either index i or index i + 1 on the next row.
```
Example
```
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
```
The first mistake that I was tempted to do was to travel top to bottom and choose the minimum of the two numbers that were valid to be taken.This is a wrong approach.To understand,look at the following example.
```
triangle = [[2] , [3,4] , [10,12,-1]]
If you take 3 in the 2nd row,then you are bound to choose 10 or 12 from the next row which gives 
you a sum of 15 or 17 whereas by taking 4 from 2nd row,you can choose -1 from last row, giving you
a sum of 2+4+(-1) = 5,which is the minimum path sum.
```
So what can we do.A easy approach would be to move bottom up.Create a dp table and fill its last row with the last row of triangle.Then move up in this way
```
For the given example,say we have dp[4] = [4,1,8,3]
Now,
dp[3][1] = min(dp[4][1] , dp[4][2]) + triangle[3][1] = min(4,1) + 6 = 7
dp[3][2] = min(dp[4][2] , dp[4][3]) + triangle[3][2] = min(1,8) + 5 = 6
dp[3][3] = min(dp[4][3] , dp[4][4]) + triangle[3][3] = min(8,3) + 7 = 10
So the dp table created by far,looks like
-
- -
7 6 10
4 1 8 3
After filling the forst two rows,
11
9 10
7 6 10
4 1 8 3
The minimum path sum is dp[0][0] i.e.
```
Let's have a look at the code now,
```cpp
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        if(n==1)return triangle[0][0];
        
        int dp[n][n];
        for(int i=0;i<n;i++)
        {
            dp[n-1][i] = triangle[n-1][i];
        }
        for(int i=n-2;i>=0;i--)
        {
            for(int j=0;j<=i;j++)
            {
                dp[i][j] = min(dp[i+1][j] , dp[i+1][j+1]) + triangle[i][j];
            }
        }
        return dp[0][0];
    }
};
```
