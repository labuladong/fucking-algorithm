/*
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Example
Example 1:

Input: [4, 5, 1, 2, 3] and target=1, 
Output: 2.
Example 2:

Input: [4, 5, 1, 2, 3] and target=0, 
Output: -1.
Challenge
O(logN) time


二 | 一
--------
三 | 四

       /
      /
     M1
    /
   /
  S    
              E
             /
            /
           M2
          /
         /
        /

这个问题也是用二分法来做，但是要考虑清楚每次劈二分的时候 mid 在那里 以及 target在哪里

1. 劈的这一刀在第二象限 即M1处。
  1.1 Target在S -> M1 之间
  1.2 Target在M1的右边而且还在这个象限
  1.3 Target在M1的右边但是落在了第四象限

2. 劈的这一刀在第四象限 即M2处
  2.1 Target在M2 -> E之间
  2.2 Target在M2的左边而且还在这个象限
  2.3 Target在M2的左边但是却在第二象限
      
*/

class Solution {
    public int search(int[] A, int target) {
        if (A.length == 0 || A == null) {
            return -1;
        }
        int start = 0, end = A.length - 1;
        
        while (start + 1 < end) {
            int mid = start + (end - start)/2;
            if (A[mid] == target) {
                return mid;
            }
            //1. mid在第2象限
            if (A[mid] > A[start] && target < A[mid] && target >= A[start]) { //1.1
                end = mid;
            }
            else if (A[mid] > A[start] && target > A[mid]) { //1.2
                start = mid;
            }
            else if (A[mid] > A[start] && target < A[start]) { //1.3
                start = mid;
            }
            //2. mid第4象限
            else if (A[mid] < A[end] && target > A[mid] && target <= A[end]) { //2.1
                start = mid;
            }
            else if (A[mid] < A[end] && target < A[mid]) { //2.2
                end = mid;
            }
            else { //2.3
                end = mid;
            }
        }
        
        if (A[start] == target) {
            return start;
        }
        
        if (A[end] == target) {
            return end;
        }
        
        return -1;        
    }
}